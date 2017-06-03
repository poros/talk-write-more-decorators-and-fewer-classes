from enum import Enum

Color = Enum("Color", ("RED", "GREEN", "BLUE"))

>>> print(repr(Color.RED))
<Color.RED: 1>
