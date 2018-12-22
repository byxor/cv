render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
        "\\documentclass{article}",

        "\\usepackage{hyperref}",
        "\\usepackage{titlesec}",
        "\\usepackage[margin=1in]{geometry}",

        "\\titleformat{\section}",
        "{\\huge\\bfseries}",
        "{}",
        "{0em}",
        "{}[\\titlerule]",

        "\\pagenumbering{gobble}",

        #########################

        "\\begin{document}",

        "\\author{Brandon Ibbotson}",
        "\\title{My Super Cool CV}",
        "\\maketitle",

        "\\section{Skills}",
        "\\begin{itemize}",
        *[f" \\item {skill}" for skill in content["skills"]],
        "\\end{itemize}",

        "\\section{Experience}",

        "\\vspace*{\\fill}",
        "\\begin{center}",
        "This CV was rendered with \\textbf{Python} {\\&} \\textbf{{\\LaTeX}}.",
        "",
        "Source code at: \\url{www.github.com/byxor/cv}",
        "\\end{center}",

        "\\end{document}",
    ])


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)
