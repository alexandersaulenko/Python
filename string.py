import re


msg = r"""Standard Out: "Image Name","PID","Session Name","Session#","Mem Usage","User Name","CPU Time"
"System","4","Services","0","304 K","N/A","0:00:59"
"taskhost.exe","2480","RDP-Tcp#0","2","7ÿ796 K","IBMRCIS\asaulenko","0:00:00"
"rdpclip.exe","1220","RDP-Tcp#0","2","6ÿ004 K","IBMRCIS\asaulenko","0:00:00"
"dwm.exe","2164","RDP-Tcp#0","2","5ÿ240 K","IBMRCIS\asaulenko","0:00:00"
"explorer.exe","2872","RDP-Tcp#0","2","46ÿ160 K","IBMRCIS\asaulenko","0:00:04"
"vmtoolsd.exe","2896","RDP-Tcp#0","2","10ÿ204 K","IBMRCIS\asaulenko","0:14:09"
"calc.exe","2500","RDP-Tcp#0","2","11ÿ740 K","IBMRCIS\asaulenko","0:00:00"
"slui.exe","1020","RDP-Tcp#0","2","8ÿ556 K","IBMRCIS\asaulenko","0:00:00"
"""

x = msg.split('\n')

print(x[0])

