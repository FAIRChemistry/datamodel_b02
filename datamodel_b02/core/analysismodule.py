from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .flowmodule import FlowModule


@forge_signature
class AnalysisModule(FlowModule):
    """This section should provide all details about the equipment of the setup."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysismoduleINDEX"),
        xml="@id",
    )

    description: Optional[str] = Field(
        description="A description of the purpose of the module.",
        dataverse="pyDaRUS.Process.method_parameters.name",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bf8592932fe757def0bd5c878a13e085d0344240"
    )
