from .base import *
try:
    from .stackato import *
except ImportError, exc:
    exc.args = tuple(['%s (did you rename settings/local.py-dist?)' % exc.args[0]])
    raise exc
