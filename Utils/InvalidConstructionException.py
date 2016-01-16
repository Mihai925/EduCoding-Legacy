__author__ = 'varun'


class InvalidConstructionException(Exception):
    def __init__(self, message=""):
        Exception.__init__(self, message=message)