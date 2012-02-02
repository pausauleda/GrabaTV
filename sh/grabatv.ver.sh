#! /bin/bash
pgrep mencoder
RESULTADO=$?
if [ $RESULTADO -eq 0 ]; then
   exit 1
fi
pgrep mplayer
RESULTADO=$?
if [ $RESULTADO -eq 0 ]; then
   exit 2
fi
mplayer -tv driver=v4l2:input=1:width=768:height=576:device=/dev/video0:alsa:adevice=hw.2:immediatemode=0:audiorate=48000 tv:// &
