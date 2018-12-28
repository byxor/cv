from cv.helpers import lines, commas
from cv.structures import DateRange
import re


def render(content):
    return lines(
        "\\documentclass{article}",

        *packages(),
        *commands(),
        *settings(),

        "\\begin{document}",

        f"\\yourtitle{{{content.name}}}{{{content.email}}}{{{content.website}}}",

        "\\section{Overview}",
        *overview(content),

        "\\section{Experience}",
        *jobs(content.jobs),

        "\\section{Projects}",
        *projects(content),

        "\\section{Education}",
        *educations(content.educations),

        *footer(content),

        "\\end{document}",
    )


def packages():
    return [f"\\usepackage{p}" for p in [
        "[a4paper, left=1in, right=1in, top=15mm, bottom=6mm]{geometry}",
        "{fontawesome}",
        "{changepage}",
        "{booktabs}",
        "{dashrule}",
        "{enumitem}",
        "{hyperref}",
        "{multicol}",
        "{ragged2e}",
        "{tabularx}",
        "{titlesec}",
        "{parskip}",
        "{titling}",
        "{lipsum}",
        "{xcolor}",
    ]]


def commands():
    return [
        "\\newcommand{\\yourlight}[1]{\\textcolor{gray}{#1}}",
        "\\newcommand{\\youremail}[1]{\\href{mailto:#1}{#1}}",
        "\\newcommand{\\yoursocial}[2]{{\\Large #1}\\hspace{0.5em}\\yourlight{\\url{#2}}}"
        "\\newcommand{\\yourjustify}[1]{\makebox[\textwidth][s]{#1}}",

        "\\newcommand{\\yourtitle}[3]{",
        "  \\begin{center}",
        "    {\\huge\\bfseries #1}\\\\",
        "    \\vspace{0.5em}",
        "    \\youremail{#2}\\\\",
        "    \\url{#3}\\\\",
        "  \\end{center}",
        "}",

        "\\newcommand{\\yourfooter}[1]{",
        "  \\vfill",
        "  \\begin{center}",
        "    #1",
        "  \\end{center}",
        "}",

        "\\newcommand{\\yourmiddle}[1]{\\noindent\\parbox[c]{\\hsize}{#1}}",
    ]


def settings():
    return [
        "\\titleformat{\\section}{\\LARGE\\bfseries}{}{0em}{}[\\titlerule]",
        "\\titlespacing{\\section}{0em}{1.1em}{0.6em}",

        "\\titlespacing{\\subsection}{0em}{0.5em}{-0.2em}",

        "\\newcolumntype{b}{X}",
        "\\newcolumntype{s}{>{\hsize=.5\hsize}X}",
        "\\setlength{\\columnseprule}{0.4pt}",
        "\\setlength\\multicolsep{0pt}",

        "\\linespread{0.9}",
        "\\setlist{nosep}",
        "\\pagenumbering{gobble}",

        "\\hypersetup{colorlinks, linkcolor={red!50!black}, citecolor={blue!50!black}, urlcolor={blue!70!black}}",
    ]


def packages():
    return [f"\\usepackage{p}" for p in [
        "[a4paper, left=1in, right=1in, top=15mm, bottom=6mm]{geometry}",
        "{fontawesome}",
        "{changepage}",
        "{booktabs}",
        "{dashrule}",
        "{enumitem}",
        "{hyperref}",
        "{multicol}",
        "{ragged2e}",
        "{tabularx}",
        "{titlesec}",
        "{parskip}",
        "{titling}",
        "{lipsum}",
        "{xcolor}",
    ]]


def commands():
    return [
        "\\newcommand{\\yourlight}[1]{\\textcolor{gray}{#1}}",
        "\\newcommand{\\youremail}[1]{\\href{mailto:#1}{#1}}",
        "\\newcommand{\\yoursocial}[2]{{\\Large #1}\\hspace{0.5em}\\yourlight{\\url{#2}}}"
        "\\newcommand{\\yourjustify}[1]{\makebox[\textwidth][s]{#1}}",

        "\\newcommand{\\yourtitle}[3]{",
        "  \\begin{center}",
        "    {\\huge\\bfseries #1}\\\\",
        "    \\vspace{.5em}",
        "    \\youremail{#2}\\\\",
        "    \\url{#3}\\\\",
        "    \\vspace{.7em}",
        "  \\end{center}",
        "}",

        "\\newcommand{\\yourfooter}[1]{",
        "  \\vspace*{\\fill}",
        "  \\begin{center}",
        "    #1",
        "  \\end{center}",
        "}",

        "\\newcommand{\\yourmiddle}[1]{\\noindent\\parbox[c]{\\hsize}{#1}}",
    ]


