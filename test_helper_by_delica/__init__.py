from .test_helper_funcs import test_bool_func
from .IOPair import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("test_helper_by_delica")
except PackageNotFoundError:
    pass

__all__ = ["test_bool_func", "IOPair"]
