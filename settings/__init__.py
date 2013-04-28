# -*- coding: utf-8 -*-

import socket
from settings.private_config import *

HOSTNAME = socket.gethostname()
if HOSTNAME == PUBLIC_HOSTNAME:
    from settings.base_settings import *
else:
    # local環境
    from settings.dev_settings import *
