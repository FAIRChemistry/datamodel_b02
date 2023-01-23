import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .chemical import Chemical
from .stoichiometry import Stoichiometry


@forge_signature
class OutputComposition(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("outputcompositionINDEX"),
        xml="@id",
    )

    components: List[Chemical] = Field(
        description="component of the output fluid.", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c797b854fa0b6a85438601dcbd3056189258ba98"
    )

    def add_to_components(
        self,
        name: List[str],
        formula: Optional[str] = None,
        pureness: Optional[float] = None,
        supplier: Optional[str] = None,
        stoichiometry: Optional[Stoichiometry] = None,
        state_of_matter: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Chemical' to the attribute 'components'.

        Args:


            id (str): Unique identifier of the 'Chemical' object. Defaults to 'None'.


            name (List[str]): IUPAC name of the compound.


            formula (Optional[str]): molecular formula of the compound. Defaults to None


            pureness (Optional[float]): pureness of the compound in percent. Defaults to None


            supplier (Optional[str]): name of the supplier of the compound. Defaults to None


            stoichiometry (Optional[Stoichiometry]): stoichiometric information like equivalents, mass, amount of substance, volume. Defaults to None


            state_of_matter (Optional[str]): s for solid, l for liquid and g for gaseous. Defaults to None
        """

        params = {
            "name": name,
            "formula": formula,
            "pureness": pureness,
            "supplier": supplier,
            "stoichiometry": stoichiometry,
            "state_of_matter": state_of_matter,
        }
        if id is not None:
            params["id"] = id
        components = [Chemical(**params)]
        self.components = self.components + components
