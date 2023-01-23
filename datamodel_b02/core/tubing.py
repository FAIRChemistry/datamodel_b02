import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .coolingmantle import CoolingMantle
from .heatingmantle import HeatingMantle
from .insulation import Insulation
from .componentinformation import ComponentInformation


@forge_signature
class Tubing(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("tubingINDEX"),
        xml="@id",
    )

    material: Optional[str] = Field(
        description="material of the Capillary connection, e.g. 1.4404, silicone, etc.",
        default=None,
    )

    inner_diameter: Optional[float] = Field(
        description="inner diameter of the Capillary connection in mm", default=None
    )

    wall_thickness: Optional[float] = Field(
        description="wall thickness of the connection in mm", default=None
    )

    length: Optional[float] = Field(
        description="length of the Capillary connection in mm", default=None
    )

    insulation: Optional[Insulation] = Field(
        description="insulation of the connection", default=None
    )

    heating_mantle: Optional[HeatingMantle] = Field(
        description="heating mantle of the connection", default=None
    )

    cooling_mantle: Optional[CoolingMantle] = Field(
        description="cooling Mantle of the connection", default=None
    )

    ID: Optional[str] = Field(
        description="ID of the Capillary connection", default=None
    )

    color: Optional[str] = Field(
        description="color of the Capillary connection", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c797b854fa0b6a85438601dcbd3056189258ba98"
    )
