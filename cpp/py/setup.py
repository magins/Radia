from textwrap import dedent
import os

from setuptools import setup, Extension, find_packages

def to_abs_path(*args):
    return [os.path.abspath(p) for p in args]

_radia = Extension(
    '_radia',
    define_macros=[('MAJOR_VERSION', '1'), ('MINOR_VERSION', '0')],
    include_dirs=to_abs_path(
        '../src/lib',
        '../src/ext/auxparse'
    ),
    library_dirs=to_abs_path(
        '../gcc',
        '../../ext_lib'
    ),
    libraries=['radia', 'm', 'fftw'],
    sources=to_abs_path('../src/clients/python/radpy.cpp'))

setup(name='radia',
    version='0.1.0',
    description='Magnetostatics Simulation Software',
    author='O. Chubar, P. Elleaume, J. Chavanne',
    author_email='chubar@bnl.gov',
    url='http://github.com/ochubar/Radia',
    long_description=dedent(
        '''\
        Magnetostatics simulation software.

        This is a fork of the original work by O. Chubar, P. Elleaume, and
        J. Chavanne that exports more functionality into the Python wrapped
        version of Radia. Additionality this variant wraps up some of the
        returned C data types into Python classes to assist with memory
        management.
        '''),
    ext_modules=[_radia],
    packages=find_packages(),
    classifiers=[
        'Topic :: Scientific/Engineering :: Physics',
        'Intended Audience :: Science/Research',
    ],
    )
