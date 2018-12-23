render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
        "\\documentclass{article}",

        "\\usepackage[a4paper, left=1in, right=1in, top=15mm, bottom=6mm]{geometry}",
        "\\usepackage{hyperref}",
        "\\usepackage{titlesec}",
        "\\usepackage{titling}",
        "\\usepackage{fontawesome}",
        "\\usepackage{titling}",
        "\\usepackage{xcolor}",
        "\\usepackage{tabularx, ragged2e}",
        "\\usepackage{booktabs}",

        "\\titleformat{\section}",
        "{\\huge\\bfseries}",
        "{}",
        "{0em}",
        "{}[\\titlerule]",

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

        "\\pagenumbering{gobble}",

        #########################

        "\\begin{document}",

        "\\maketitle",

        "\\section{Skills}",
        "\\begin{itemize}",
        *[f"\\item {skill}" for skill in content.skills],
        "\\end{itemize}",

        "\\section{Languages}",

        "\\section{Experience}",

        "\\section{Projects}",


        "\\yourfooter{",
        "  \\begin{tabularx}{\\textwidth}{*3{>{\\Centering}X}}",
        f"   \\yoursocial{{\\faGithub}}{{{content.github}}} &",
        f"   \\yoursocial{{\\faStackOverflow}}{{{content.stack_overflow}}} &",
        f"   \\yoursocial{{\\faKeyboardO}}{{{content.website}}}\\\\",
        "  \\end{tabularx}",
        "  ",
        "  \\vspace{1em}",
        "  ",
        "  This CV was rendered with \\textbf{Python} {\\&} \\textbf{{\\LaTeX}}.\\\\",
        "  Source code: \\url{www.github.com/byxor/cv}",
        "}",

        "\\end{document}",
    ])


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)
