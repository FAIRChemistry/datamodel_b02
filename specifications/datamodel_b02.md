# Data model for CRC 1333 project B02


### Dataset

- __title*__
  - Type: string
  - Description: title of the work.
- __description*__
  - Type: string
  - Description: describes the content of the dataset.
- __authors*__
  - Type: Author
  - Multiple: True
  - Description: authors of this dataset.
- __process_scheme__
  - Type: ProcessScheme
  - Description: PandID like setup scheme of the reactor.


### Author

This is another object that represents the author of the dataset. Please note, that the options here contain all required fields but also custom ones. In this example, the ```Dataverse``` option specifies where each field should be mapped, when exported to a Dataverse format. Hence, these options allow you to link your dataset towards any other data model without writing code by yourself.

- __name*__
  - Type: string
  - Description: full name including given and family name.
- __affiliation__
  - Type: string
  - Description: to which organization the author is affiliated to.


### ProcessScheme

- __devices__
  - Type: Device
  - Description: device of a reactor setup.
  - Multiple: True
- __tubings__
  - Type: Tubing
  - Description: tubing connection between two devices of a reactor setup.
  - Multiple: True
- __operating_media__
  - Type: OperatingMedium
  - Description: chemical used for the experiment.
  - Multiple: True
- __output__
  - Type: OutputComposition
  - Description: output of the experimental setup, propably containing the desired product, propably not.


### ComponentInformation

- __manufacturer__
  - Type: string
  - Description: name of the manufacturer of the device.
- __type_number__
  - Type: string
  - Description: exact type number given by the manufacturer of the device.
- __series__
  - Type: string
  - Description: the series of the device.
- __operational_mode__
  - Type: string
  - Description: operational mode of the flow module.

### Device

- __measuring_instruments__
  - Type: MeasurungInstrument
  - Description: instrument that measures a physical quantity.
- __reactors__
  - Type: Reactor
  - Description: tubing or vessel in which the reaction takes place.
- __flow_modules__
  - Type: FlowModule
  - Description: component involved in the transport of media.


### MeasuringInstrument

- __process_controllers__
  - Type: ProcessController
  - Description: devices that measure physical parameters to control and observe the process.
- __analyzers__
  - Type: Analyzer
  - Description: analyzation module to investigate the composition of the reactor output.


### ProcessController

- __thermocouples__
  - Type: Thermocouple
  - Description: thermocouple to measure the temperature at a specific position in the reaction plant.
  - Multiple: True

- __pressure_gauge__
  - Type: PressureGauge
  - Description: pressure gauge to measure the pressure at a specific position in the reaction plant.
  - Multiple: True


### Thermocouple[_ComponentInformation_]

- __thermocouple_type__
  - Type: string
  - Description: type of the thermocouple (E, J, K, M, N, T, B, R, S, C, D, G or others).


### PressureGauge[_ComponentInformation_]


### Analyzer[_ComponentInformation_]


### Reactor

- __reactor_type__
  - Type: string
  - Description: reactor type.


### Tubing

- __material__
  - Type: string
  - Description: material of the Capillary connection (e.g. 1.4404, silicone, etc.)
- __inner_diameter__
  - Type: float
  - Description: inner diameter of the Capillary connection in mm
- __wall_thickness__
  - Type: float
  - Description: wall thickness of the connection in mm
- __length__
  - Type: float
  - Description: length of the Capillary connection in mm
- __insulation__
  - Type: Insulation
  - Description: insulation of the connection
- __heating_mantle__
  - Type: HeatingMantle
  - Description: heating mantle of the connection
- __cooling_mantle__
  - Type: CoolingMantle
  - Description: cooling Mantle of the connection
- __ID__
  - Type: string
  - Description: ID of the Capillary connection
- __color__
  - Type: string
  - Description: color of the Capillary connection


### Insulation

- __insulation_material__
  - Type: string
  - Description: material of which the insulation is made of.
- __thickness__
   - Type: float
   - Description: thickness of the insulation in mm.


### HeatingMantle

- __length__
  - Type: float
  - Description: length of the heating mantle in mm.
- __power__
  - Type: float
  - Description: power of the heating mantle in W.


### CoolingMantle

- __length__
  - Type: float
  - Description: length of the cooling mantle in mm.
- __power__
  - Type: float
  - Description: power of the cooling mantle in W.


### Chemical

- __name__
  - Type: string
  - Description: IUPAC name of the compound.
  - Multiple: True
- __formula__
  - Type: string
  - Description: molecular formula of the compound.
- __pureness__
  - Type: float
  - Description: pureness of the compound in percent.
- __supplier__
  - Type: string
  - Description: name of the supplier of the compound.
- __stoichiometry__
  - Type: Stoichiometry
  - Description: stoichiometric information like equivalents, mass, amount of substance, volume
- __state_of_matter__
  - Type: string
  - Description: s for solid, l for liquid and g for gaseous


### Stoichiometry

Stoichiometric information about the compound.

- __equivalents__
  - Type: float
  - Description: used equivalents in relation to the reference compound
- __amount_of_substance__
  - Type: float
  - Description: amount of substance n in mmol
- __mass__
  - Type: float
  - Description: used mass of the compound in g
