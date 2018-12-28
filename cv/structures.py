from collections import namedtuple

Job = namedtuple("Job",
                 ["company",
                  "location",
                  "role",
                  "dates",
                  "technologies",
                  "description"])

Education = namedtuple("Education",
                       ["institution",
                        "location",
                        "type",
                        "name",
                        "short_name",
                        "dates",
                        "description"])

Language = namedtuple("Language", ["name", "usage"])

ExtraLanguage = namedtuple("ExtraLanguage", ["name"])

Project = namedtuple("Project", ["name", "link", "description", "technologies"])

Hackathon = namedtuple("Hackathon", ["name", "year", "description"])


class Date(namedtuple("Date", ["month", "year"])):
    def __str__(self):
        return f"{self.month} {self.year}"


class DateRange(namedtuple("DateRange", ["start", "end"])):
    def __str__(self):
        return f"{self.start} - {self.end}"
