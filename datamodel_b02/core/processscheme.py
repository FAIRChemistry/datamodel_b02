import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional

from .coolingmantle import CoolingMantle
from .device import Device
from .educt import Educt
from .flowmodule import FlowModule
from .heatingmantle import HeatingMantle
from .inertgas import InertGas
from .insulation import Insulation
from .measuringinstrument import MeasuringInstrument
from .operatingmedium import OperatingMedium
from .outputcomposition import OutputComposition
from .reactor import Reactor
from .tubing import Tubing


@forge_signature
class ProcessScheme(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processschemeINDEX"),
        xml="@id",
    )
    devices: List[Device] = Field(
        description="device of a reactor setup.",
        default_factory=ListPlus,
    )

    tubings: List[Tubing] = Field(
        description="tubing connection between two devices of a reactor setup.",
        default_factory=ListPlus,
    )

    operating_media: List[OperatingMedium] = Field(
        description="chemical used for the experiment.",
        default_factory=ListPlus,
    )

    output: Optional[OutputComposition] = Field(
        description=(
            "output of the experimental setup, propably containing the desired product,"
            " propably not."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8ad9c293393d92336f63257326745c6bc4db3b6b"
    )

    def add_to_devices(
        self,
        measuring_instruments: Optional[MeasuringInstrument] = None,
        reactors: Optional[Reactor] = None,
        flow_modules: Optional[FlowModule] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Device' to the attribute 'devices'.

        Args:
            id (str): Unique identifier of the 'Device' object. Defaults to 'None'.
            measuring_instruments (Optional[MeasuringInstrument]): instrument that measures a physical quantity. Defaults to None
            reactors (Optional[Reactor]): tubing or vessel in which the reaction takes place. Defaults to None
            flow_modules (Optional[FlowModule]): component involved in the transport of media. Defaults to None
        """

        params = {
            "measuring_instruments": measuring_instruments,
            "reactors": reactors,
            "flow_modules": flow_modules,
        }

        if id is not None:
            params["id"] = id

        devices = [Device(**params)]

        self.devices = self.devices + devices

    def add_to_tubings(
        self,
        material: Optional[str] = None,
        inner_diameter: Optional[float] = None,
        wall_thickness: Optional[float] = None,
        length: Optional[float] = None,
        insulation: Optional[Insulation] = None,
        heating_mantle: Optional[HeatingMantle] = None,
        cooling_mantle: Optional[CoolingMantle] = None,
        ID: Optional[str] = None,
        color: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Tubing' to the attribute 'tubings'.

        Args:
            id (str): Unique identifier of the 'Tubing' object. Defaults to 'None'.
            material (Optional[str]): material of the Capillary connection, e.g. 1.4404, silicone, etc. Defaults to None
            inner_diameter (Optional[float]): inner diameter of the Capillary connection in mm. Defaults to None
            wall_thickness (Optional[float]): wall thickness of the connection in mm. Defaults to None
            length (Optional[float]): length of the Capillary connection in mm. Defaults to None
            insulation (Optional[Insulation]): insulation of the connection. Defaults to None
            heating_mantle (Optional[HeatingMantle]): heating mantle of the connection. Defaults to None
            cooling_mantle (Optional[CoolingMantle]): cooling Mantle of the connection. Defaults to None
            ID (Optional[str]): ID of the Capillary connection. Defaults to None
            color (Optional[str]): color of the Capillary connection. Defaults to None
        """

        params = {
            "material": material,
            "inner_diameter": inner_diameter,
            "wall_thickness": wall_thickness,
            "length": length,
            "insulation": insulation,
            "heating_mantle": heating_mantle,
            "cooling_mantle": cooling_mantle,
            "ID": ID,
            "color": color,
        }

        if id is not None:
            params["id"] = id

        tubings = [Tubing(**params)]

        self.tubings = self.tubings + tubings

    def add_to_operating_media(
        self,
        educts: List[Educt],
        inert_gas: Optional[InertGas] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'OperatingMedium' to the attribute 'operating_media'.

        Args:
            id (str): Unique identifier of the 'OperatingMedium' object. Defaults to 'None'.
            educts (List[Educt]): educt of the reaction investigated.
            inert_gas (Optional[InertGas]): inert gas with which the reaction apparatus is flushed. Defaults to None
        """

        params = {
            "educts": educts,
            "inert_gas": inert_gas,
        }

        if id is not None:
            params["id"] = id

        operating_media = [OperatingMedium(**params)]

        self.operating_media = self.operating_media + operating_media
