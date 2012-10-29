# pylint: disable = E0611,F0401
from distutils.version import StrictVersion as SV
# pylint: enable = E0611,F0401
import sys

import pykka


if not (2, 6) <= sys.version_info < (3,):
    sys.exit(
        u'Mopidy requires Python >= 2.6, < 3, but found %s' %
        '.'.join(map(str, sys.version_info[:3])))

if (isinstance(pykka.__version__, basestring)
        and not SV('1.0') <= SV(pykka.__version__) < SV('2.0')):
    sys.exit(
        u'Mopidy requires Pykka >= 1.0, < 2, but found %s' % pykka.__version__)


__version__ = '0.8.0'


from mopidy import settings as default_settings_module
from mopidy.utils.settings import SettingsProxy
settings = SettingsProxy(default_settings_module)
