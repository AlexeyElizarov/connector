from vpn import Cisco, FortiClient, OpenVPN, Barracuda3, Barracuda5, Checkpoint

# # from vpn import Cisco, FortiClient, OpenVPN, Pulse, CheckPoint, Barracuda
#
VPN = {'cisco': Cisco,
       'forticlient': FortiClient,
       'openvpn': OpenVPN,
       # 'pulse': Pulse,
       'checkpoint': Checkpoint,
       'barracuda3': Barracuda3,
       'barracuda5': Barracuda5}