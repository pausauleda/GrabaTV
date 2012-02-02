#! /bin/bash
TIMESTAMP=`date '+%y.%m.%d-%H.%M.%S'`
pgrep mencoder
RESULTADO=$?
if [ $RESULTADO -eq 0 ]; then
   exit 1
fi
pgrep mplayer
RESULTADO=$?
if [ $RESULTADO -eq 0 ]; then
   killall mplayer
   sleep 3
fi
mencoder -tv driver=v4l2:input=1:width=768:height=576:device=/dev/video0:alsa:adevice=hw.2:audiorate=48000 -oac pcm -ovc lavc -lavcopts vcodec=mjpeg -o ~/Desktop/digital.$TIMESTAMP.avi tv:// &
