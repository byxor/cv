render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
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

        "\\section{Skills}",
        "\\begin{itemize}",
        *[f"\\item {skill}" for skill in content.skills],
        "\\end{itemize}",

        "\\section{Languages}",

        "\\subsection{Primary Languages}",
        "\\begin{itemize}",
        *[f"\\item \\textbf{{{language.name}}}: {language.usage}" for language in content.primary_languages],
        "\\end{itemize}",

        "\\subsection{Extra Languages}",
        ', '.join([language.name for language in content.extra_languages]),

        "\\section{Experience}",
        "\\lipsum[1]",

        "\\section{Projects}",
        "\\lipsum[1]",

        "\\yourfooter{",
        _create_latex_strip([
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
    ])


def _create_latex_strip(contents):
    innards = " & ".join(contents) + "\\\\"
    return "\n".join([
        f"\\begin{{tabularx}}{{\\textwidth}}{{*{len(contents)}{{>{{\\Centering}}X}}}}",
        innards,
        "\\end{tabularx}"
    ])




def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)
