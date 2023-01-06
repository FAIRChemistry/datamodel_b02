import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class FlowModule(sdRDM.DataModel):

    """This section should provide all details about the equipment of the setup."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("flowmoduleINDEX"),
        xml="@id",
    )
    key: str = Field(
        ...,
        description="Name of the flow module",
        dataverse="pyDaRUS.Process.method_parameters.name",
    )

    id: str = Field(
        ...,
        description="A unique id that should be findable in the flow scheme",
        dataverse="pyDaRUS.Process.method_parameters.value",
    )

    manufacturer: Optional[str] = Field(
        description="Name of the manufacturer of the device",
        default=None,
    )

    type_number: Optional[str] = Field(
        description="Exact type number given by the manufacturer of the device",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    series: Optional[str] = Field(
        description="The Series of the device",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    manual_link: Optional[str] = Field(
        description="Possibility to get the manual of the device",
        dataverse="pyDaRUS.Process.method_parameters.value",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="None")
