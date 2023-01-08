from pydantic_xml import BaseXmlModel, attr


class RootNode(BaseXmlModel):

    version: str = attr()
    tiledversion: str = attr()
