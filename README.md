# AnyAuth
An IndieAuth endpoint that will report whatever identity URL you want

This is intended for testing the correctness of an IndieAuth client, particularly in handling [differing profile URLs](https://indieauth.spec.indieweb.org/#differing-user-profile-urls).

It should not be used for actually logging into websites beyond testing their conformance.

## Installation

This is a very simple Flask application; please see the [Flask deployment guide](https://flask.palletsprojects.com/en/1.1.x/deploying/) for more information.

## Usage

When prompted to sign in to an IndieAuth client, provide an identity URL that starts with your AnyAuth endpoint; for example if you're running at `https://anyauth.example.com/` you can use an identity URL such as `https://anyauth.example.com/test_user` or the like.

Then when you are prompted for login confirmation, provide whatever "canonical" identity URL you want. If the client implements differing profile URLs correctly, it should accept the canonical URL if and only if it matches that portion of the IndieAuth spec (linked above).

## Test cases

Per the spec as of March 2019, the following cases should succeed:

* any case where the domain matches exactly (e.g. `https://anyauth.example.com/foo` &rarr; `http://anyauth.example.com/bar` should succeed)

And anything else should fail.
