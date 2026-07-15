#!/bin/bash

pkill -f chromium 2>/dev/null

sleep 1

chromium \
  --kiosk \
  --disable-infobars \
  --noerrdialogs \
  --disable-session-crashed-bubble \
  --autoplay-policy=no-user-gesture-required \
  --start-fullscreen \
  "file:///home/frost/weather-channel/launch.html"
