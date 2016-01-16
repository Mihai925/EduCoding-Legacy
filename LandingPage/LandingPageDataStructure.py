__author__ = 'varun'


class Feature:
    def __init__(self, title, description, icon):
        self.title = title
        self.description = description
        self.icon = icon

    def get_icon(self):
        return self.icon

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description


class LandingPage:
    def __init__(self, features, description):
        self.description = description
        self.features = features

    def get_features(self):
        return self.features

    def get_description(self):
        return self.description