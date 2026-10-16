#!/bin/bash
LOG="./ia22_m2m_trace.log"
ts(){ date -u +"%Y-%m-%dT%H:%M:%SZ"; }
trace(){ echo "[IA22TRACE] $(ts) SRC=$1 DST=$2 PAYLOAD=\"$3\"" | tee -a "$LOG"; }
