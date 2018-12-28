from functools import partial

from cv.content import Data
from cv.formatting import export_file
from cv.renderers.latex import render


def build_cv(data, renderer, exporter):
    rendered = renderer(data)
    print(rendered)
    exporter(rendered)


if __name__ == "__main__":
    exporter = partial(export_file, "cv.tex")
    build_cv(Data, render, exporter)
