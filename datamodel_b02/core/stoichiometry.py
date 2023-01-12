import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Stoichiometry(sdRDM.DataModel):
    """Stoichiometric information about the compound."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("stoichiometryINDEX"),
        xml="@id",
    )

    equivalents: Optional[float] = Field(
        description="used equivalents in relation to the reference compound",
        default=None,
    )

    amount_of_substance: Optional[float] = Field(
        description="amount of substance n in mmol", default=None
    )

    mass: Optional[float] = Field(
        description="used mass of the compound in g", default=None
    )

    volume: Optional[float] = Field(description="volume of the compound", default=None)

    density: Optional[float] = Field(
        description="density of the compound at standard temperature and pressure.",
        default=None,
    )

    molar_mass: Optional[float] = Field(
        description="molar mass of the compound in g per mol", default=None
    )

    mass_concentration: Optional[float] = Field(
        description="mass concentration in percent.", default=None
    )

    molar_concentration: Optional[float] = Field(
        description="molar concentration in mol per l.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="293993f042f1c1fa4930e9edafb7db27e642d4b0"
    )
