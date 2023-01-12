from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .componentinformation import ComponentInformation


@forge_signature
class ReliefValve(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reliefvalveINDEX"),
        xml="@id",
    )

    placeholder: Optional[int] = Field(description="placeholder", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="293993f042f1c1fa4930e9edafb7db27e642d4b0"
    )
