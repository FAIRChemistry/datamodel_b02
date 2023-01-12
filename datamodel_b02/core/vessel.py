from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .componentinformation import ComponentInformation


@forge_signature
class Vessel(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("vesselINDEX"),
        xml="@id",
    )

    volume: Optional[float] = Field(
        description="volume of the vessel in ml.", default=None
    )

    material: Optional[str] = Field(
        description="material the vessel is made of.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="adf936baacb5f1daed30a445b2e8875ca8cc0a6a"
    )
