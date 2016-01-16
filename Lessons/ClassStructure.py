from Utils.InvalidConstructionException import InvalidConstructionException


class Unit:
    def __init__(self, name, lessons, unit_id):
        self.name = name
        self.lessons = lessons
        self.unit_id = unit_id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.unit_id

    def get_lessons(self):
        return self.lessons

    def __str__(self):
        return self.name + ":\t" + str(self.lessons)

    def __repr__(self):
        return self.__str__()


class Lesson:
    def __init__(self, lesson_id, title, description, briefing, introduction, assignments=[]):
        if title is None or description is None or briefing is None or introduction is None or lesson_id is None:
            raise InvalidConstructionException("Invalid Construction of Lesson")
        self.title = title
        self.description = description
        self.briefing = briefing
        self.introduction = introduction
        self.assignments = assignments
        self.lesson_id = lesson_id

    def get_title(self):
        return self.title

    def get_id(self):
        return self.lesson_id

    def get_description(self):
        return self.description

    def get_briefing(self):
        return self.briefing

    def get_introduction(self):
        return self.introduction

    def get_assignments(self):
        return self.assignments

    def __str__(self):
        return self.title + ":\t" + str(self.description)

    def __repr__(self):
        return self.__str__()


class Assignment:
    def __init__(self, description, content, title):
        if title is None or description is None or content is None:
            raise InvalidConstructionException(
                "Please supply description, content and title for exercise object to be constructed")
        self.title = title
        self.description = description
        self.content = content

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_content(self):
        return self.content

    def __str__(self):
        return "Exercise: " + self.title + "\t" + self.description

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return self.__str__()
