from functools import partial

from cv.content import Data
from cv.exporters.file import export
from cv.renderers.latex import render


def build_cv(data, renderer, exporter):
    rendered = renderer(data)
    print(rendered)
    exporter(rendered)


if __name__ == "__main__":
    build_cv(Data, render, partial(export, "cv.tex"))
