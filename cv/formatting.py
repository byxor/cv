render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
        "\\documentclass{article}",
        "\\begin{document}",

        "\\huge{Skills}",
        "\\begin{itemize}",
        *[f"  \\item {skill}" for skill in content["skills"]],
        "\\end{itemize}",

        "Rendered with Python \\& \\LaTeX!",

        "\\end{document}",
        "",
    ])


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)

