import dataclasses
from dataclasses import dataclass, fields
from pydoc import locate


@dataclass
class Base():

    def __post_init__(self):

        def cast(value, type):
            if type == bool:
                return False if value == "0" else True
            return locate(type.__name__)(value)

        # Cast values to right types
        for field in fields(self):
            val = getattr(self, field.name)
            if not isinstance(val, field.type) and val != None:
                setattr(self, field.name, cast(val, field.type))

        # Replace None by default values
        # https://stackoverflow.com/a/69944614
        for field in fields(self):
            if not isinstance(field.default, dataclasses._MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)
