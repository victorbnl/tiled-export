# Tiled exporter

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/victorbnl/tiled-export/test.yml?label=tests)

Tiled exporter is a project exporter for the
[Tiled](https://www.mapeditor.org/) map editor

## Discontinued

I originally started this project as an alternative to running the full Tiled
software to build maps in automated workflows (like CI/CD). However, it
requires some work to support all features and keep it up-to-date with Tiled’s
format. Plus, it only brings a bit of performance which is near negligible on
modern hardware. Therefore, I do not find it worth keeping maintaining it.

If you need to build maps in headless environments, you can use Xvfb (as per
https://doc.mapeditor.org/en/stable/manual/export/):

```
xvfb-run tiled --export-map ...
```

## Setup

### Install

```
pip install git+https://github.com/victorbnl/tiled-export
tiled-export --help
```

### Without installing

```
pip install -r requirements.txt
python3 -m tiled_export --help
```

## Usage

### As a command

```
tiled-export level.tmx output.csv
```

### As a module

```py
import tiled_export

files = tiled_export.export('level.tmx', 'csv', 'output.csv')

for file_ in files:
    with open(file_.path, 'w') as outfile:
        outfile.write(file_.get_content())
```
