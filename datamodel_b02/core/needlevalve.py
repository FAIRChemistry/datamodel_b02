from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .componentinformation import ComponentInformation


@forge_signature
class NeedleValve(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("needlevalveINDEX"),
        xml="@id",
    )
    placeholder: Optional[int] = Field(
        description="placeholder",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8ad9c293393d92336f63257326745c6bc4db3b6b"
    )
