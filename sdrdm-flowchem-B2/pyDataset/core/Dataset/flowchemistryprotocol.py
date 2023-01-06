import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional

from .author import Author
from .flowmodule import FlowModule


@forge_signature
class FlowChemistryProtocol(sdRDM.DataModel):

    """This is the root of the data model and contains all objects defined in this example. While its good practice to have a single root, you can define as many roots as you like. Furthermore, the name does not have to be ```Root``` and can be any other name.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("flowchemistryprotocolINDEX"),
        xml="@id",
    )
    description: str = Field(
        ...,
        description="Describes the content of the dataset.",
        dataverse="pyDaRUS.Citation.description.text",
    )

    title: str = Field(
        ...,
        description="Title of the work",
        dataverse="pyDaRUS.Citation.title",
    )

    subject: str = Field(
        ...,
        description="Subject of matter linked to the dataset",
        dataverse="pyDaRUS.Citation.subject",
    )

    authors: List[Author] = Field(
        description="Authors of this dataset.",
        default_factory=ListPlus,
    )

    flowmodules: List[FlowModule] = Field(
        description="Equipment used in the flowprocess",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    def add_to_authors(
        self,
        name: str,
        affiliation: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:
            name (str): Full name including given and family name.
            affiliation (Optional[str]): To which organization the author is affiliated to. Defaults to None
        """

        authors = [
            Author(
                name=name,
                affiliation=affiliation,
            )
        ]

        self.authors = self.authors + authors

    def add_to_flowmodules(
        self,
        key: str,
        id: str,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        manual_link: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'FlowModule' to the attribute 'flowmodules'.

        Args:
            key (str): Name of the flow module.
            id (str): A unique id that should be findable in the flow scheme.
            manufacturer (Optional[str]): Name of the manufacturer of the device. Defaults to None
            type_number (Optional[str]): Exact type number given by the manufacturer of the device. Defaults to None
            series (Optional[str]): The Series of the device. Defaults to None
            manual_link (Optional[str]): Possibility to get the manual of the device. Defaults to None
        """

        flowmodules = [
            FlowModule(
                key=key,
                id=id,
                manufacturer=manufacturer,
                type_number=type_number,
                series=series,
                manual_link=manual_link,
            )
        ]

        self.flowmodules = self.flowmodules + flowmodules
