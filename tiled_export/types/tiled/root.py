from pydantic_xml import BaseXmlModel, attr


class RootNode(BaseXmlModel):
    """
    An object when at root
    """

    version: str = attr()
    tiledversion: str = attr()
