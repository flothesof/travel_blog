# travel_blog
Travel blog source for my upcoming sabbatical.

# How to build this blog

## Install dependencies

I think at least this:
```shell
pip install pelican piexif PIL
```

## Build the blog

Either in debug mode:

```shell
pelican -s pelicanconf.py
```

Or in publishing mode (with all the right URLs):

```shell
pelican -s publishconf.py
```

The result can then be served by a HTTP server from the `output` directory.

In debug mode, I use this with Python > 3:

```shell
cd output
python -m http.server
```


# Notes

## Videos

Use ffmpeg as in [here](https://trac.ffmpeg.org/wiki/Encode/VP8).

See also this [cheat sheet](http://rodrigopolo.com/ffmpeg/cheats.php).

Here's my goto encoding:
```
ffmpeg -i input.mp4 -s 1280x720 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output.webm
```
