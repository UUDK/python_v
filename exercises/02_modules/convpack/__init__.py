# Convert the module to a package with the three conversions
# in separate files

from .temp import c2f, f2c
from .fluid import l2g, g2l
from .length import m2i, i2m

__all__ = ["f2c", "c2f", "l2g", "g2l", "m2i", "i2m"]
