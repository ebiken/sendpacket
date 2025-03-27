from scapy.all import *
from scapy.contrib.mac_control import *
import sys

frm = Ether(src='00:01:01:01:01:01', dst=MACControl.DEFAULT_DST_MAC)/ \
      MACControlClassBasedFlowControl(c3_enabled=1, c3_pause_time=0xffff)

if len(sys.argv) < 2:
  print("Usage: python3 pfc_gen.py <interface> [number of packets to send]")
  sys.exit(1)
else:
  interface = sys.argv[1]

if len(sys.argv) < 3:
  num = 1
else:
  num = sys.argv[2]

print(f"sending {num} packets to {interface}")

sendp(frm,iface=interface, count=int(num))

### To send faster ###
# prerequisit: sudo apt install tcpreplay
#
#sendpfast(frm,iface=interface, pps=9999999, loop=int(num))
