import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .pressuregauge import PressureGauge
from .thermocouple import Thermocouple


@forge_signature
class ProcessController(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processcontrollerINDEX"),
        xml="@id",
    )

    thermocouples: List[Thermocouple] = Field(
        description=(
            "thermocouple to measure the temperature at a specific position in the"
            " reaction plant."
        ),
        default_factory=ListPlus,
    )

    pressure_gauge: List[PressureGauge] = Field(
        description=(
            "pressure gauge to measure the pressure at a specific position in the"
            " reaction plant."
        ),
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c797b854fa0b6a85438601dcbd3056189258ba98"
    )

    def add_to_thermocouples(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        thermocouple_type: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Thermocouple' to the attribute 'thermocouples'.

        Args:


            id (str): Unique identifier of the 'Thermocouple' object. Defaults to 'None'.


            manufacturer (Optional[str]): name of the manufacturer of the device. Defaults to None


            type_number (Optional[str]): exact type number given by the manufacturer of the device. Defaults to None


            series (Optional[str]): the series of the device. Defaults to None


            operational_mode (Optional[str]): operational mode of the flow module. Defaults to None


            thermocouple_type (Optional[str]): type of the thermocouple like J, K, R, S. Defaults to None
        """

        params = {
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "operational_mode": operational_mode,
            "thermocouple_type": thermocouple_type,
        }
        if id is not None:
            params["id"] = id
        thermocouples = [Thermocouple(**params)]
        self.thermocouples = self.thermocouples + thermocouples

    def add_to_pressure_gauge(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        placeholder: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'PressureGauge' to the attribute 'pressure_gauge'.

        Args:


            id (str): Unique identifier of the 'PressureGauge' object. Defaults to 'None'.


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
        pressure_gauge = [PressureGauge(**params)]
        self.pressure_gauge = self.pressure_gauge + pressure_gauge
