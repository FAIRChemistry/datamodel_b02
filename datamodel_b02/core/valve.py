import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .ballvalve import BallValve
from .checkvalve import CheckValve
from .needlevalve import NeedleValve
from .plugvalve import PlugValve
from .reliefvalve import ReliefValve


@forge_signature
class Valve(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("valveINDEX"),
        xml="@id",
    )

    ball_valve: Optional[BallValve] = Field(
        description=(
            "flow control device which uses a hollow, single or multi perforated and"
            " pivoting ball to control flow through the valvle."
        ),
        default=None,
    )

    plug_valves: Optional[PlugValve] = Field(
        description=(
            "flow control device with cylindrical or conically tapered, single or multi"
            " perforated and pivoting plug to control flow through the valve."
        ),
        default=None,
    )

    needle_valves: Optional[NeedleValve] = Field(
        description=(
            "flow control device with a small port and a threaded, needle-shaped"
            " plunger to allows precise regulation of flow, although it is generally"
            " only capable of relatively low flow rates."
        ),
        default=None,
    )

    check_valves: Optional[CheckValve] = Field(
        description=(
            "flow control device that normally allows fluid to flow through it in only"
            " one direction."
        ),
        default=None,
    )

    relief_valves: Optional[ReliefValve] = Field(
        description=(
            "flow control device for safety used to control or limit the pressure in a"
            " system and allowing the pressurized fluid to flow from an auxiliary"
            " passage out of the system."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="293993f042f1c1fa4930e9edafb7db27e642d4b0"
    )
