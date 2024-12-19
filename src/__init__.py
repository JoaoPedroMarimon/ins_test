"""
The __init__.py file contains only the methods and variables the main.py file located at root will be using.
"""

from .environment import (DEFAULT_CONFIGFILE, CONFIGFILE_PATHNAME,
                          PAD_INSPECT_TIMEOUT)


from .IHM.interface import Interface
from .IHM.ihm import IHM
#from .inspection_designer.inspection_designer.inspection import PadInspection
#from .interface import Interface
from .inspection_designer.inspection_designer.inspection import TemplateInspection
from .logger import init_logging
#from .messenger.messenger import QueueMessenger
from .parser import main_parse, execute_parse, get_product_from_configfile
from .serial_connection import SerialController

from .utils import (get_port_connection, get_all_ports,
                    load_json_configfile, get_rtsp_url,
                    ThreadedVideoCapture,
                    try_camera_connection)