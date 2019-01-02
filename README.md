# cv

Tools I use to generate and maintain my CV.

## Toolchain Summary

Python -> LaTeX -> PDF

* My [CV content](https://github.com/byxor/cv/blob/master/cv/content.py) is written in Python.
* It gets [formatted](https://github.com/byxor/cv/blob/master/cv/renderers/latex.py) into a [LaTeX document](https://github.com/byxor/cv/blob/master/cv.tex).
* Then it gets converted into a [PDF document](https://github.com/byxor/cv/blob/master/cv.pdf).

## Build Instructions

Requires: [Python3.6](https://www.python.org/downloads/release/python-360/), [live-server](https://github.com/tapio/live-server)

```bash
virtualenv venv -p python3.6
source venv/bin/activate
```

### Build Once

```bash
./build_cv.sh
```

### Rebuild Automatically

```bash
./auto_build.sh
```
