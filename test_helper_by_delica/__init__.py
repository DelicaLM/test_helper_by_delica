from .test_helper_funcs import *
from .IOPair import *
from .test_data_generators import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("test_helper_by_delica")
except PackageNotFoundError:
    pass

__all__ = ["test_helper_funcs", "IOPair", "test_data_generators"]
