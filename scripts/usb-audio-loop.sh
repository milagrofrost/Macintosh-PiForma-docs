#!/bin/bash

SOURCE="alsa_input.usb-C-Media_Electronics_Inc._Cable_Creation-00.mono-fallback"

while true
do
    if pactl list short sources | grep -q "$SOURCE"; then

        if ! pgrep -f "$SOURCE" >/dev/null; then
            pactl set-source-volume alsa_input.usb-C-Media_Electronics_Inc._Cable_Creation-00.mono-fallback 50%
            pw-loopback --capture="$SOURCE" &
        fi

    fi

    sleep 5
done
