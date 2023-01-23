import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .backpressureregulator import BackPressureRegulator
from .pressurereducingregulator import PressureReducingRegulator


@forge_signature
class PressureRegulator(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("pressureregulatorINDEX"),
        xml="@id",
    )

    pressure_reducing_regulators: Optional[PressureReducingRegulator] = Field(
        description=(
            "pressure control device that reduces the primary pressure, e.g. coming"
            " form a gas cylinder, to a fixed value. Installed upstream."
        ),
        default=None,
    )

    back_pressure_regulators: Optional[BackPressureRegulator] = Field(
        description=(
            "pressure control device that maintains a defined pressure upstream of its"
            " own inlet. Installed downstream."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="41a609850676450d6df0f1c036836a32e74f1eaf"
    )
