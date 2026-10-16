#!/usr/bin/env python3
import subprocess, time
T="./core/IA22TRACEM2M01.sh"
def pulse(a,b,c): subprocess.call([T,a,b,c])
for a,b,c in [("ORBITRON.IA","IA22_BIN","PULSE:BOOT"),
              ("IA22_BIN","IA22TRACEVISUALIZER_02","SYNC:INIT"),
              ("ICE_SHIELD","IA22_BIN","STATE:SAFE")]:
    pulse(a,b,c); time.sleep(0.3)
