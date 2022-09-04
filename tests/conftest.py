import time
import pytest
from selene import have, command
from selene.support.shared import browser

url = "https://demoqa.com/"


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = url
    browser.open('automation-practice-form')
# time.sleep(1)
# (
#     browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
#     .with_(timeout=10)
#     .should(have.size_greater_than_or_equal(3))
#     .perform(command.js.remove)
# )
