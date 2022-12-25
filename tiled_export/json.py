class Encoder:

    def __init__(self, indent=1):
        self.indentation = " " * indent
        self.nl = "\n" if indent > 0 else ""

    def indent(self, s):
        return ''.join(f"{self.indentation}{l}" for l in s.splitlines(True))

    def encode(self, obj):

        # Dict
        if isinstance(obj, dict):
            s = "{" + self.nl

            content = ""

            for i, (k, v) in enumerate(obj.items()):

                if v != None:

                    k = k.rstrip("_")

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
            if all([isinstance(item, list) for item in obj]):

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

                s = "[" + self.nl

                content = ""
                for i, v in enumerate(obj):
                    line = self.encode(v)
                    if i != len(obj) - 1:
                        line += ","
                    content += line + self.nl

                s += self.indent(content)
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

        raise ValueError
