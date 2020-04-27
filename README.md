# travel_blog
Travel blog source for my upcoming sabbatical.

# How to build this blog

## Clone the source

```shell
git clone https://github.com/flothesof/travel_blog.git
```

## Install dependencies

I think at least this:
```shell
pip install "pelican<4" markdown piexif pillow
```

## Build the blog

Either in local editing mode:

```shell
pelican -s pelicanconf.py
```

Or in publishing mode (with all the links pointing to the full website URLs):

```shell
pelican -s publishconf.py
```
## Serving the content for previewing locally

The result can be served by a HTTP server from the `output` directory.

In debug mode, I use this with Python > 3:

```shell
python -m http.server --directory output
```

# Notes

## Videos

Use ffmpeg as in [here](https://trac.ffmpeg.org/wiki/Encode/VP8).

See also this [cheat sheet](http://rodrigopolo.com/ffmpeg/cheats.php).

Here's my goto encoding:
```
ffmpeg -i input.mp4 -s 1280x720 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output.webm
```
