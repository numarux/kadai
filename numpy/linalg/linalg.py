import warnings
from numpy.linalg import _linalg

def __getattr__(name):
    try:
        return getattr(_linalg, name)
    except AttributeError:
        raise AttributeError(f"module 'numpy.linalg' has no attribute '{name}'")
    warnings.warn(
        "The numpy.linalg.linalg has been made private and renamed to "
        "numpy.linalg._linalg. All public functions exported by it are "
        f"available from numpy.linalg. Please use numpy.linalg.{name} "
        "instead.",
        DeprecationWarning,
        stacklevel=2
    )

# Assign the __getattr__ function to the numpy.linalg module
import numpy.linalg as linalg
linalg.__getattr__ = __getattr__

