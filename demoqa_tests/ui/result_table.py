from typing import Optional

from selene import have
from selene.support.shared import browser


class ResultTable:
    def __init__(self, css_class: Optional[str] = None, tr: Optional[str] = None):
        self.element = browser.element(css_class).all(tr) if css_class and tr else browser.element('.table').all('tr')

    def table_row(self, /, *, value):
        browser.element('.table').all("tr")[self].element('td:nth-child(2)').should(have.exact_text(value))
