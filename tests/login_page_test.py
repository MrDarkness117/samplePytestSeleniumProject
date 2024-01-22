import json
import logging
import pytest
from paths import credentials
from page_objects.github_auth_page import GitHubPage as Page


@pytest.mark.auth
def test_auth_page_fail(setup_login):
    logging.info("Test Fail Auth")
    verification_text = "Incorrect username or password."
    page = Page(driver=setup_login)
    page.go()
    page.username_field.input_text("mromantsov@gmail.com")
    page.password_field.input_text("abcd")
    page.login_button.click()
    page.verification_step_fail.verify_has_text(verification_text)


@pytest.mark.auth
def test_auth_page_existing_user(setup_login):
    logging.info("Test Successful Auth")
    verification_text_logged_in = "Dashboard"
    verification_text_logged_out = "Sign up for GitHub"
    # Должен содержать логин/пароль от вашего GitHub! Информацию менять в auth_creds.json - key: login, value: password
    with open(credentials, "r", encoding="utf-8") as f:
        creds = json.load(f)
        f.close()
    page = Page(driver=setup_login)
    page.go()
    page.username_field.input_text(list(creds.keys())[0])
    page.password_field.input_text(creds[list(creds.keys())[0]])
    page.login_button.click()
    page.dashboard_title.verify_has_text(verification_text_logged_in)
    page.user_avatar.click()
    page.sign_out.click()
    page.sign_out_submit.click()
    page.sign_up_button.verify_has_text(verification_text_logged_out)
