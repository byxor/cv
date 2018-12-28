import re
import functools


export = lambda content: NotImplementedError()


def export_file(path, content):
    with open(path, "w") as f:
        f.write(content)
