import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class CapillaryConnection(sdRDM.DataModel):

    """This section should provide all details about the capillary connections of the setup.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("capillaryconnectionINDEX"),
        xml="@id",
    )
    start: str = Field(
        ...,
        description=(
            "A unique ID of a Flowmodule (reaction / analysis) that should be findable"
            " in the flow scheme"
        ),
        dataverse="pyDaRUS.Process.method_parameters.name",
    )

    end: str = Field(
        ...,
        description=(
            "A unique ID of a Flowmodule (reaction / analysis) that should be findable"
            " in the flow scheme"
        ),
        dataverse="pyDaRUS.Process.method_parameters.value",
    )

    color: Optional[str] = Field(
        description="Color of the Capillary connection",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    material: Optional[str] = Field(
        description="Material of the Capillary connection",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    inner_diameter: Optional[float] = Field(
        description="Inner diameter of the Capillary connection in mm",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    length: Optional[float] = Field(
        description="Length of the Capillary connection in mm",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    ID: Optional[str] = Field(
        description="ID of the Capillary connection",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b0fc3d71fcf52185c0f38911ddd3994f9f99640b"
    )
