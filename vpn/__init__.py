# from vpn.base import VPN
# from vpn.desktop import Desktop
# from vpn.webbased import WebBased
# from vpn.cisco import Cisco
# from vpn.forticlient import FortiClient
# from vpn.openvpn import OpenVPN
# from vpn.pulse import Pulse
# from vpn.checkpoint import CheckPoint
# # from vpn.barracuda import Barracuda
#

# from vpn.base import model
#
# print(model)

# from vpn.controllers import VPN
# from vpn.controllers import Desktop

from vpn.base import VPN
from vpn.desktop.controller import Desktop
from vpn.webbased.controller import Webbased
from vpn.cisco import Cisco
from vpn.openvpn import OpenVPN
from vpn.barracuda3 import Barracuda3
from vpn.barracuda5 import Barracuda5
from vpn.forticlient import FortiClient
from vpn.checkpoint import Checkpoint

