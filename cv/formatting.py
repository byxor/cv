render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
        "\\documentclass{article}",

        "\\usepackage{hyperref}",
        "\\usepackage{titlesec}",
        "\\usepackage{titling}",
        "\\usepackage[a4paper, left=1in, right=1in, top=15mm, bottom=6mm]{geometry}",

        # "\\usepackage{fullpage}",
        # "\\usepackage[T1]{fontenc}",
        # "\\usepackage[utf8]{inputenc}",


        "\\titleformat{\section}",
        "{\\huge\\bfseries}",
        "{}",
        "{0em}",
        "{}[\\titlerule]",

        "\\newcommand{\\youremail}[1]{ \\href{#1}{#1} }",

        "\\renewcommand{\\maketitle}{",

        "  \\vspace{.25em}",

        "  \\begin{center}",
        f"   {{ \\huge \\bfseries {content.name} }}",
        "",
        f"   \\youremail{{ {content.email} }}",
        "",
        f"   \\url{{ {content.website} }}",
        "  \\end{center}",

        "  \\vspace{1em}",
        "}",

        "\\pagenumbering{gobble}",

        #########################

        "\\begin{document}",

        "\\maketitle",

        "\\section{Skills}",
        "\\begin{itemize}",
        *[f" \\item {skill}" for skill in content.skills],
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
