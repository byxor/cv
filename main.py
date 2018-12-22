from functools import partial

from cv.content import data
from cv.formatting import render_latex, export_file


def build_cv(data, renderer, exporter):
    rendered = renderer(data)
    print(rendered)
    exporter(rendered)


if __name__ == "__main__":
    renderer = render_latex
    exporter = partial(export_file, "cv.tex")
    build_cv(data, renderer, exporter)
