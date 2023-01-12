import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ComponentInformation(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("componentinformationINDEX"),
        xml="@id",
    )

    manufacturer: Optional[str] = Field(
        description="name of the manufacturer of the device.", default=None
    )

    type_number: Optional[str] = Field(
        description="exact type number given by the manufacturer of the device.",
        default=None,
    )

    series: Optional[str] = Field(description="the series of the device.", default=None)

    operational_mode: Optional[str] = Field(
        description="operational mode of the flow module.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="1e3c1dd9ffd79c2ed7f59e418212f341e9c2f977"
    )
