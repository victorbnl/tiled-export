from abc import ABC, abstractmethod

from typing import List, Tuple, Any
from pydantic import BaseModel


def get_items(obj: BaseModel) -> List[Tuple[str, str]]:
    """Returns a list of items from a pydantic class"""

    return [
        (
            k.rstrip('_'),
            v
        )
        for k, v in obj
    ]


class Encoder(ABC):

    def __init__(self, indent=2):
        """Encodes an object"""

        self.indentation = indent
        self.newline = "\n" if indent else ""

    def indent(self, string: str) -> str:
        """Indents the given string once"""

        indentation = " " * self.indentation

        return ''.join(
            f"{indentation}{line}"
            for line in string.splitlines(True)
        )

    def separator(self) -> str:
        """Returns a list/dict separator"""

        return f",{self.newline}"

    def block(self, content: str, delimiters: Tuple[str, str]) -> str:
        """Returns the given content inside a properly indented and delimited block"""

        string = delimiters[0]

        if content:
            string += self.newline
            string += self.indent(content)
            string += self.newline

        string += delimiters[1]

        return string

    @abstractmethod
    def encode(self, obj: Any):
        """Encodes an object into a string"""

        raise ValueError(f"Cannot encode type: {type(obj).__name__}")
