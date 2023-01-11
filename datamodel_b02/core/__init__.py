from .analysismodule import AnalysisModule
from .author import Author
from .capillaryconnection import CapillaryConnection
from .dataset import Dataset
from .flowmodule import FlowModule
from .reactionmodule import ReactionModule

__doc__ = "This is the place where you can describe the complete module or dataset and give information about all the details. Markdown offers a convenient way to enable as much space as needed to elucidate purpose and capabilities of your data model."

__all__ = [
    "AnalysisModule",
    "Author",
    "CapillaryConnection",
    "Dataset",
    "FlowModule",
    "ReactionModule",
]
