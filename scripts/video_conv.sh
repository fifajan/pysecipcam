#! /bin/sh

for VID in "$@" ;
do
    ffmpeg -i "$VID" -acodec copy -vcodec mpeg4 -b 5000k "$VID".avi
done
