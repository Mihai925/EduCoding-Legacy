import requests
from django.conf import settings


class Compiler():
    def __init__(self, code, language_id=0, program_input=""):
        self.code = code
        self.language_id = language_id
        self.program_input = program_input

    def change_input(self, file_input):
        self.program_input = file_input

    def compile(self):
        r = None
        try:
            r = requests.post(settings.COMPILER_API,
                              data={"language": self.language_id, "code": self.code, "stdin": self.program_input})
        except Exception as e:
            # Log the error, alert the monitors
            pass
        if r.ok:
            return r
        # log and alert
        return None
