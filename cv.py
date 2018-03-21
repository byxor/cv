from collections import namedtuple

Date = namedtuple("Date", "month year")
Language = namedtuple("Language", "name usage")
ExtraLanguage = lambda name: Language(name, "")
Hackathon = namedtuple("Hackathon", "name year description")
Job = namedtuple("Job", "company location role start_date end_date technologies description")
Project = namedtuple("Project", "name link description")

github = lambda project: f"http://www.github.com/byxor/{project}"

##############################################################

SKILLS = [
    "Test Driven Development",
    "Agile Development",
]

PRIMARY_LANGUAGES = [
    Language("Java",             "Over 4 years of experience and consistent use in personal projects."),
    Language("Python 3",         "Essential language for degree. Used in year-long team project and many personal projects."),
    Language("C++",              "Used to program ASICs in Arista switches and solve competitive programming problems."),
    Language("Kotlin",           "Used in production environment to write HTTP backend."),
    Language("JavaScript (ES6)", "Used for web development with AngularJS. Familiar with ES6 features."),
    Language("C",                "Taught me about memory management, the stack, heap and pointers."),
]

EXTRA_LANGUAGES = [
    ExtraLanguage("Go"),
    ExtraLanguage("Ruby"),
    ExtraLanguage("x86 Assembly (MASM)"),
    ExtraLanguage("Prolog"),
    ExtraLanguage("Clojure"),
    ExtraLanguage("UnityScript"),
]

JOBS = [
    Job("Instil Software",
        "Belfast",
        "Software Engineering Intern",
        Date("July", 2016),
        Date("September", 2016),
        ["Kotlin", "AngularJS", "DropWizard", "PostgreSQL", "Swagger"],
        ""),

    Job("Arista Networks",
        "Dublin",
        "Software Engineering Intern",
        Date("June", 2017),
        "Present",
        ["C++", "C", "Embedded", "Command-line"],
        ""),
]

PROJECTS = [
    Project("LIMP Programming Language",
            github("limp"),
            "An interpreter for my functional programming language with 98% test coverage. Supports anonymous functions, collections, strings, recursion, immutability, scoped constants, and a small standard library. Soon to support objects and modules. Written in python3.6."),

    Project("Passflip",
            github("passflip"),
            "A lightweight SHA224-based password manager.")
]
