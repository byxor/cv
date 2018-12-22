render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
        "\\documentclass{article}",

        "\\usepackage{hyperref}",

        "\\author{Brandon Ibbotson}",
        "\\title{My Super Cool CV}",

        "\\begin{document}",

        "\\maketitle",

        "\\section{Skills}",
        "\\begin{itemize}",
        *[f" \\item {skill}" for skill in content["skills"]],
        "\\end{itemize}",

        "\\section{Experience}",

        "\\section{Outro}",
        "This CV was rendered with \\textbf{Python} {\\&} \\textbf{{\\LaTeX}}.",
        "",
        "Source code at: \\url{www.github.com/byxor/cv}",

        "\\end{document}",
    ])


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)

