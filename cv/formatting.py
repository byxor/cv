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
        "\\newcommand{\\yoursocial}[2]{{\\Large #1}\\yourlight{\\url{#2}}}"
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

        ###

        "\\titleformat{\\section}{\\huge\\bfseries}{}{0em}{}[\\titlerule]",
        # "\\titleformat{\\subsection}[runin]{\\bfseries}{}{5em}{}[:]",
        "\\titlespacing{\\subsection}{0pt}{1ex}{5ex}",

        "\\newcolumntype{b}{X}",
        "\\newcolumntype{s}{>{\hsize=.5\hsize}X}",

        "\\linespread{0.9}",
        "\\setlist{nosep}",
        "\\pagenumbering{gobble}",

        # Document ####################################################################

        "\\begin{document}",

        f"\\yourtitle{{{content.name}}}{{{content.email}}}{{{content.website}}}",

        "\\section{Overview}",

        "\\begin{tabularx}{\\textwidth}{sb}",

        "\\textbf{Skills} &",
        _escape_latex(_commas(*content.skills)),
        "\\\\",

        "\\textbf{Primary Languages} &",
        _escape_latex(_commas(*[language.name for language in content.primary_languages])),
        "\\\\",

        "\\textbf{Extra Languages} &",
        _escape_latex(_commas(*[language.name for language in content.extra_languages])),
        "\\\\",

        "\\end{tabularx}",

        "\\section{Experience}",
        _render_latex_jobs(content.jobs),

        "\\section{Projects}",
        "\\begin{center}",
        f" See more projects at \\url{{{content.website}/projects}}",
        "\\end{center}",

        "\\yourfooter{",
        _render_wide_latex_strip([
            f"\\yoursocial{{\\faGithub}}{{{content.github}}}",
            f"\\yoursocial{{\\faStackOverflow}}{{{content.stack_overflow}}}",
            f"\\yoursocial{{\\faLaptop}}{{{content.website}}}",
        ]),
        "  ",
        "  \\vspace{1em}",
        "  ",
        "  This CV was rendered with \\textbf{Python} {\\&} \\textbf{{\\LaTeX}}.\\\\",
        "  Source code: \\url{www.github.com/byxor/cv}",
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
        "{ragged2e}",
        "{tabularx}",
        "{titlesec}",
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
    return "".join([_render_latex_job(job) for job in jobs])


def _render_latex_job(job):
    return _lines(
        f"\\subsection{{{job.company} ({job.location}) - {job.role}}}",
        f"{_escape_latex(job.description)}\\\\",
        _render_thin_latex_strip(job.technologies),
    )


def _escape_latex(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
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
