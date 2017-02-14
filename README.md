# asyncio-ipython-magic [![Requirements Status](https://requires.io/github/Gr1N/asyncio-ipython-magic/requirements.svg?branch=master)](https://requires.io/github/Gr1N/asyncio-ipython-magic/requirements/?branch=master) [![PyPI](https://img.shields.io/pypi/v/asyncio-ipython-magic.svg)](https://pypi.python.org/pypi/asyncio-ipython-magic) [![Supported Python versions](https://img.shields.io/pypi/pyversions/asyncio-ipython-magic.svg)](https://pypi.python.org/pypi/asyncio-ipython-magic)

An extension for [IPython](https://ipython.org) that help to run AsyncIO code in your interactive session.

Based on [Gist](https://gist.github.com/takluyver/b9663b08ac9a4472afa6).

## Installation

Install `asyncio-ipython-magic` using [pip](http://www.pip-installer.org/):

    $ pip install asyncio-ipython-magic

...or directly from the repository using the `%install_ext` magic command:

    $ In[1]: %install_ext https://raw.githubusercontent.com/Gr1N/asyncio-ipython-magic/master/asynciomagic.py

Enjoy!

## Usage

    In [1]: %load_ext asynciomagic

    In [2]: import asyncio

    In [3]: import time

    In [4]: async def foo():
       ...:     i = 0
       ...:     while i < 3:
       ...:         print('time =', time.time())
       ...:         i += 1
       ...:         await asyncio.sleep(2)
       ...:

    In [5]: %%async_
       ...: await foo()
       ...:
    time = 1478985421.307329
    time = 1478985423.309606
    time = 1478985425.31514

    In [6]: %await_ foo()
    time = 1487097377.700184
    time = 1487097379.705614
    time = 1487097381.707186

    In [7]:

## Testing

It just works, I hope.

## License

*asyncio-ipython-magic* is licensed under the MIT license. See the license file for details.
