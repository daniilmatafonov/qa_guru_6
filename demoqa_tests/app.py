from demoqa_tests.page import RegistrationForm
from demoqa_tests.ui.result_table import ResultTable


class App:
    result_registered_user_dialog = ResultTable
    registration_form = RegistrationForm()


app = App