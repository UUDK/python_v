# Convert the module to a package with the three conversions
# in separate files

from .temp import f2c, c2f
from .fluid import g2l, l2g
from .length import m2i, i2m

__all__ = ["f2c", "c2f", "g2l", "l2g", "m2i", "i2m"]
