# Tiled exporter

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/victorbnl/tiled-export/test.yml?label=tests)

Tiled exporter is a project exporter for the
[Tiled](https://www.mapeditor.org/) map editor

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
