# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'moava',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = moava.settings']},
)
