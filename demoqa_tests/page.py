from selene import command, have
from selene.support.shared import browser

from demoqa_tests.ui.datepicker import DatePicker
from demoqa_tests.ui.dropdown import Dropdown
from demoqa_tests.ui.input_tags import InputTags
from demoqa_tests.utils import get_abspath


def submit_form():
    browser.element('#submit').perform(command.js.click)


class RegistrationForm:
    def __init__(self):
        self.birth_date = DatePicker(browser.element('#dateOfBirthInput'))

    def set_first_name(self, param):
        browser.element('#firstName').type(param)
        return self

    def set_last_name(self, param):
        browser.element('#lastName').type(param)
        return self

    def set_user_email(self, param):
        browser.element('#userEmail').type(param)
        return self

    def set_gender(self, param):
        browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text(param)).click()
        return self

    def set_phone_number(self, param):
        browser.element('#userNumber').type(param)
        return self

    def set_birth_date(self, birth_date):
        self.birth_date.add(birth_date)
        return self

    def set_subjects(self, *names):
        for name in names:
            InputTags(browser.element('#subjectsInput')).add(name)
        return self

    def set_hobbies(self, *values):
        hobbies_list = {
            'Sports': '[for=hobbies-checkbox-1]',
            'Reading': '[for=hobbies-checkbox-2]',
            'Music': '[for=hobbies-checkbox-3]'
        }
        for value in values:
            browser.element(hobbies_list[value]).click()
        return self

    def set_picture(self, image):
        browser.element('#uploadPicture').send_keys(get_abspath(image))
        return self

    def set_address(self, param):
        browser.element('#currentAddress').type(param)
        return self

    def set_state(self, param):
        browser.element('#state').type(param)
        return self

    def set_city(self, param):
        browser.element('#city').autocomplete(param)
        return self

    @staticmethod
    def submit():
        browser.element('#submit').perform(command.js.click)
