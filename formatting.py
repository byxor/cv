render = lambda content: NotImplementedError()
export = lambda content: NotImplementedError()


def render_latex(content):
    return "\n".join([
        "Hello, this is my file.",
        "I just rendered it.",
        ""
    ])


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)


