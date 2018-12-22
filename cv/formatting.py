render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
        "\\documentclass{article}",
        "\\begin{document}",
        "\\end{document}",
        "",
    ])


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)