- __volume__
  - Type: float
  - Description: volume of the compound
- __density__
  - Type: float
  - Description: density of the compound at standard temperature and pressure.
- __molar_mass__
  - Type: float
  - Description: molar mass of the compound in g per mol
- __mass_concentration__
  - Type: float
  - Description: mass concentration in percent.
- __molar_concentration__
  - Type: float
  - Description: molar concentration in mol per l.


### OperatingMedium

- __educts__
  - Type: Educt
  - Description: educt of the reaction investigated.
  - Multiple: True
- __inert_gas__
  - Type: InertGas
  - Description: inert gas with which the reaction apparatus is flushed.


### Educt

- __reagents__
  - Type: Reagent
  - Description: Reagent that is used in the reaction under study.
  - Multiple: True
- __solvents__
  - Type Solvent
  - Description: solvent in which the educts are solved.
  - Multiple: True


### Reagent[_Chemical_]


### Solvent[_Chemical_]


### InertGas[_Chemical_]


### OutputComposition

- __Component__
  - Type: Chemical
  - Description: component of the output fluid.
  - Multiple: True


### FlowModule

- __vessels__
  - Type: Vessel
  - Description: vessels in which reactants are stored.
  - Multiple: True
- __pressure_regulators__
  - Type: PressureRegulator
  - Description: devices to control the pressure after or before them.
  - Multiple: True
- __valves__
  - Type: Valve
  - Description: different types of valves that are part of the plant.
  - Multiple: True
- __pumps__
  - Type: Pump
  - Description: different types of pumps that are part of the plant.
  - Multiple: True
- __mass_flow_controllers__
  - Type: MassFlowController
  - Description: electronic flow control device to remotely and precisely adjust the mass flow. 
  - Multiple: True
- __nozzles__
  - Type: Nozzle
  - Description: nozzle
  - Multiple: True
- __mixers__
  - Type: Mixer
  - Description: component that ensures good mixing of fluids.
  - Multiple: True


### Vessel[_ComponentInformation_]

- __volume__
  - Type: float
  - Description: volume of the vessel in ml.
- __material__
  - Type: string
  - Description: material the vessel is made of.


### PressureRegulator

- __pressure_reducing_regulators__
  - Type: PressureReducingRegulator
  - Description: pressure control device that reduces the primary pressure (e.g. coming form a gas cylinder) to a fixed value. Installed upstream.
- __back_pressure_regulators__
  - Type: BackPressureRegulator
  - Description: pressure control device that maintains a defined pressure upstream of its own inlet. Installed downstream.


### PressureReducingRegulator[_ComponentInformation_]

- __stages__
  - Type: integer
  - Description: number of stages the pressure reducing valve has (1 or 2). 
- __max_primary_pressure__
  - Type: integer
  - Description: maximum permissible primary pressure with which this device may be operated in mbar.
- __max_secundary_pressure__
  - Type: integer
  - Description: maximum possible secondary pressure that can be tapped at this device in mbar.


### BackPressureRegulator[_ComponentInformation_]

- __max_primary_pressure__
  - Type: integer
  - Description: maximum possible primary pressure that can be maintained by this device in mbar.
- __min_primary_pressure__
  - Type: integer
  - Description: minimum possible primary pressure that can be maintained by this device in mbar.


### Valve

- __ball_valve__
  - Type: BallValve
  - Description: flow control device which uses a hollow, (multi)perforated and pivoting ball to control flow through the valvle.
- __plug_valves__
  - Type: BallValve
  - Description: flow control device with cylindrical or conically tapered, (multi)perforated and pivoting plug to control flow through the valve.
- __needle_valves__
  - Type: NeedleValve
  - Description: flow control device with a small port and a threaded, needle-shaped plunger to allows precise regulation of flow, although it is generally only capable of relatively low flow rates.
- __check_valves__
  - Type: CheckValve
  - Description: flow control device that normally allows fluid to flow through it in only one direction.
- __relief_valves__
  - Type: ReliefValve
  - Description: flow control device for safety used to control or limit the pressure in a system and allowing the pressurized fluid to flow from an auxiliary passage out of the system.


### BallValve[_ComponentInformation_]

- __number_of_ports__
  - Type: integer
  - Description: number of ports


### PlugVavle[_ComponentInformation_]

- __number_of_ports__
  - Type: integer
  - Description: number of ports


### NeedleValve[_ComponentInformation_]


### CheckValve[_ComponentInformation_]


### ReliefValve[_ComponentInformation_]


### Pump[_ComponentInformation_]

- __reciprocating_pumps__
  - Type: ReciprocatingPump
  - Description: reciprocating pump.
  - Multiple: True
- __syringe_pumps__
  - Type: SyringePump
  - Description: syringe pump.
  - Multiple: True


### ReciprocatingPump[_ComponentInformation_]


### SyringePump[_ComponentInformation_]


### MFC[_ComponentInformation_]

- __minimum_mass_flow__
  - Type: float
  - Description: minimum volume flow in SCCM.
- __maximum_mass_flow__
  - Type: float
  - Description: maximum volume flow in SCCM.


### Nozzle[_ComponentInformation_]


### Mixer[_ComponentInformation_]



