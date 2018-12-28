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
    Job("Arista Networks",
        "Dublin",
        "Software Engineering Intern",
        DateRange(Date("June", 2017), Date("June", 2018)),
        ["TACC", "C++", "C", "Perforce"],
        "Wrote/Tested/Deployed TACC & C++ on high-performance switches around the world. "
        "Maintained Arista EOS Operating System. Worked exclusively in CLI over SSH. "
        "Interacted with switch hardware to toggle various features."),

    Job("Instil Software",
        "Belfast",
        "Software Engineering Intern",
        DateRange(Date("July", 2016), Date("September", 2016)),
        ["Kotlin", "AngularJS", "DropWizard", "PostgreSQL", "Swagger"],
        "Full Stack Developer. Built REST API & Email Service with Kotlin. "
        "Increased test coverage by ~15% in first month. Maintained AngularJS frontend. "
        "Received first-class training on TDD and Refactoring."),
]

_educations = [
    Education("Dublin City University",
              "Ireland",
              "BSc.",
              "Computational Problem Solving & Software Development",
              "C.P.S.S.D.",
              DateRange(Date("September", 2015), Date("June", 2019)),
              "Innovative degree program for students with pre-existing programming experience.",
              "www.cpssd.net"),
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
        "Android/iOS IoT app to configure events on smart devices within the Home. React-Native frontend. Go WebSocket backend. Raspberry Pi Hub.",
        ["Go", "ES6", "React-Native", "Redux"]),

    Project(
        "byxor.xyz",
        github("website"),
        "Personal website.",
        ["Angular 5", "TypeScript"]),

    # Project(
    #     "Try LIMP - WebApp",
    #     None,
    #     "A full-stack application to execute LIMP code in the browser. Web client written with ES6, JQuery and Bootstrap 3. Backend is a REST API written in Python using Flask, running on DigitalOcean VPS. Try it out at byxor.xyz/try-limp."),

    Project(
        "Passflip",
        github("passflip"),
        "A lightweight SHA224-based password manager. Installable via pip.",
        ["Python"]),

    Project(
        "Slimput",
        github("slimput"),
        "Faster input scanners for Java.",
        ["Java"]),

    Project(
        "Kapoki",
        github("kapoki"),
        "A multi-language skeleton generator for new projects.",
        ["Bash", "C++", "Python"]),

    Project(
        "Thought",
        github("thought"),
        "A compiler/tool to encourage articulated, exploratory, disciplined thinking.",
        ["C++"]),

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
    educations = _educations
    projects = _projects
    events = _events
