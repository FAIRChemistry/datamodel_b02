import sdRDM

from typing import Optional, Union
from typing import Optional
from typing import List
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .backpressureregulator import BackPressureRegulator
from .ballvalve import BallValve
from .checkvalve import CheckValve
from .massflowcontroller import MassFlowController
from .needlevalve import NeedleValve
from .nozzle import Nozzle
from .plugvalve import PlugValve
from .pressurereducingregulator import PressureReducingRegulator
from .pressureregulator import PressureRegulator
from .pump import Pump
from .reciprocatingpump import ReciprocatingPump
from .reliefvalve import ReliefValve
from .syringepump import SyringePump
from .valve import Valve
from .vessel import Vessel
from .mixer import Mixer


@forge_signature
class FlowModule(sdRDM.DataModel):
    """This section should provide all details about the equipment of the setup."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("flowmoduleINDEX"),
        xml="@id",
    )

    vessels: List[Vessel] = Field(
        description="vessels in which the reactants are stored.",
        default_factory=ListPlus,
    )

    pressure_regulators: List[PressureRegulator] = Field(
        description="devices to control the pressure after or before them.",
        default_factory=ListPlus,
    )

    valves: List[Valve] = Field(
        description="different types of valves that are part of the plant.",
        default_factory=ListPlus,
    )

    pumps: List[Pump] = Field(
        description="different types of pumps that are part of the plant.",
        default_factory=ListPlus,
    )

    mass_flow_controllers: List[MassFlowController] = Field(
        description=(
            "electronic flow control device to remotely and precisely adjust the mass"
            " flow."
        ),
        default_factory=ListPlus,
    )

    nozzles: List[Nozzle] = Field(description="nozzle.", default_factory=ListPlus)

    mixers: List[Mixer] = Field(
        description="component that ensures good mixing of fluids.",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="4c9b99d8f8bfef1da92cd9da2ca6cc7487cee9fe"
    )

    def add_to_vessels(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        volume: Optional[float] = None,
        material: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Vessel' to the attribute 'vessels'.

        Args:


            id (str): Unique identifier of the 'Vessel' object. Defaults to 'None'.


            manufacturer (Optional[str]): name of the manufacturer of the device. Defaults to None


            type_number (Optional[str]): exact type number given by the manufacturer of the device. Defaults to None


            series (Optional[str]): the series of the device. Defaults to None


            operational_mode (Optional[str]): operational mode of the flow module. Defaults to None


            volume (Optional[float]): volume of the vessel in ml. Defaults to None


            material (Optional[str]): material the vessel is made of. Defaults to None
        """

        params = {
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "operational_mode": operational_mode,
            "volume": volume,
            "material": material,
        }
        if id is not None:
            params["id"] = id
        vessels = [Vessel(**params)]
        self.vessels = self.vessels + vessels

    def add_to_pressure_regulators(
        self,
        pressure_reducing_regulators: Optional[PressureReducingRegulator] = None,
        back_pressure_regulators: Optional[BackPressureRegulator] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'PressureRegulator' to the attribute 'pressure_regulators'.

        Args:


            id (str): Unique identifier of the 'PressureRegulator' object. Defaults to 'None'.


            pressure_reducing_regulators (Optional[PressureReducingRegulator]): pressure control device that reduces the primary pressure, e.g. coming form a gas cylinder, to a fixed value. Installed upstream. Defaults to None


            back_pressure_regulators (Optional[BackPressureRegulator]): pressure control device that maintains a defined pressure upstream of its own inlet. Installed downstream. Defaults to None
        """

        params = {
            "pressure_reducing_regulators": pressure_reducing_regulators,
            "back_pressure_regulators": back_pressure_regulators,
        }
        if id is not None:
            params["id"] = id
        pressure_regulators = [PressureRegulator(**params)]
        self.pressure_regulators = self.pressure_regulators + pressure_regulators

    def add_to_valves(
        self,
        ball_valve: Optional[BallValve] = None,
        plug_valves: Optional[PlugValve] = None,
        needle_valves: Optional[NeedleValve] = None,
        check_valves: Optional[CheckValve] = None,
        relief_valves: Optional[ReliefValve] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Valve' to the attribute 'valves'.

        Args:


            id (str): Unique identifier of the 'Valve' object. Defaults to 'None'.


            ball_valve (Optional[BallValve]): flow control device which uses a hollow, single or multi perforated and pivoting ball to control flow through the valvle. Defaults to None


            plug_valves (Optional[PlugValve]): flow control device with cylindrical or conically tapered, single or multi perforated and pivoting plug to control flow through the valve. Defaults to None


            needle_valves (Optional[NeedleValve]): flow control device with a small port and a threaded, needle-shaped plunger to allows precise regulation of flow, although it is generally only capable of relatively low flow rates. Defaults to None


            check_valves (Optional[CheckValve]): flow control device that normally allows fluid to flow through it in only one direction. Defaults to None


            relief_valves (Optional[ReliefValve]): flow control device for safety used to control or limit the pressure in a system and allowing the pressurized fluid to flow from an auxiliary passage out of the system. Defaults to None
        """

        params = {
            "ball_valve": ball_valve,
            "plug_valves": plug_valves,
            "needle_valves": needle_valves,
            "check_valves": check_valves,
            "relief_valves": relief_valves,
        }
        if id is not None:
            params["id"] = id
        valves = [Valve(**params)]
        self.valves = self.valves + valves

    def add_to_pumps(
        self,
        reciprocating_pumps: List[ReciprocatingPump],
        syringe_pumps: List[SyringePump],
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Pump' to the attribute 'pumps'.

        Args:


            id (str): Unique identifier of the 'Pump' object. Defaults to 'None'.


            reciprocating_pumps (List[ReciprocatingPump]): reciprocating pump.


            syringe_pumps (List[SyringePump]): syringe pump.


            manufacturer (Optional[str]): name of the manufacturer of the device. Defaults to None


            type_number (Optional[str]): exact type number given by the manufacturer of the device. Defaults to None


            series (Optional[str]): the series of the device. Defaults to None


            operational_mode (Optional[str]): operational mode of the flow module. Defaults to None
        """

        params = {
            "reciprocating_pumps": reciprocating_pumps,
            "syringe_pumps": syringe_pumps,
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "operational_mode": operational_mode,
        }
        if id is not None:
            params["id"] = id
        pumps = [Pump(**params)]
        self.pumps = self.pumps + pumps

    def add_to_mass_flow_controllers(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        minimum_mass_flow: Optional[float] = None,
        maximum_mass_flow: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'MassFlowController' to the attribute 'mass_flow_controllers'.

        Args:


            id (str): Unique identifier of the 'MassFlowController' object. Defaults to 'None'.


            manufacturer (Optional[str]): name of the manufacturer of the device. Defaults to None


            type_number (Optional[str]): exact type number given by the manufacturer of the device. Defaults to None


            series (Optional[str]): the series of the device. Defaults to None


            operational_mode (Optional[str]): operational mode of the flow module. Defaults to None


            minimum_mass_flow (Optional[float]): minimum volume flow in SCCM. Defaults to None


            maximum_mass_flow (Optional[float]): maximum volume flow in SCCM. Defaults to None
        """

        params = {
            "manufacturer": manufacturer,
            "type_number": type_number,
            "series": series,
            "operational_mode": operational_mode,
            "minimum_mass_flow": minimum_mass_flow,
            "maximum_mass_flow": maximum_mass_flow,
        }
        if id is not None:
            params["id"] = id
        mass_flow_controllers = [MassFlowController(**params)]
        self.mass_flow_controllers = self.mass_flow_controllers + mass_flow_controllers

    def add_to_nozzles(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        placeholder: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Nozzle' to the attribute 'nozzles'.

        Args:


            id (str): Unique identifier of the 'Nozzle' object. Defaults to 'None'.


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
        nozzles = [Nozzle(**params)]
        self.nozzles = self.nozzles + nozzles

    def add_to_mixers(
        self,
        manufacturer: Optional[str] = None,
        type_number: Optional[str] = None,
        series: Optional[str] = None,
        operational_mode: Optional[str] = None,
        placeholder: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Mixer' to the attribute 'mixers'.

        Args:


            id (str): Unique identifier of the 'Mixer' object. Defaults to 'None'.


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
        mixers = [Mixer(**params)]
        self.mixers = self.mixers + mixers
