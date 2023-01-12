import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .analyzer import Analyzer
from .processcontroller import ProcessController


@forge_signature
class MeasuringInstrument(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measuringinstrumentINDEX"),
        xml="@id",
    )

    process_controllers: Optional[ProcessController] = Field(
        description=(
            "devices that measure physical parameters to control and observe the"
            " process."
        ),
        default=None,
    )

    analyzers: Optional[Analyzer] = Field(
        description=(
            "analyzation module to investigate the composition of the reactor output."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="4c9b99d8f8bfef1da92cd9da2ca6cc7487cee9fe"
    )
