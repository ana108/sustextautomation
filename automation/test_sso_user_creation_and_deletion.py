import re
from playwright.sync_api import Page, expect
from configuration import Configuration
import pytest

@pytest.fixture(scope="session")
def config():
    """Load configuration once per test session."""
    return Configuration()

@pytest.fixture(scope="session")
def staging_url(config):
    """returning the stagind host url"""
    url = config.get_staging_host()
    # print(f"[CONFIG] Using Staging url: {url}")
    return url

@pytest.fixture(scope="session")
def login_details(config):
    """returning the text sso user_email and password"""
    email = config.get_google_user()
    pwd = config.get_google_password()
    return email, pwd

def test_sso_user_creation(page: Page, staging_url:str, login_details: str):
    page.goto(staging_url)

    email, password = login_details

    page.get_by_role("button", name="Sign in").click()
    with page.expect_popup() as page1_info:
        # page.locator("iframe[title=\"Sign in with Google Button\"]").content_frame.get_by_role("button", name="Sign in with Google. Opens in").click()
        page.get_by_role("button", name="Sign in with Google. Opens in new tab").click()
    page1 = page1_info.value
    page1.wait_for_load_state()
    page1.get_by_role("textbox", name="Email or phone").click()
    page1.get_by_role("textbox", name="Email or phone").fill(email)
    page1.get_by_role("button", name="Next").click()
    page1.get_by_role("textbox", name="Enter your password").fill(password)
    page1.get_by_role("button", name="Next").click()
    # page1.get_by_role("button", name="Continue").click()
    expect(page.get_by_role("link", name="Logout")).to_be_visible
    

