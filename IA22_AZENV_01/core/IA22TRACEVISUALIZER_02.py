#!/usr/bin/env python3
import os
f="ia22_m2m_trace.log"
if not os.path.exists(f): exit()
for l in open(f):
    p=l.strip().split()
    if len(p)<5: continue
    print("[IA22VIS]",p[1],p[2].split("=")[1],"->",p[3].split("=")[1],"::",p[4].split("=")[1].strip('"'))
