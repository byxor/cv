from collections import namedtuple

Job = namedtuple("Job",
                 ["company",
                  "location",
                  "role",
                  "start_date",
                  "end_date",
                  "technologies",
                  "description"])

Language = namedtuple("Language", ["name", "usage"])

ExtraLanguage = namedtuple("ExtraLanguage", ["name"])

Project = namedtuple("Project", ["name", "link", "description", "technologies"])

Hackathon = namedtuple("Hackathon", ["name", "year", "description"])

Date = namedtuple("Date", ["month", "year"])
