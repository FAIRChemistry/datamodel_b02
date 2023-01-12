import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class HeatingMantle(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("heatingmantleINDEX"),
        xml="@id",
    )

    length: Optional[float] = Field(
        description="length of the heating mantle in mm.", default=None
    )

    power: Optional[float] = Field(
        description="power of the heating mantle in W.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="1f46c6e9b1ff52ff4820a24a83eccf60d379514b"
    )
