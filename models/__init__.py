from .AMIO import AMIO
from .DARIA import DARIA

from importlib import import_module as _import_module
import sys as _sys
from types import ModuleType as _ModuleType

# Compatibility exports for historical callers and serialized classes.
CRIU = DARIA
ARG_MSA = DARIA

# Historical pickle/import paths without retaining old implementation filenames.
_implementation = _import_module('.DARIA', package=__name__)


def _legacy_attribute(name):
    if name in {'CRIU', 'ARG_MSA'}:
        return DARIA
    return getattr(_implementation, name)


for _legacy_name in ('CRIU', 'ARG_MSA'):
    _legacy_module = _ModuleType(f'{__name__}.{_legacy_name}')
    _legacy_module.__getattr__ = _legacy_attribute
    _legacy_module.__all__ = ['DARIA', 'CRIU', 'ARG_MSA']
    _sys.modules.setdefault(_legacy_module.__name__, _legacy_module)
