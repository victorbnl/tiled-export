import pytest
from pytest import mark

import os
import glob
import re
import filecmp

from tiled_export.convert import convert


# Constants
INPUT_FOLDER = "inputs"
OUTPUT_FOLDER = "outputs"
EXPECTED_OUTPUTS_FOLDER = "expected_outputs"


# Change to tests directory
os.chdir(os.path.dirname(__file__))

# Create output directory
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)


@mark.parametrize("format_", ["csv", "json", "lua"])
@mark.parametrize("filename", [os.path.basename(path) for path in glob.glob(f"{INPUT_FOLDER}/*") if re.match(r".*\.[tmx|tsx]", path)])
def test_all(filename, format_):

    # Split base name and extension
    name, ext = os.path.splitext(filename)

    # Cannot export tileset as CSV
    if format_ == "csv" and ext == ".tsx":
        pytest.skip("Cannot export tileset as CSV")

    # Convert the file
    convert(f"{INPUT_FOLDER}/{filename}", format_, f"{OUTPUT_FOLDER}/{name}.{format_}")

    # Expected output not yet written
    if not os.path.exists(f"{EXPECTED_OUTPUTS_FOLDER}/{name}.{format_}"):
        pytest.xfail(f"Expected output not yet written for file: {name}.{format_}")

    # Check if output file is equal to expected output
    assert filecmp.cmp(f"{OUTPUT_FOLDER}/{name}.{format_}", f"{EXPECTED_OUTPUTS_FOLDER}/{name}.{format_}")
