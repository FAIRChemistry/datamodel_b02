import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional

from .analysismodule import AnalysisModule
from .author import Author
from .capillaryconnection import CapillaryConnection
from .flowmodule import FlowModule
from .reactionmodule import ReactionModule


@forge_signature
class Dataset(sdRDM.DataModel):

    """This is the root of the data model and contains all objects defined in this example. While its good practice to have a single root, you can define as many roots as you like. Furthermore, the name does not have to be ```Root``` and can be any other name.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
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

    reactionmodules: List[ReactionModule] = Field(
        description="Flow modules in the reaction part of the process",
        default_factory=ListPlus,
    )

    analysismodules: List[AnalysisModule] = Field(
        description="Flow modules in the analysis part of the process",
        default_factory=ListPlus,
    )

    capillaryconnections: List[CapillaryConnection] = Field(
        description="A Capillary connection between two flow modules",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bf8592932fe757def0bd5c878a13e085d0344240"
    )

    def add_to_authors(
        self, name: str, affiliation: Optional[str] = None, id: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (str): Full name including given and family name.
            affiliation (Optional[str]): To which organization the author is affiliated to. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
        }

        if id is not None:
            params["id"] = id

        authors = [Author(**params)]

        self.authors = self.authors + authors

    def add_to_flowmodules(
        self,
        key: str,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        manual_link: Optional[str] = None,
        operation_mode: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'FlowModule' to the attribute 'flowmodules'.

        Args:
            id (str): Unique identifier of the 'FlowModule' object. Defaults to 'None'.
            key (str): Name of the flow module.
            manufacturer (Optional[str]): Name of the manufacturer of the device. Defaults to None
            type_number (Optional[str]): Exact type number given by the manufacturer of the device. Defaults to None
            series (Optional[str]): The Series of the device. Defaults to None
            manual_link (Optional[str]): Possibility to get the manual of the device. Defaults to None
            operation_mode (Optional[str]): Operation mode of the Flow module. Defaults to None
        """

        params = {
            "key": key,
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "manual_link": manual_link,
            "operation_mode": operation_mode,
        }

        if id is not None:
            params["id"] = id

        flowmodules = [FlowModule(**params)]

        self.flowmodules = self.flowmodules + flowmodules

    def add_to_reactionmodules(
        self,
        key: str,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        manual_link: Optional[str] = None,
        operation_mode: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'ReactionModule' to the attribute 'reactionmodules'.

        Args:
            id (str): Unique identifier of the 'ReactionModule' object. Defaults to 'None'.
            key (str): Name of the flow module.
            manufacturer (Optional[str]): Name of the manufacturer of the device. Defaults to None
            type_number (Optional[str]): Exact type number given by the manufacturer of the device. Defaults to None
            series (Optional[str]): The Series of the device. Defaults to None
            manual_link (Optional[str]): Possibility to get the manual of the device. Defaults to None
            operation_mode (Optional[str]): Operation mode of the Flow module. Defaults to None
            description (Optional[str]): A description of the purpose of the module. Defaults to None
        """

        params = {
            "key": key,
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "manual_link": manual_link,
            "operation_mode": operation_mode,
            "description": description,
        }

        if id is not None:
            params["id"] = id

        reactionmodules = [ReactionModule(**params)]

        self.reactionmodules = self.reactionmodules + reactionmodules

    def add_to_analysismodules(
        self,
        key: str,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        manual_link: Optional[str] = None,
        operation_mode: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'AnalysisModule' to the attribute 'analysismodules'.

        Args:
            id (str): Unique identifier of the 'AnalysisModule' object. Defaults to 'None'.
            key (str): Name of the flow module.
            manufacturer (Optional[str]): Name of the manufacturer of the device. Defaults to None
            type_number (Optional[str]): Exact type number given by the manufacturer of the device. Defaults to None
            series (Optional[str]): The Series of the device. Defaults to None
            manual_link (Optional[str]): Possibility to get the manual of the device. Defaults to None
            operation_mode (Optional[str]): Operation mode of the Flow module. Defaults to None
            description (Optional[str]): A description of the purpose of the module. Defaults to None
        """

        params = {
            "key": key,
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "manual_link": manual_link,
            "operation_mode": operation_mode,
            "description": description,
        }

        if id is not None:
            params["id"] = id

        analysismodules = [AnalysisModule(**params)]

        self.analysismodules = self.analysismodules + analysismodules

    def add_to_capillaryconnections(
        self,
        start: str,
        end: str,
        color: Optional[str] = None,
        material: Optional[str] = None,
        inner_diameter: Optional[float] = None,
        length: Optional[float] = None,
        ID: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'CapillaryConnection' to the attribute 'capillaryconnections'.

        Args:
            id (str): Unique identifier of the 'CapillaryConnection' object. Defaults to 'None'.
            start (str): A unique ID of a Flowmodule (reaction / analysis) that should be findable in the flow scheme.
            end (str): A unique ID of a Flowmodule (reaction / analysis) that should be findable in the flow scheme.
            color (Optional[str]): Color of the Capillary connection. Defaults to None
            material (Optional[str]): Material of the Capillary connection. Defaults to None
            inner_diameter (Optional[float]): Inner diameter of the Capillary connection in mm. Defaults to None
            length (Optional[float]): Length of the Capillary connection in mm. Defaults to None
            ID (Optional[str]): ID of the Capillary connection. Defaults to None
        """

        params = {
            "start": start,
            "end": end,
            "color": color,
            "material": material,
            "inner_diameter": inner_diameter,
            "length": length,
            "ID": ID,
        }

        if id is not None:
            params["id"] = id

        capillaryconnections = [CapillaryConnection(**params)]

        self.capillaryconnections = self.capillaryconnections + capillaryconnections
