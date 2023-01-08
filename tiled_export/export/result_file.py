import io


class ResultFile:

    def __init__(self, path):
        self.path = path
        self.io = io.StringIO()

    def write(self, content: str) -> None:
        self.io.write(content)

    def get_content(self) -> str:
        return self.io.getvalue()
