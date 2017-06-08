import os
from setuptools import setup

setup(
    name = "tornadoist2",
    version = "0.2.1",
    author = "Eren G\xc3\xbcven, Yalei Du",
    author_email = "erenguven0@gmail.com",
    description = "mixins for tornado",
    license = "Apache License, Version 2",
    keywords = ["tornado", "celery"],
    url = "https://github.com/badbye/tornadoist.git",
    packages = ['tornadoist2',],
    long_description = open("README.rst").read(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
)
