import re


def get_file_ext(filename):
    """Get file extension from file name"""

    return filename.split(".")[-1]


def hex_to_rgb(color):
    """Convert hexadecimal color to RGB"""

    color = color.lstrip("#")

    r_hex = color[0:2]
    g_hex = color[2:4]
    b_hex = color[4:6]

    r = int(r_hex, 16)
    g = int(g_hex, 16)
    b = int(b_hex, 16)

    return (r, g, b)
