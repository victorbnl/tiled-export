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

- **Maps**
    - **Features**
        - [x] Infinite
        - [x] Tile layers
        - [ ] Object layers
        - [ ] Image layers
        - [ ] Group layers
    - **Encodings**
        - [ ] XML (deprecated)
        - [x] CSV
        - [x] Base64
            - [x] Uncompressed
            - [x] gzip
            - [x] zlib
            - [x] Zstandard
    - **Export formats**
        - [x] CSV
        - [x] JSON
        - [x] Lua
        - [ ] JavaScript
        - [ ] GameMaker Studio 2
        - [ ] GameMaker Room
- **Tilesets**
    - **Features**
        - [ ] Wangsets
    - **Export formats**
        - [x] JSON
        - [x] Lua

Unchecked features are planned to be worked on in the future. If there's a feature that you think should be implemented which doesn't appear in this list, please create an [issue](https://github.com/victorbnl/tiled-export/issues).
