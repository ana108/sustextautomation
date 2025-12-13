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
    print(f"[CONFIG] Using Staging url: {url}")
    return url

def test_login_form_opens(page: Page, staging_url: str):
    """
    Docstring for test_login_form_opens
    
    :param page: Description
    :type page: Page
    :param staging_url: Description
    :type staging_url: str
    """
    
    page.goto(staging_url)

    #finds the sign in button and clicks on it
    page.get_by_role("button", name="Sign in").click()
    
    #checks if the form open after clicking on the sign in button
    expect(page.get_by_role("heading", name="Welcome to   Sustainable Text!")).to_be_visible()

def test_login_faliure(page: Page, staging_url : str):
    page.goto(staging_url)

    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("textbox", name="Login").fill("arpanraval223@gmail.com")
    page.get_by_role("textbox", name="Password").fill("@Rp@n2242")
    page.get_by_role("button", name="Continue").click()
    expect(page.get_by_text("Invalid password. Please try again")).to_be_visible()

