import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .educt import Educt
from .inertgas import InertGas
from .reagent import Reagent
from .solvent import Solvent


@forge_signature
class OperatingMedium(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("operatingmediumINDEX"),
        xml="@id",
    )

    educts: List[Educt] = Field(
        description="educt of the reaction investigated.", default_factory=ListPlus
    )

    inert_gas: Optional[InertGas] = Field(
        description="inert gas with which the reaction apparatus is flushed.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="293993f042f1c1fa4930e9edafb7db27e642d4b0"
    )

    def add_to_educts(
        self, reagents: List[Reagent], solvents: List[Solvent], id: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'Educt' to the attribute 'educts'.

        Args:


            id (str): Unique identifier of the 'Educt' object. Defaults to 'None'.


            reagents (List[Reagent]): Reagent that is used in the reaction under study.


            solvents (List[Solvent]): solvent in which the educts are solved.
        """

        params = {"reagents": reagents, "solvents": solvents}
        if id is not None:
            params["id"] = id
        educts = [Educt(**params)]
        self.educts = self.educts + educts
