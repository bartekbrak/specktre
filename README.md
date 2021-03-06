# Specktre

Specktre is a tool for generating low-contrast desktop wallpapers from tiling patterns.  Here are some examples of the sort of pattern it produces:

![](output/demo.png)

It can be used as a Python library, or invoked from the command-line.

## What's in the repo?

The most interesting parts are in these files:

*   `tilings.py` -- draw regular tilings of the plane with Pillow.
*   `colors.py` -- a generator of random colour shades.
*   `specktre.py` -- a bit of drawing code (and lots of argument parsing code) that ties both files together, and presents a command-line tool for using them.

These files contain the core drawing logic, and are the most carefully written and reviewed parts of the repo.

The `flaskapp` folder contains some hacked-together code used to serve the live demo.
I'll clean it up at some point, but there's probably nothing very interesting in that folder.

## What’s in the name?

The word "speckled" came to mind when describing this pattern, and I wrote the first version shortly after the James Bond film *SPECTRE* had been released.

## Installation

Clone this repository, or [download the ZIP][zip]:

```console
$ git clone git@github.com:alexwlchan/specktre.git
```

You need to have Python installed (should work in 2.7 or 3.3+), then you need to install the two Python dependencies, which are [Pillow][pillow] and [docopt][docopt].
I recommend using a virtualenv:

```console
$ cd specktre
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

There's also a Flask app you can use, if you prefer a graphical interface.
You need to install some extra dependencies:

```console
$ pip install -r flask_requirements.txt
```

[zip]: https://github.com/alexwlchan/specktre/archive/master.zip
[pillow]: https://github.com/python-pillow/Pillow
[docopt]: https://github.com/docopt/docopt

## Usage

The file `specktre.py` is the main runner.  To see a help message:

```console
$ python specktre.py --help
```

The three demo images were generated as follows:

```console
$ python specktre.py --size=400x400 --start=178,26,16 --end=136,25,17 --squares --name='demo_sq.png'
Saved new wallpaper as demo_sq.png

$ python specktre.py --size=400x400 --start=255,204,0 --end=255,238,56 --triangles --name='demo_tr.png'
Saved new wallpaper as demo_tr.png

$ python specktre.py --size=400x400 --start=56,56,255 --end=0,0,194 --hexagons --name='demo_hex.png'
Saved new wallpaper as demo_hex.png
```

The `--start` and `--end` arguments indicate the colours that will be used to generate the pattern.
It's a tuple of R,G,B colours.
I recommend [HSL Picker][picker] as a free tool for finding RGB colour sets you like.

Alternatively, you can use the Flask app:

```console
$ python manage.py
```

and use it at <http://localhost:7007> in your browser.

The images are randomly generated, so each run will create a new pattern of colours.

[picker]: http://hslpicker.com

## License

The code is licensed under the MIT license.
