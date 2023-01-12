import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class CoolingMantle(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("coolingmantleINDEX"),
        xml="@id",
    )

    length: Optional[float] = Field(
        description="length of the cooling mantle in mm.", default=None
    )

    power: Optional[float] = Field(
        description="power of the cooling mantle in W.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="77e70dd05752c75381f94d10c2488f1e8d2ddd01"
    )
