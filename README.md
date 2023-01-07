# Tiled exporter

A level converter for the [Tiled](https://www.mapeditor.org/) map editor

## Usage

**Install**

```
pip install git+https://github.com/victorbnl/tiled-export
tiled-export --help
```

**Without installing**

```
pip install -r requirements.txt
python3 -m tiled_export --help
```

## Roadmap

Here are the features that are known (not) to be supported:

- [x] Maps
    - [x] Parse:
        - [ ] XML encoding (deprecated)
        - [x] CSV encoding
        - [x] Base64 encoding
            - [x] Uncompressed
            - [x] gzip compressed
            - [x] zlib compressed
            - [x] Zstandard compressed
    - [x] Export:
        - [x] JSON
        - [x] CSV
        - [ ] JavaScript
        - [ ] GameMaker Studio 2
        - [ ] GameMaker room
        - [x] Lua
- [x] Tilesets
    - [x] Export:
        - [x] JSON
        - [x] Lua

Unchecked features are planned to be worked on in the future. If there's a feature that you think should be implemented which doesn't appear in this list, please create an [issue](https://github.com/victorbnl/tiled-export/issues).
