#!/usr/bin/env python3
import os
log="ia22_m2m_trace.log"; out="security/ICE_SHIELD_EVENTS.log"
if os.path.exists(log):
    a=[l for l in open(log) if "ANOMALY" in l or "ALERT" in l]
    open(out,"a").writelines(a)
