#!/bin/sh
  /usr/bin/python /home/pi/pypadnu/src/pypadnu.py
  rm -f /etc/profile.d/pypadnu.sh
  exec login -f pi
