from collections import namedtuple

Job = namedtuple("Job",
                 ["company",
                  "location",
                  "role",
                  "start_date",
                  "end_date",
                  "technologies",
                  "description"])

Education = namedtuple("Education",
                       ["institution",
                        "location",
                        "type",
                        "name",
                        "short_name",
                        "start_date",
                        "end_date",
                        "description"])

Language = namedtuple("Language", ["name", "usage"])

ExtraLanguage = namedtuple("ExtraLanguage", ["name"])

Project = namedtuple("Project", ["name", "link", "description", "technologies"])

Hackathon = namedtuple("Hackathon", ["name", "year", "description"])

Date = namedtuple("Date", ["month", "year"])
