from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .flowmodule import FlowModule


@forge_signature
class ReactionModule(FlowModule):

    """This section should provide all details about the equipment of the setup."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionmoduleINDEX"),
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
        default="b0fc3d71fcf52185c0f38911ddd3994f9f99640b"
    )
