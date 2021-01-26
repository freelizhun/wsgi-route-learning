#!/bin/bash
# usage
# ./start_service.sh debug
MODE=$1
if [ -z "$1" ]; then
    echo "default mode set to: debug"
    MODE="debug"
fi
python2 ps_launcher.py --mode $MODE
