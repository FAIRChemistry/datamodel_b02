import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class CoolingMantle(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("coolingmantleINDEX"),
        xml="@id",
    )
    length: Optional[float] = Field(
        description="length of the cooling mantle in mm.",
        default=None,
    )

    power: Optional[float] = Field(
        description="power of the cooling mantle in W.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8ad9c293393d92336f63257326745c6bc4db3b6b"
    )
