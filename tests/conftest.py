import pytest
from selene.support.shared import browser

url = "https://demoqa.com/"


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = url
    browser.open('automation-practice-form')
