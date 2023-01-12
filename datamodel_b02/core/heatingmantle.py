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
        default="adf936baacb5f1daed30a445b2e8875ca8cc0a6a"
    )
