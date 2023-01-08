import io


class ResultFile:

    def __init__(self, path):
        """Represents a file to be written"""

        self.path = path
        self.io = io.StringIO()

    def write(self, content: str) -> None:
        """Writes content into result file"""

        self.io.write(content)

    def get_content(self) -> str:
        """Returns file content"""

        return self.io.getvalue()
