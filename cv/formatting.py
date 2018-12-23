import re


render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return _lines(
        "\\documentclass{article}",

        # Packages

        "\\usepackage[a4paper, left=1in, right=1in, top=15mm, bottom=6mm]{geometry}",
        "\\usepackage{fontawesome}",
        "\\usepackage{booktabs}",
        "\\usepackage{enumitem}",
        "\\usepackage{hyperref}",
        "\\usepackage{ragged2e}",
        "\\usepackage{tabularx}",
        "\\usepackage{titlesec}",
        "\\usepackage{titling}",
        "\\usepackage{lipsum}",
        "\\usepackage{xcolor}",

        # Custom Commands

        "\\newcommand{\\light}[1]{\\textcolor{gray}{#1}}",
        "\\newcommand{\\youremail}[1]{\\href{mailto:#1}{#1}}",
        "\\newcommand{\\yoursocial}[2]{{\\Large #1} \\light{\\url{#2}}}"

        "\\newcommand{\\yourfooter}[1]{",
        "  \\vspace*{\\fill}",
        "  \\begin{center}",
        "    #1",
        "  \\end{center}",
        "}",

        "\\renewcommand{\\maketitle}{",
        "  \\begin{center}",
        f"   {{ \\huge \\bfseries {content.name} }}\\\\",
        "    \\vspace{.5em}",
        f"   \\youremail{{ {content.email} }}\\\\",
        f"   \\url{{{content.website}}}\\\\",
        "    \\vspace{.7em}",
        "  \\end{center}",
        "}",

        # Formatting

        "\\titleformat{\\section}",
        "{\\huge\\bfseries}",
        "{}",
        "{0em}",
        "{}[\\titlerule]",

        "\\setlist{nosep}",

        # Misc Settings

        "\\pagenumbering{gobble}",

        # Document

        "\\begin{document}",

        "\\maketitle",

        "\\section{Overview}",

        "\\subsection{Skills}",

        "\\begin{itemize}",
        *[f"\\item \\textbf{{{skill}}}" for skill in content.skills],
        "\\end{itemize}",

        "\\subsection{Primary Languages}",
        "\\begin{itemize}",
        *[f"\\item \\textbf{{{language.name}}}: {language.usage}" for language in content.primary_languages],
        "\\end{itemize}",

        "\\subsection{Extra Languages}",
        ', '.join([language.name for language in content.extra_languages]),

        "\\section{Experience}",
        _render_latex_jobs(content.jobs),

        "\\section{Projects}",
        "\\lipsum[1]",
        "",
        "\\begin{center}",
        f" See more projects at \\url{{{content.website}/projects}}",
        "\\end{center}",

        "\\yourfooter{",
        _render_latex_strip([
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


def _render_latex_strip(contents):
    innards = " & ".join(contents) + "\\\\"
    return _lines(
        f"\\begin{{tabularx}}{{\\textwidth}}{{*{len(contents)}{{>{{\\Centering}}X}}}}",
        innards,
        "\\end{tabularx}",
    )


def _render_latex_jobs(jobs):
    return "\\\\".join([_render_latex_job(job) for job in jobs])


def _render_latex_job(job):
    return _lines(
        f"\\subsection{{{job.company} - {job.location} - {job.role}}}",
        f"{_escape_latex(job.description)}"
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


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)
