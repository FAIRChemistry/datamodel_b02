from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .componentinformation import ComponentInformation
from .reciprocatingpump import ReciprocatingPump
from .syringepump import SyringePump


@forge_signature
class Pump(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("pumpINDEX"),
        xml="@id",
    )

    reciprocating_pumps: List[ReciprocatingPump] = Field(
        description="reciprocating pump.", default_factory=ListPlus
    )

    syringe_pumps: List[SyringePump] = Field(
        description="syringe pump.", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="1f46c6e9b1ff52ff4820a24a83eccf60d379514b"
    )

    def add_to_reciprocating_pumps(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        placeholder: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'ReciprocatingPump' to the attribute 'reciprocating_pumps'.

        Args:


            id (str): Unique identifier of the 'ReciprocatingPump' object. Defaults to 'None'.


            manufacturer (Optional[str]): name of the manufacturer of the device. Defaults to None


            type_number (Optional[str]): exact type number given by the manufacturer of the device. Defaults to None


            series (Optional[str]): the series of the device. Defaults to None


            operational_mode (Optional[str]): operational mode of the flow module. Defaults to None


            placeholder (Optional[int]): placeholder. Defaults to None
        """

        params = {
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "operational_mode": operational_mode,
            "placeholder": placeholder,
        }
        if id is not None:
            params["id"] = id
        reciprocating_pumps = [ReciprocatingPump(**params)]
        self.reciprocating_pumps = self.reciprocating_pumps + reciprocating_pumps

    def add_to_syringe_pumps(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        placeholder: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'SyringePump' to the attribute 'syringe_pumps'.

        Args:


            id (str): Unique identifier of the 'SyringePump' object. Defaults to 'None'.


            manufacturer (Optional[str]): name of the manufacturer of the device. Defaults to None


            type_number (Optional[str]): exact type number given by the manufacturer of the device. Defaults to None


            series (Optional[str]): the series of the device. Defaults to None


            operational_mode (Optional[str]): operational mode of the flow module. Defaults to None


            placeholder (Optional[int]): placeholder. Defaults to None
        """

        params = {
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "operational_mode": operational_mode,
            "placeholder": placeholder,
        }
        if id is not None:
            params["id"] = id
        syringe_pumps = [SyringePump(**params)]
        self.syringe_pumps = self.syringe_pumps + syringe_pumps