def settings():
    return [
        "\\titleformat{\\section}{\\LARGE\\bfseries}{}{0em}{}[\\titlerule]",
        "\\titlespacing{\\section}{0em}{1.1em}{0.6em}",

        "\\titlespacing{\\subsection}{0em}{0.5em}{-0.2em}",

        "\\newcolumntype{b}{X}",
        "\\newcolumntype{s}{>{\hsize=.5\hsize}X}",

        "\\linespread{0.9}",
        "\\setlist{nosep}",
        "\\pagenumbering{gobble}",

        "\\hypersetup{colorlinks, linkcolor={red!50!black}, citecolor={blue!50!black}, urlcolor={blue!70!black}}",
    ]


def overview(content):
    space = "\\vspace{0.75em}"
    return [
        "\\begin{tabularx}{\\textwidth}{ll}",
        space,

        _row("\\textbf{Skills}", commas(*content.skills)),
        space,

        _row("\\textbf{Primary Languages}",
             commas(*[language.name for language in content.primary_languages])),

        _row("\\textbf{Extra Languages}",
             commas(*[language.name for language in content.extra_languages])),

        "\\end{tabularx}",
    ]


def jobs(jobs):
    def job(j):
        return lines(
            f"\\subsection{{{j.company} ({j.location}) - {j.role}}}",
            f"{_dates(j.dates)}",
            "",
            f"{_escape(j.description)}",
            "",
            technologies(j.technologies),
            "\\vspace{0.5em}",
        )

    return [job(j) for j in jobs]


def educations(educations):
    ed = educations[0]
    return [
        f"\\subsection{{{ed.institution}, {ed.location}}}",
        f"{_dates(ed.dates)}",
        "",
        f"\\textbf{{{ed.type}}} {_escape(ed.name)}\\\\"
    ]


def footer(content):
    return [
        "\\yourfooter{",
        "\\vspace{1em}",
        _wide_strip([
            f"\\yoursocial{{\\faGithub}}{{{content.github}}}",
            f"\\yoursocial{{\\faStackOverflow}}{{{content.stack_overflow}}}",
            f"\\yoursocial{{\\faLaptop}}{{{content.website}}}",
        ]),
        "",
        "This CV was rendered with \\textbf{Python} {\\&} \\textbf{{\\LaTeX}} (\\url{www.github.com/byxor/cv}).\\\\",
        "}",
    ]


def projects(content):
    projects = content.projects

    def project(project):
        if project.link:
            url = f"(\\href{{{project.link}}}{{github}})"
        else:
            url = "(proprietary, no source)"

        s = ""
        s = "\\parbox{\\linewidth}{"
        s += f"\\textbf{{{project.name}}} - "
        s += _escape(project.description)
        s += f" {url}\\\\"
        s += "\n"
        s += technologies(project.technologies)
        s += "}"
        return s

    chosen_projects = projects[:6]

    between_projects = "\\vspace{1em}\\\\"

    return [
        "\\begin{multicols}{2}",
        between_projects.join([project(p) for p in chosen_projects]),
        "\\end{multicols}",

        "\\begin{center}",
        f" See more projects at \\url{{{content.website}/projects}}",
        "\\end{center}",
    ]


def technologies(technologies):
    return f"\\textbf{{Technologies}}: {_escape(commas(*technologies))}"


#########################


def _escape(text):
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile('|'.join(re.escape(key) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)


def _wide_strip(contents):
    return lines(
        f"\\begin{{tabularx}}{{\\linewidth}}{{*{len(contents)}{{>{{\\Centering}}X}}}}",
        _row(*contents),
        "\\end{tabularx}",
    )


def _row(*things):
    return " & ".join(things) + "\\\\"


def _dates(dates):
    return f"\\textit{{{dates}}}"
