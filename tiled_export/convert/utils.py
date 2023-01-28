"""
Some common utilities that can be useful for various plugins
"""


from abc import ABC, abstractmethod

from typing import List, Tuple, Any
from pydantic import BaseModel


def get_items(obj: BaseModel) -> List[Tuple[str, str]]:
    """
    Get fields of pydantic objects

    Args:
        obj (pydantic object): The pydantic object to get fields from

    Returns:
        A list of tuples (name, value) of object fields
    """

    return [
        (
            k.rstrip('_'),
            v
        )
        for k, v in obj
    ]


class Encoder(ABC):

    def __init__(self, indent=2):
        """
        Encodes an object
        """

        self.indentation = indent
        self.newline = "\n" if indent else ""

    def indent(self, string: str) -> str:
        """
        Indents a string once

        Args:
            string (string): String to be indented

        Returns:
            The indented string
        """

        indentation = " " * self.indentation

        return ''.join(
            f"{indentation}{line}"
            for line in string.splitlines(True)
        )

    def separator(self) -> str:
        """
        Get a separator for list and dict values

        Returns:
            The separator
        """

        return f",{self.newline}"

    def block(self, content: str, delimiters: Tuple[str, str]) -> str:
        """
        Get the given content inside a properly indented and delimited block

        Returns:
            content put in a block
        """

        string = delimiters[0]

        if content:
            string += self.newline
            string += self.indent(content)
            string += self.newline

        string += delimiters[1]

        return string

    @abstractmethod
    def encode(self, obj: Any) -> str:
        """
        Encodes an object into a string

        Args:
            obj (object): Object to encode

        Returns:
            Encoded object
        """

        raise ValueError(f"Cannot encode type: {type(obj).__name__}")
