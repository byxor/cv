from collections import namedtuple

Date = namedtuple("Date", "month year")
Language = namedtuple("Language", "name usage")
ExtraLanguage = namedtuple("ExtraLanguage", "name")
Event = namedtuple("Event", "name year description")
Job = namedtuple("Job", "company location role start_date end_date technologies description")
Project = namedtuple("Project", "name link description")

github = lambda project: f"http://www.github.com/byxor/{project}"

##############################################################

SKILLS = [
    "Test Driven Development",
    "Agile Development",
]

PRIMARY_LANGUAGES = [
    Language("Java",             "First taste of OOP, used frequently in many early projects."),
    Language("Python 3",         "Essential language for degree. Used in year-long team project and many personal projects."),
    Language("C++",              "Used to program ASICs in Arista switches and solve competitive programming problems."),
    Language("Kotlin",           "Used in production environment to write HTTP backend."),
    Language("JavaScript (ES6)", "Used for web development with Angular. Familiar with ES6 features."),
    Language("C",                "Taught me about memory management, the stack, the heap, pointers."),
    Language("Go",               "Introduced me to goroutines and channels as a concurrency model."),
]

EXTRA_LANGUAGES = [
    ExtraLanguage("Go"),
    ExtraLanguage("Ruby"),
    ExtraLanguage("x86 Assembly (MASM)"),
    ExtraLanguage("x64 Assembly (NASM)"),
    ExtraLanguage("Prolog"),
    ExtraLanguage("Clojure"),
    ExtraLanguage("UnityScript"),
    ExtraLanguage("LIMP"),
]

JOBS = [
    Job("Instil Software",
        "Belfast",
        "Software Engineering Intern",
        Date("July", 2016),
        Date("September", 2016),
        ["Kotlin", "AngularJS", "DropWizard", "PostgreSQL", "Swagger"],
        "Full Stack Developer for a Time Tracking Tool. Built REST API & Email Service with Kotlin. Increased test coverage by ~15% in first month. Maintained AngularJS frontend. Received first-class training on Test-Driven Development and Refactoring."),

    Job("Arista Networks",
        "Dublin",
        "Software Engineering Intern",
        Date("June", 2017),
        "Present",
        ["TACC", "C++", "C", "Command-line"],
        "Wrote & tested C++ deployed on high-performance switches around the world. Worked exclusively in command-line environments."),
]

PROJECTS = [
    Project("LIMP Programming Language",
            github("limp"),
            "Functional Programming Language Interpreter with 98% Test Coverage. Supports anonymous functions, collections, strings, recursion, immutability, scoped constants. Has a small standard library. Soon to support objects and modules. Written in Python 3.6."),

    Project("Website at byxor.xyz",
            github("website"),
            "A website built using Angular 5. Can be seen at http://www.byxor.xyz"),
    
    Project("Try LIMP - WebApp",
            None,
            "A full-stack application to execute LIMP code in the browser. Web client written with ES6, JQuery and Bootstrap 3. Backend is a REST API written in Python using Flask, running on DigitalOcean VPS. Try it out at http://byxor.xyz/try-limp."),
    
    Project("Passflip",
            github("passflip"),
            "A lightweight SHA224-based password manager."),

    Project("Slimput",
            github("slimput"),
            "A faster way of scanning standard input for Java."),
    
    Project("Kapoki",
            github("kapoki"),
            "A multi-language skeleton generator for new projects."),

    Project("Thought",
            github("thought"),
            "A compiler/tool to encourage articulated, exploratory, disciplined thinking."),

    Project("DecayQueueJs",
            github("DecayQueueJs"),
            "A JavaScript Data Structure that removes old elements automatically."),
]

EVENTS = [
    Hackathon("YRS Festival of Code", 2014, "Week long. Competed in Plymouth, England as First Northern Irish team to compete. Awarded semi-finalists in 'Should Exist' category."),
    Hackathon("YRS Festival of Code", 2015, ""),
    Hackathon("Global Game Jam",      2015, ""),
    Hackathon("AIB Data Hack",        2016, ""),
    Hackathon("Google Hash Code",     2017, ""),
    Hackathon("Arista Hack-a-Switch", 2017, ""),
]
