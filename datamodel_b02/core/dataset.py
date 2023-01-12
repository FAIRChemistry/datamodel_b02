import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .author import Author
from .processscheme import ProcessScheme


@forge_signature
class Dataset(sdRDM.DataModel):
    """This is the root of the data model and contains all objects defined in this example. While its good practice to have a single root, you can define as many roots as you like. Furthermore, the name does not have to be ```Root``` and can be any other name.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    title: str = Field(..., description="title of the work.")

    description: str = Field(..., description="describes the content of the dataset.")

    authors: List[Author] = Field(
        description="authors of this dataset.", default_factory=ListPlus
    )

    process_scheme: Optional[ProcessScheme] = Field(
        description="PandID like setup scheme of the reactor.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8ad9c293393d92336f63257326745c6bc4db3b6b"
    )

    def add_to_authors(
        self, name: str, affiliation: Optional[str] = None, id: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:


            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.


            name (str): full name including given and family name.


            affiliation (Optional[str]): to which organization the author is affiliated to. Defaults to None
        """

        params = {"name": name, "affiliation": affiliation}
        if id is not None:
            params["id"] = id
        authors = [Author(**params)]
        self.authors = self.authors + authors
