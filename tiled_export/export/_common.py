from abc import ABC, abstractmethod
from dataclasses import fields


def get_items(obj):
    """Returns a list of items from a dataclass"""

    return [
        (
            field.name.rstrip("_"),
            getattr(obj, field.name)
        )
        for field in fields(obj)
    ]


class Encoder(ABC):

    def __init__(self, indent=2):
        """Encodes an object"""

        self.indentation = indent
        self.newline = "\n" if indent else ""

    def indent(self, string):
        """Indents the given string once"""

        indentation = " " * self.indentation

        return ''.join(
            f"{indentation}{line}"
            for line in string.splitlines(True)
        )

    def separator(self):
        """Returns a list/dict separator"""

        return f",{self.newline}"

    def block(self, content, delimiters):
        """Returns the given content inside a properly indented and delimited block"""

        string = delimiters[0]

        if content:
            string += self.newline
            string += self.indent(content)
            string += self.newline

        string += delimiters[1]

        return string

    @abstractmethod
    def encode(self, obj):
        """Encodes an object into a string"""

        raise ValueError(f"Cannot encode type: {type(obj).__name__}")
