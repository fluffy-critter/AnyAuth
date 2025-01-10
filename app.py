""" A rogue IndieAuth authorization_endpoint test

pipenv run flask run -p 6789
"""

import urllib.parse

import flask
import itsdangerous

app = flask.Flask(__name__)  # pylint:disable=invalid-name

sign = itsdangerous.URLSafeSerializer('key')  # pylint:disable=invalid-name


@app.route('/', methods=('GET', 'POST'))
@app.route('/<path:path>', methods=('GET', 'POST'))
def endpoint(path=''):
    """ Do-all endpoint """
    get = flask.request.args
    post = flask.request.form

    # Client code verification
    if 'code' in post:
        url, scope = sign.loads(post['code'])
        return flask.jsonify({'me': url, 'scope': scope})

    # User login completed
    if 'me' in post:
        redir = post['redirect_uri']
        args = urllib.parse.urlencode({
            'code': sign.dumps((post['me'], post.get('scope', 'read'))),
            'state': post.get('state'),
            'me': post['me']
        })

        return flask.redirect(redir + ('&' if '?' in redir else '?') + args)

    # Login requested
    if 'redirect_uri' in get:
        return flask.render_template('login.html', get=get, path=path)

    return flask.render_template('index.html', path=path)

from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

