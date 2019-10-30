"""confdaora"""

__version__ = '0.0.1'

from confdaora.confdaora import from_env
from confdaora.exceptions import ValidationError


__all__ = [from_env.__name__, ValidationError.__name__]
