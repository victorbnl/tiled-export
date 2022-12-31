from tiled_export.export._common import tiled_to_dict


class JsonEncoder:

    def __init__(self, indent=1):
        self.indentation = " " * indent
        self.nl = "\n" if indent > 0 else ""

    def indent(self, s):
        """Adds a level of indentation to a string"""

        return ''.join(f"{self.indentation}{l}" for l in s.splitlines(True))

    def encode(self, obj):
        """Encodes a Python object to a JSON string"""

        # Dict
        if isinstance(obj, dict):

            s = "{" + self.nl

            content = ""
            for i, (k, v) in enumerate(obj.items()):
                line = f"{self.encode(k)}: {self.encode(v)}"
                if i != len(obj) - 1:
                    line += ","
                content += line + self.nl

            s += self.indent(content)
            s += "}"

            return s

        # List
        if isinstance(obj, list):

            # Matrix
            if len(obj) > 0 and all([isinstance(item, list) for item in obj]):

                s = "[" + self.nl

                content = ""
                for i, row in enumerate(obj):
                    for j, v in enumerate(row):
                        chunk = self.encode(v)
                        if i != len(obj) - 1 or j != len(row) - 1:
                            chunk += ", "
                        content += chunk
                    content = content.strip()
                    content += self.nl

                s += self.indent(content)
                s += "]"

                return s

            # Classic list
            else:

                s = "["

                if len(obj) > 0:

                    content = ""
                    for i, v in enumerate(obj):
                        suffix = f",{self.nl}" if i != len(obj) - 1 else ""
                        content += self.encode(v) + suffix

                    s += self.nl
                    s += self.indent(content)
                    s += self.nl

                s += "]"

                return s

        # Boolean
        if isinstance(obj, bool):
            return "true" if bool else "false"

        # Integer
        if isinstance(obj, int):
            return str(obj)

        # Float
        if isinstance(obj, float):
            return str(obj)

        # String
        if isinstance(obj, str):
            return f"\"{obj}\""

        raise ValueError(type(obj).__name__)


def export(obj):
    """Exports a Tiled object to JSON"""

    # Convert Tiled object to dictionary
    dict_ = tiled_to_dict(obj)

    # Encode it in json
    result = JsonEncoder(indent=2).encode(dict_)

    return result
