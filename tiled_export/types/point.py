from pydantic_xml import BaseXmlModel, attr


class Point(BaseXmlModel, tag='point'):

    x: int = attr()
    y: int = attr()
