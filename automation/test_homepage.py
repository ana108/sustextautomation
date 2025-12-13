import re
import pytest
from playwright.sync_api import Page, expect
# from automation.configuration import Configuration
from configuration import  Configuration

# def setup():
#     conf = Configuration()
#     print("Get staging host ", conf.get_staging_host())

# def test_has_title(page: Page):
#     conf = Configuration()
#     print("Calling setup")
#     setup()
#     # page.goto("https://sustainabletext.ca")
#     page.goto(conf.get_staging_host())

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("sustainabletext.ca"))
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

def test_has_title(page: Page, staging_url: str):
    """
    Verify that the homepage title contains 'sustainabletext.ca'

    """
    page.goto(staging_url)
    expect(page).to_have_title(re.compile("sustainabletext.ca"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    #Test comment
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
