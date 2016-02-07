__author__ = 'varun'

from google_spreadsheet.api import SpreadsheetAPI
from educoding.settings import GOOGLE_DRIVE_FOLDER_KEY, GOOGLE_DRIVE_PASSWORD, GOOGLE_DRIVE_USERNAME, \
    SUBCRIPTION_SPREADSHEET_KEY, SUBCRIPTION_WORKSHEET_KEY

__api = SpreadsheetAPI(GOOGLE_DRIVE_USERNAME, GOOGLE_DRIVE_PASSWORD, GOOGLE_DRIVE_FOLDER_KEY)

__subscription_sheet = __api.get_worksheet(SUBCRIPTION_SPREADSHEET_KEY, SUBCRIPTION_WORKSHEET_KEY)


def add_subscriber(email):
    __subscription_sheet.insert_row({'email': email})


