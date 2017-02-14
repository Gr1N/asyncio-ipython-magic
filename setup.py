# -*- coding: utf-8 -*-

from setuptools import setup

readme = open('README.rst').read()

setup(
    name='asyncio-ipython-magic',
    version='0.0.3',
    description='An extension for IPython that help to run AsyncIO code in '
                'your interactive session.',
    long_description=readme,
    author='Nikita Grishko',
    author_email='gr1n@protonmain.com',
    url='https://github.com/Gr1N/asyncio-ipython-magic',
    py_modules=(
        'asynciomagic',
    ),
    install_requires=(
        'ipython',
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
