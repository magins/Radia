---
title: Radia; 3D Magnetostatics Computer Code
---

[Radia] is a fast multiplatform software dedicated to 3D magnetostatics
computation. It is optimized for the design of undulators and wigglers made
with permanent magnets, coils and linear/nonlinear soft magnetic materials.
Radia has been heavily benchmarked with a commercially available finite
element package and with real devices built at the ESRF Insertion Devices
Laboratory.

It also happens to be great for magnet simulations in Magnetic Particle
Imaging. :-)

All work here was done by the ESRF; the original work can be found
[here][original_code].


Compiling
=========

Currently this has only been tested on MacOS Mojave (10.14).


MacOS
-----

1. If you do not have the XCode developer tools installed, run
   `xcode-select --install` to get the command line tools needed to compile
   the project.
1. Activate the python environment you wish to compile to. This can be 
   either the system python or some python version installed in a virtual
   environment.
2. Run `make all`, which will compile both FFTW and the python library.


Running Python
==============

To run the python code, cd into `env/radia_python`. All the functions can be
run locally from there.

Please see the `py-methods.md` for the functions in the python radia module.
Each function has a brief description, but a more detailed description of
most of the functions can be found [reference].

<!-- Links -->
[original_code]: https://github.com/ochubar/Radia
[Radia]: http://www.esrf.eu/Accelerators/Groups/InsertionDevices/Software/Radia/Documentation
[radia]: http://www.esrf.eu/Accelerators/Groups/InsertionDevices/Software/Radia/Documentation
[reference]: http://www.esrf.eu/Accelerators/Groups/InsertionDevices/Software/Radia/Documentation/ReferenceGuide
