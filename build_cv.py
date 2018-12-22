from functools import partial

from content import data
from formatting import render_latex, export_file


def build_cv(data, renderer, exporter):
    exporter(renderer(data))


if __name__ == "__main__":
    renderer = render_latex
    exporter = partial(export_file, "cv.tex")
    build_cv(data, renderer, exporter)
