# travel_blog
Travel blog source for my upcoming sabbatical.


# Notes

## Videos

Use ffmpeg as in [here](https://trac.ffmpeg.org/wiki/Encode/VP8).

See also this [cheat sheet](http://rodrigopolo.com/ffmpeg/cheats.php).
```
ffmpeg -i input.mp4 -s 1280x720 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output.webm
```
