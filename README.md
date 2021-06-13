This is a fork of [playsound](https://github.com/TaylorSMarks/playsound) that I will try to maintain. I forked this repo from https://github.com/driedler/playsound, a fork of https://github.com/TaylorSMarks/playsound that fixed a memory leak for Windows. 

playsoundv2
=========
*Pure Python, cross platform, single function module with no dependencies for playing sounds.*

Installation
============
Install via pip:

```
$ pip install playsound
```

Done.

If you insist on the (slightly) harder way of installing, from source, you know how to do it already and don't need my help.

The latest version of the source code can be found at:
https://github.com/kethan1/playsoundv2

Quick Start
===========
Once you've installed, you can really quickly verified that it works with just this:

```
>>> from playsound import playsound
>>> playsound('/path/to/a/sound/file/you/want/to/play.mp3')
```

Documentation
=============
The playsound module contains only one thing - the function (also named) playsound.

It requires one argument - the path to the file with the sound you'd like to play. This may be a local file, or a URL.

There's an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.

On Windows, uses windll.winmm. WAVE and MP3 have been tested and are known to work. Other file formats may work as well.

On OS X, uses AppKit.NSSound. WAVE and MP3 have been tested and are known to work. In general, anything QuickTime can play, playsound should be able to play, for OS X.

On Linux, uses GStreamer. Known to work on Ubuntu 14.04 and ElementaryOS
Loki. Support for the `block` argument is currently not implemented.

Requirements
============
I have only tested this module on Windows 10 with Python 3.8 and Python 3.9, though it should work with other OSes and versions. 

If you are getting this error on Linux:
```
ImportError: No module named 'gi'
```
Then run the below commands:
```
sudo apt install python3-gi
pip3 install vext
pip3 install vext.gi
```

Copyright
=========
Original software is Copyright (c) 2016 Taylor Marks <taylor@marksfam.com>.
Modified software is Copyright (c) 2021 Kethan Vegunta <kethan@vegunta.com>. 

See the bundled LICENSE file for more information.
