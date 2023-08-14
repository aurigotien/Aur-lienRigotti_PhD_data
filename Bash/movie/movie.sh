#!/bin/bash
# Script to make an mp4 movie from png pictures 
# Input : -root : shared in all the picture filenames (defaults : 'png')
# Optional : - name : name of the resulting movie (default : movie.mp4)
# 	     - fps number of frames per seconds (default : 4)

# beggin

if [$# -gt 1]; then
	name=$2
else 
	name=movie
fi 

if [$# -gt 2]; then 
	echo 'FPS is set to ' $fps
else 
	fps=10
fi 

ffmpeg -framerate $fps -pattern_type glob -i "*$1*.jpg" -c:v libx264 -crf 24 -pix_fmt yuv420p -tune film -c:a aac -b:a 192k -ar 44100 -vol 300 -strict -2 -speed fastest $name.mp4

# end 
