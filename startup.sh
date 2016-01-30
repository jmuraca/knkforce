#!/bin/bash

kill -s SIGKILL $(ps axg | grep "[l]ightpulse" | awk '{print $1}')
echo "LED128,128,128;" > /dev/ttyAMA0
python server.py