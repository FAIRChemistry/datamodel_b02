import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Author(sdRDM.DataModel):

    """This is another object that represents the author of the dataset. Please note, that the options here contain all required fields but also custom ones. In this example, the ```Dataverse``` option specifies where each field should be mapped, when exported to a Dataverse format. Hence, these options allow you to link your dataset towards any other data model without writing code by yourself.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Full name including given and family name",
        dataverse="pyDaRUS.Citation.author.name",
    )

    affiliation: Optional[str] = Field(
        description="To which organization the author is affiliated to",
        dataverse="pyDaRUS.Citation.author.affiliation",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b0fc3d71fcf52185c0f38911ddd3994f9f99640b"
    )
