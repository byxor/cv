import re
import functools


render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return _lines(
        "\\documentclass{article}",

        *_latex_packages(),

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

        ###

        "\\titleformat{\\section}{\\huge\\bfseries}{}{0em}{}[\\titlerule]",
        "\\titlespacing{\\section}{0em}{1em}{1em}",

        # "\\titleformat{\\subsection}{\\bfseries}{}{1em}{}[]",
        "\\titlespacing{\\subsection}{0pt}{0.5em}{-0.2em}",

        "\\newcolumntype{b}{X}",
        "\\newcolumntype{s}{>{\hsize=.5\hsize}X}",

        "\\linespread{0.9}",
        "\\setlist{nosep}",
        "\\pagenumbering{gobble}",

        "\\hypersetup{colorlinks, linkcolor={red!50!black}, citecolor={blue!50!black}, urlcolor={blue!70!black}}",

        # Document ####################################################################

        "\\begin{document}",

        f"\\yourtitle{{{content.name}}}{{{content.email}}}{{{content.website}}}",

        "\\section{Overview}",

        "\\subsection{Skills}",
        _escape_latex(_commas(*content.skills)),

        "\\subsection{Primary Languages}",
        _escape_latex(_commas(*[language.name for language in content.primary_languages])),

        "\\subsection{Extra Languages}",
        _escape_latex(_commas(*[language.name for language in content.extra_languages])),

        "\\section{Experience}",
        _render_latex_jobs(content.jobs),

        "\\section{Projects}",

        "\\begin{multicols}{2}",
        _render_latex_projects(content.projects),
        "\\end{multicols}",

        "\\begin{center}",
        f" See more projects at \\url{{{content.website}/projects}}",
        "\\end{center}",

        "\\section{Education}",
        

        "\\yourfooter{",
        _render_wide_latex_strip([
            f"\\yoursocial{{\\faGithub}}{{{content.github}}}",
            f"\\yoursocial{{\\faStackOverflow}}{{{content.stack_overflow}}}",
            f"\\yoursocial{{\\faLaptop}}{{{content.website}}}",
        ]),
        "",
        "  \\vspace{1em}",
        "  This CV was rendered with \\textbf{Python} {\\&} \\textbf{{\\LaTeX}} (\\url{www.github.com/byxor/cv}).\\\\",
        "}",

        "\\end{document}",
    )


def _latex_packages():
    return [f"\\usepackage{p}" for p in [
        "[a4paper, left=1in, right=1in, top=15mm, bottom=6mm]{geometry}",
        "{fontawesome}",
        "{booktabs}",
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


def _render_wide_latex_strip(contents):
    innards = " & ".join(contents) + "\\\\"
    return _lines(
        f"\\begin{{tabularx}}{{\\textwidth}}{{*{len(contents)}{{>{{\\Centering}}X}}}}",
        innards,
        "\\end{tabularx}",
    )


def _render_thin_latex_strip(contents):
    innards = " & ".join(contents) + "\\\\"
    return _lines(
        "\\begin{center}",
        f" \\begin{{tabular}}{{{'c' * len(contents)}}}",
        innards,
        "  \\end{tabular}",
        "\\end{center}",
    )


def _render_latex_jobs(jobs):
    def _render_latex_job(job):
        return _lines(
            f"\\subsection{{{job.company} ({job.location}) - {job.role}}}",
            f"{_render_latex_date(job.start_date)} - {_render_latex_date(job.end_date)}",
            "",
            f"{_escape_latex(job.description)}",
            "",
            f"\\textbf{{Technologies: }}{_commas(*job.technologies)}",
            "\\vspace{0.5em}",
        )

    def _render_latex_date(date):
        if type(date) == str:
            return date
        return f"\\textbf{{{date.month} {date.year}}}"

    return "".join([_render_latex_job(job) for job in jobs])


def _render_latex_projects(projects):
    def _render_latex_project(project):
        if project.link:
            url = f"(\\href{{{project.link}}}{{github}})"
        else:
            url = ""
        return f"{{\\textbf{{{project.name}}} {url}\\hspace{{1.5em}}-\\hspace{{1.5em}}{_escape_latex(project.description)}}}\\\\"

    return "\\\\".join([_render_latex_project(project) for project in projects])



def _escape_latex(text):
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


def _lines(*lines):
    return "\n".join(lines)


def _commas(*things):
    return ", ".join(things)


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)
