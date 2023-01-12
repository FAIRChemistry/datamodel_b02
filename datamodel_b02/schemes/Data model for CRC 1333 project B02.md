```mermaid
classDiagram
    ComponentInformation <-- Thermocouple
    ComponentInformation <-- PressureGauge
    ComponentInformation <-- Analyzer
    ComponentInformation <-- Reactor
    ComponentInformation <-- Tubing
    ComponentInformation <-- Vessel
    ComponentInformation <-- PressureReducingRegulator
    ComponentInformation <-- BackPressureRegulator
    ComponentInformation <-- BallValve
    ComponentInformation <-- PlugValve
    ComponentInformation <-- NeedleValve
    ComponentInformation <-- CheckValve
    ComponentInformation <-- ReliefValve
    ComponentInformation <-- Pump
    ComponentInformation <-- ReciprocatingPump
    ComponentInformation <-- SyringePump
    ComponentInformation <-- MassFlowController
    ComponentInformation <-- Nozzle
    ComponentInformation <-- Mixer
    Chemical <-- Reagent
    Chemical <-- Solvent
    Chemical <-- InertGas
    Dataset *-- Author
    Dataset *-- ProcessScheme
    ProcessScheme *-- Device
    ProcessScheme *-- Tubing
    ProcessScheme *-- OperatingMedium
    ProcessScheme *-- OutputComposition
    Device *-- MeasuringInstrument
    Device *-- Reactor
    Device *-- FlowModule
    MeasuringInstrument *-- ProcessController
    MeasuringInstrument *-- Analyzer
    ProcessController *-- Thermocouple
    ProcessController *-- PressureGauge
    Tubing *-- Insulation
    Tubing *-- HeatingMantle
    Tubing *-- CoolingMantle
    FlowModule *-- Vessel
    FlowModule *-- PressureRegulator
    FlowModule *-- Valve
    FlowModule *-- Pump
    FlowModule *-- MassFlowController
    FlowModule *-- Nozzle
    FlowModule *-- Mixer
    PressureRegulator *-- PressureReducingRegulator
    PressureRegulator *-- BackPressureRegulator
    Valve *-- BallValve
    Valve *-- PlugValve
    Valve *-- NeedleValve
    Valve *-- CheckValve
    Valve *-- ReliefValve
    Pump *-- ReciprocatingPump
    Pump *-- SyringePump
    Chemical *-- Stoichiometry
    OperatingMedium *-- Educt
    OperatingMedium *-- InertGas
    Educt *-- Reagent
    Educt *-- Solvent
    
    class Dataset {
        +string title*
        +string description*
        +Author[0..*] authors*
        +ProcessScheme process_scheme
    }
    
    class Author {
        +string name*
        +string affiliation
    }
    
    class ProcessScheme {
        +Device[0..*] devices
        +Tubing[0..*] tubings
        +OperatingMedium[0..*] operating_media
        +OutputComposition output
    }
    
    class Device {
        +MeasuringInstrument measuring_instruments
        +Reactor reactors
        +FlowModule flow_modules
    }
    
    class MeasuringInstrument {
        +ProcessController process_controllers
        +Analyzer analyzers
    }
    
    class ProcessController {
        +Thermocouple[0..*] thermocouples
        +PressureGauge[0..*] pressure_gauge
    }
    
    class ComponentInformation {
        +string manufacturer
        +string type_number
        +string series
        +string operational_mode
    }
    
    class Thermocouple {
        +string thermocouple_type
    }
    
    class PressureGauge {
        +int placeholder
    }
    
    class Analyzer {
        +int placeholder
    }
    
    class Reactor {
        +string reactor_type
    }
    
    class Tubing {
        +string material
        +float inner_diameter
        +float wall_thickness
        +float length
        +Insulation insulation
        +HeatingMantle heating_mantle
        +CoolingMantle cooling_mantle
        +string ID
        +string color
    }
    
    class Insulation {
        +string insulation_material
        +float thickness
    }
    
    class HeatingMantle {
        +float length
        +float power
    }
    
    class CoolingMantle {
        +float length
        +float power
    }
    
    class FlowModule {
        +Vessel[0..*] vessels
        +PressureRegulator[0..*] pressure_regulators
        +Valve[0..*] valves
        +Pump[0..*] pumps
        +MassFlowController[0..*] mass_flow_controllers
        +Nozzle[0..*] nozzles
        +Mixer[0..*] mixers
    }
    
    class Vessel {
        +float volume
        +string material
    }
    
    class PressureRegulator {
        +PressureReducingRegulator pressure_reducing_regulators
        +BackPressureRegulator back_pressure_regulators
    }
    
    class PressureReducingRegulator {
        +int stages
        +int max_primary_pressure
        +int max_secundary_pressure
    }
    
    class BackPressureRegulator {
        +int max_primary_pressure
        +int min_primary_pressure
    }
    
    class Valve {
        +BallValve ball_valve
        +PlugValve plug_valves
        +NeedleValve needle_valves
        +CheckValve check_valves
        +ReliefValve relief_valves
    }
    
    class BallValve {
        +int number_of_ports
    }
    
    class PlugValve {
        +int number_of_ports
    }
    
    class NeedleValve {
        +int placeholder
    }
    
    class CheckValve {
        +int placeholder
    }
    
    class ReliefValve {
        +int placeholder
    }
    
    class Pump {
        +ReciprocatingPump[0..*] reciprocating_pumps
        +SyringePump[0..*] syringe_pumps
    }
    
    class ReciprocatingPump {
        +int placeholder
    }
    
    class SyringePump {
        +int placeholder
    }
    
    class MassFlowController {
        +float minimum_mass_flow
        +float maximum_mass_flow
    }
    
    class Nozzle {
        +int placeholder
    }
    
    class Mixer {
        +int placeholder
    }
    
    class Chemical {
        +string[0..*] name
        +string formula
        +float pureness
        +string supplier
        +Stoichiometry stoichiometry
        +string state_of_matter
    }
    
    class Stoichiometry {
        +float equivalents
        +float amount_of_substance
        +float mass
        +float volume
        +float density
        +float molar_mass
        +float mass_concentration
        +float molar_concentration
    }
    
    class OperatingMedium {
        +Educt[0..*] educts
        +InertGas inert_gas
    }
    
    class Educt {
        +Reagent[0..*] reagents
        +Solvent[0..*] solvents
    }
    
    class Reagent {
        +int placeholder
    }
    
    class Solvent {
        +int placeholder
    }
    
    class InertGas {
        +int placeholder
    }
    
    class OutputComposition {
        +Chemical[0..*] components
    }
    
```