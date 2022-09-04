from demoqa_tests.app import app


def test_registration_form():
    (app.registration_form
     .set_first_name('Daniil')
     .set_last_name('M')
     .set_user_email('test@mail.ru')
     .set_gender('Male')
     .set_phone_number('1234567890')
     .set_birth_date('15.08.1989')
     .set_subjects('Computer Science', 'English')
     .set_hobbies('Sports', 'Reading', 'Music')
     .set_picture('fry.jpeg')
     .set_address('Love street')
     .set_state('Haryana')
     .submit()
     )

    # check results
    app.result_registered_user_dialog.table_row(1, value='Daniil M')
    app.result_registered_user_dialog.table_row(2, value='test@mail.ru')
    app.result_registered_user_dialog.table_row(3, value='Male')
    app.result_registered_user_dialog.table_row(4, value='1234567890')
    app.result_registered_user_dialog.table_row(5, value='15 August,1989')
    app.result_registered_user_dialog.table_row(6, value='Economics, English, Arts')
    app.result_registered_user_dialog.table_row(7, value='Sports, Music')
    app.result_registered_user_dialog.table_row(8, value='fry.jpeg')
    app.result_registered_user_dialog.table_row(9, value='Love street')
    app.result_registered_user_dialog.table_row(10, value='NCR Deli')