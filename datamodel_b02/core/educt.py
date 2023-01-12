import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .reagent import Reagent
from .solvent import Solvent
from .stoichiometry import Stoichiometry


@forge_signature
class Educt(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("eductINDEX"),
        xml="@id",
    )

    reagents: List[Reagent] = Field(
        description="Reagent that is used in the reaction under study.",
        default_factory=ListPlus,
    )

    solvents: List[Solvent] = Field(
        description="solvent in which the educts are solved.", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="77e70dd05752c75381f94d10c2488f1e8d2ddd01"
    )

    def add_to_reagents(
        self,
        name: List[str],
        formula: Optional[str] = None,
        pureness: Optional[float] = None,
        supplier: Optional[str] = None,
        stoichiometry: Optional[Stoichiometry] = None,
        state_of_matter: Optional[str] = None,
        placeholder: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Reagent' to the attribute 'reagents'.

        Args:


            id (str): Unique identifier of the 'Reagent' object. Defaults to 'None'.


            name (List[str]): IUPAC name of the compound.


            formula (Optional[str]): molecular formula of the compound. Defaults to None


            pureness (Optional[float]): pureness of the compound in percent. Defaults to None


            supplier (Optional[str]): name of the supplier of the compound. Defaults to None


            stoichiometry (Optional[Stoichiometry]): stoichiometric information like equivalents, mass, amount of substance, volume. Defaults to None


            state_of_matter (Optional[str]): s for solid, l for liquid and g for gaseous. Defaults to None


            placeholder (Optional[int]): placeholder. Defaults to None
        """

        params = {
            "name": name,
            "formula": formula,
            "pureness": pureness,
            "supplier": supplier,
            "stoichiometry": stoichiometry,
            "state_of_matter": state_of_matter,
            "placeholder": placeholder,
        }
        if id is not None:
            params["id"] = id
        reagents = [Reagent(**params)]
        self.reagents = self.reagents + reagents

    def add_to_solvents(
        self,
        name: List[str],
        formula: Optional[str] = None,
        pureness: Optional[float] = None,
        supplier: Optional[str] = None,
        stoichiometry: Optional[Stoichiometry] = None,
        state_of_matter: Optional[str] = None,
        placeholder: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Solvent' to the attribute 'solvents'.

        Args:


            id (str): Unique identifier of the 'Solvent' object. Defaults to 'None'.


            name (List[str]): IUPAC name of the compound.


            formula (Optional[str]): molecular formula of the compound. Defaults to None


            pureness (Optional[float]): pureness of the compound in percent. Defaults to None


            supplier (Optional[str]): name of the supplier of the compound. Defaults to None


            stoichiometry (Optional[Stoichiometry]): stoichiometric information like equivalents, mass, amount of substance, volume. Defaults to None


            state_of_matter (Optional[str]): s for solid, l for liquid and g for gaseous. Defaults to None


            placeholder (Optional[int]): placeholder. Defaults to None
        """

        params = {
            "name": name,
            "formula": formula,
            "pureness": pureness,
            "supplier": supplier,
            "stoichiometry": stoichiometry,
            "state_of_matter": state_of_matter,
            "placeholder": placeholder,
        }
        if id is not None:
            params["id"] = id
        solvents = [Solvent(**params)]
        self.solvents = self.solvents + solvents
