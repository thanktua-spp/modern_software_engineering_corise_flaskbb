from flask import url_for
import os
import pytest
from flaskbb import create_app
from flaskbb.configs.testing import TestingConfig as Config
from flaskbb.extensions import db
from flaskbb.utils.populate import create_default_groups, create_default_settings
from flaskbb.utils.translations import compile_translations
from playwright.sync_api import Page, expect

os.environ['FLASK_ENV'] = 'development'
###################################################################
# CoRise TODO: add a new fixture `translations` that calls the
# `compile_translations` function from flaskbb.utils.translations

# ADD CODE HERE

@pytest.fixture(scope="session")
def app():
    # Hint: create the app, and setup any default context like translations,
    # settings, DB, etc.
    # Hint: take a look at the tests/fixtures/app.py file for the details of 
    # how to configure the application.
    # TODO: ADD CODE HERE
    #pass
    app = create_app(Config)
    
    with app.app_context():
        db.create_all()
        create_default_groups()
        create_default_settings()
        compile_translations()

    return app


def test_create_new_account(live_server, page: Page):
    # Hint: Check out `flask.url_for` helper function to get the external url for 
    # an endpoint. Then go to it using playwright's `page.goto(url)`
    # TODO: ADD CODE HERE
    url=url_for('forum.index', _external=True)

    page.goto(url)
    expect(page).to_have_title("FlaskBB - A lightweight forum software in Flask")

###################################################################