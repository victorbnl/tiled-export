import pytest
import os

from tiled_export.convert import convert


@pytest.mark.parametrize("limit", ["finite", "infinite"])
@pytest.mark.parametrize("encoding", ["csv", "base64"])
@pytest.mark.parametrize("compression", ["uncompressed", "gzip", "zlib", "zstd"])
@pytest.mark.parametrize("format_", ["csv", "json", "lua"])
def test_map(limit, encoding, compression, format_):

    if encoding == "csv" and compression != "uncompressed":
        return

    filename = f"level_{limit}_{encoding}_{compression}"

    with open(f"test_out/{filename}.{format_}", "w") as outfile:
        outfile.write(convert(f"tests/files/{filename}.tmx", format_))
