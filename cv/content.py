from cv.structures import *
from cv.helpers import *

_primary_languages = [
    Language("Go", "Introduced me to goroutines and channels as a concurrency model."),
    Language("Python", "Essential language for degree. Used in year-long team project and many personal projects."),
    Language("Kotlin", "Used in production environments to write HTTP backends."),
    Language("JavaScript (ES6/ES7)", "Used for web development with Angular. Familiar with ES6 features."),
    Language("Java", "First taste of OOP, used frequently in many early projects."),
    Language("C", "Taught me about memory management, the stack, the heap, pointers."),
    Language("C++", "Used to program ASICs in Arista switches and solve competitive programming problems."),
]

_extra_languages = [
    ExtraLanguage("Haskell"),
    ExtraLanguage("x86"),
    ExtraLanguage("x64"),
    ExtraLanguage("LIMP"),
    ExtraLanguage("UnityScript"),
    ExtraLanguage("Ruby"),
    ExtraLanguage("Clojure"),
    ExtraLanguage("Prolog"),

]

_jobs = [
    Job("Instil Software",
        "Belfast",
        "Software Engineering Intern",
        Date("July", 2016),
        Date("September", 2016),
        ["Kotlin", "AngularJS", "DropWizard", "PostgreSQL", "Swagger"],
        "Full Stack Developer for a Time Tracking Tool. Built REST API & Email Service with Kotlin. "
        "Increased test coverage by ~15% in first month. Maintained AngularJS frontend. "
        "Received first-class training on Test-Driven Development and Refactoring."),

    Job("Arista Networks",
        "Dublin",
        "Software Engineering Intern",
        Date("June", 2017),
        Date("June", 2018),
        ["TACC", "C++", "C", "SSH", "Perforce"],
        "Wrote & tested C++ deployed on high-performance switches around the world. "
        "Worked exclusively in command-line environments using SSH, Tmux & Emacs. "),
]

_projects = [
    Project(
        "LIMP",
        github("limp"),
        "Functional Programming Language Interpreter with 99% Test Coverage. Supports anonymous functions, objects, collections, strings, recursion, immutability, scoped constants, and a small standard library.",
        ["Python3.6"]),

    Project(
        "Entua",
        "",
        "Android/iOS IoT app. Go WebSocket backend. Android/iOs frontend with React Native & Redux. ",
        ["Go", "ES6", "React Native", "Redux"]),

    Project(
        "byxor.xyz",
        github("website"),
        "My personal website.",
        ["Angular 5", "TypeScript"]),

    # Project(
    #     "Try LIMP - WebApp",
    #     None,
    #     "A full-stack application to execute LIMP code in the browser. Web client written with ES6, JQuery and Bootstrap 3. Backend is a REST API written in Python using Flask, running on DigitalOcean VPS. Try it out at byxor.xyz/try-limp."),

    Project(
        "Passflip",
        github("passflip"),
        "A lightweight SHA224-based password manager.",
        []),

    Project(
        "Slimput",
        github("slimput"),
        "A faster way of scanning standard input for Java.",
        []),

    Project(
        "Kapoki",
        github("kapoki"),
        "A multi-language skeleton generator for new projects.",
        []),

    Project(
        "Thought",
        github("thought"),
        "A compiler/tool to encourage articulated, exploratory, disciplined thinking.",
        []),

    Project(
        "DecayQueueJs",
        github("DecayQueueJs"),
        "A JavaScript Data Structure that removes old elements automatically.",
        []),
]

_events = [
    Hackathon("YRS Festival of Code",
              2014,
              "Week long. Competed in Plymouth, England as First Northern Irish team to compete. Awarded semi-finalists in 'Should Exist' category."),

    Hackathon("YRS Festival of Code", 2015, ""),
    Hackathon("Global Game Jam", 2015, ""),
    Hackathon("AIB Data Hack", 2016, ""),
    Hackathon("Google Hash Code", 2017, ""),
    Hackathon("Arista Hack-a-Switch", 2017, ""),
]


class Data:
    name = "Brandon Ibbotson"
    email = decode("oenaqba.voobgfba2@znvy.qph.vr")
    website = "www.byxor.xyz"
    github = "www.github.com/byxor"
    stack_overflow = "www.stackoverflow.com/users/5601284"
    skills = ["Test-Driven Development", "Agile", "Git"]
    primary_languages = _primary_languages
    extra_languages = _extra_languages
    jobs = _jobs
    projects = _projects
    events = _events
