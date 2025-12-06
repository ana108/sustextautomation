import re
from playwright.sync_api import Page, expect
# from automation.configuration import Configuration
from configuration import  Configuration

def setup():
    conf = Configuration()
    print("Get staging host ", conf.get_staging_host())

def test_has_title(page: Page):
    print("Calling setup")
    setup()
    page.goto("https://sustainabletext.ca")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("sustainabletext.ca"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
