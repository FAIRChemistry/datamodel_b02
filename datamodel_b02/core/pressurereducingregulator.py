from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .componentinformation import ComponentInformation


@forge_signature
class PressureReducingRegulator(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("pressurereducingregulatorINDEX"),
        xml="@id",
    )

    stages: Optional[int] = Field(
        description="number of stages the pressure reducing valve has, usually 1 or 2.",
        default=None,
    )

    max_primary_pressure: Optional[int] = Field(
        description=(
            "maximum permissible primary pressure with which this device may be"
            " operated in mbar."
        ),
        default=None,
    )

    max_secundary_pressure: Optional[int] = Field(
        description=(
            "maximum possible secondary pressure that can be tapped at this device in"
            " mbar."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c797b854fa0b6a85438601dcbd3056189258ba98"
    )
