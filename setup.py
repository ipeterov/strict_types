"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='strict',
    version='1.0.0',
    description="Decorator that implements strict typing using type-hints.",
    long_description=long_description,
    url='https://github.com/ipeterov/strict_types',
    author='Ilya Peterov',
    author_email='ipeterov@gmail.com',
    license='MIT',
    keywords='strict-typing',
    py_modules=['strict_typing'],
)
