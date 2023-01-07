import pytest
from pytest import mark

import os
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
@mark.parametrize("filename", [filename for filename in os.listdir(INPUT_FOLDER) if re.match(r".*\.[tmx|tsx]", filename)])
def test_all(filename, format_):

    # Split base name and extension
    name, ext = os.path.splitext(filename)

    # Cannot export tileset as CSV
    if format_ == "csv" and ext == ".tsx":
        pytest.skip("Cannot export tileset as CSV")

    # Directories
    output_folder = os.path.join(OUTPUT_FOLDER, f"{filename}-{format_}")
    expected_output_folder = EXPECTED_OUTPUTS_FOLDER
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # File names
    input_file = os.path.join(INPUT_FOLDER, filename)
    output_file = os.path.join(output_folder, f"{name}.{format_}")

    # Convert the file
    convert(input_file, format_, output_file)

    # Compare each file
    for output in os.listdir(output_folder):

        # File names
        output_file = os.path.join(output_folder, output)
        expected_output_file = os.path.join(expected_output_folder, output)

        # Expected output not yet written
        if not os.path.exists(f"{expected_output_folder}/{output}"):
            pytest.xfail(f"Expected output not yet written for file: {output}")

        # Check if output file is equal to expected output
        assert filecmp.cmp(output_file, expected_output_file)
