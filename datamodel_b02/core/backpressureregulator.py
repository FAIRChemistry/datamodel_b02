from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .componentinformation import ComponentInformation


@forge_signature
class BackPressureRegulator(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("backpressureregulatorINDEX"),
        xml="@id",
    )

    max_primary_pressure: Optional[int] = Field(
        description=(
            "maximum possible primary pressure that can be maintained by this device in"
            " mbar."
        ),
        default=None,
    )

    min_primary_pressure: Optional[int] = Field(
        description=(
            "minimum possible primary pressure that can be maintained by this device in"
            " mbar."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="9c71adb672a8872ef0b47cda2cdc4ecb47fa7c8d"
    )
