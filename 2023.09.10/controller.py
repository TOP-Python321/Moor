from model import Email, FileIO
from view import CLI


class Application:
    def __init__(self, email_model: Email):
        self.email_model = email_model

    def save_email(self, email: str):
        try:
            self.email_model.email = email
            FileIO.add_email(email)
            CLI.show_save_message()
        except ValueError as ex:
            CLI.show_incorrect_message()

    def run_app(self):
        while True:
            email = CLI.input_email()
            if email == '':
                break
            self.save_email(email)
