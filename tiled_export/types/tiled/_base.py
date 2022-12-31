import dataclasses
from dataclasses import dataclass, field, fields


@dataclass
class Base():

    def __post_init__(self):

        def cast(value, type_):
            if type_ == bool:
                return False if value == "0" else True
            return type_(value)

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


@dataclass
class BaseObject(Base):

    class_: str = ""
    properties: list = field(default_factory=list)
