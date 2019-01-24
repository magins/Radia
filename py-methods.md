Methods exported to Python from the C++ shared object. We should be able to use
more by just adding them to the list?

Methods matching the Mathematica Documentation
==============================================

Field Sources
-------------

- ObjRecCur: creates a current carrying rectangular parallelepiped block
- ObjArcCur: creates a current carrying finite-length arc of rectangular cross-section
- ObjRaceTrk: instantiates Recetrack conductor with rectangular cross-secton and constant current density over the volume
- ObjFlmCur: creates a filament polygonal line conductor with current
- ObjRecMag: instantiates Rectangular Parallelepiped with Constant Magnetizatiom over volume
- ObjThckPgn: instantiates a uniformly magnetized extruded polygon
- ObjPolyhdr: creates a uniformly magnetized polyhedron (closed volume limited by planes)
- ObjArcPgnMag: creates a uniformly magnetized finite-length arc of polygonal cross-section
- ObjMltExtPgn: attempts to create one uniformly magnetized convex polyhedron or a set of convex polyhedrons based on slices.
- ObjMltExtRtg: attempts to create one uniformly magnetized convex polyhedron or a set of convex polyhedrons based on rectangular slices
- ObjM: provides coordinates of geometrical center point(s) and magnetization(s) of an object
- ObjBckg: creates a source of uniform background magnetic field
- ObjCnt: instantiates Container of Magnetic Field Sources
- ObjAddToCnt: adds objects to the container object
- ObjCntStuf: returns list with the reference numbers of objects present in container
- ObjDivMag: subdivides (segments) a 3D object obj by sets of parallel planes or coaxial elliptical cylinders
- ObjCutMag: cuts 3D object by a plane passing through a given point normally to a given vector
- ObjDpl: duplicates 3D object
- ObjDegFre: gives number of degrees of freedom for the relaxation of an object
- ObjDrwAtr: assigns drawing attributes - RGB color (r,g,b) and line thickness thcn - to a Magnetic Field Source object
- ObjDrwOpenGL: assigns drawing attributes - RGB color (r,g,b) and line thickness thcn - to a Magnetic Field Source object


Object creation/probing
-----------------------

- ObjMltExtTri: creates triangulated extruded polygon block, i.e. an extruded polygon with its bases subdivided by triangulation
- ObjCylMag: creates a cylindrical magnet
- ObjFullMag: instantiates Rectangular Parallelepiped with Constant Magnetizatiom over volume, subdivided, and added to a group, with some color assigned
- ObjScaleCur: scales current (density) in a 3D object by multiplying it by a constant
- ObjCntSize: calculates the number of objects in the container
- ObjCenFld: provides coordinates of geometrical center point and field at that point
- ObjSetM: sets magnetization of an object

- ObjDivMagPln: subdivides (segments) a 3D object by 3 sets of parallel planes
- ObjDivMagCyl: subdivides (segments) a 3D object obj by a set of coaxial elliptical cylinders
- ObjGeoVol: computes geometrical volume of a 3D object
- ObjGeoLim: computes coordinates of object extrimities in laboratory frame


Magnetic Materials
------------------

- MatApl: applies magnetic material to a 3D object
- MatLin: creates a linear anisotropic magnetic material.
- MatStd: creates a pre-defined magnetic material (the material is identified by its name/formula, e.g. \"NdFeB\")
- MatSatIsoFrm: creates a nonlinear isotropic magnetic material with the M versus H curve defined by the formula M = ms1*tanh(ksi1*H/ms1) + ms2*tanh(ksi2*H/ms2) + ms3*tanh(ksi3*H/ms3), where H is the magnitude of the magnetic field strength vector (in Tesla)
- MatSatIsoTab: creates a nonlinear isotropic magnetic material with the M versus H curve defined by the list of pairs corresponding values of H and M [[H1,M1],[H2,M2],...]
- MatMvsH: computes magnetization from magnetic field strength vector for a given material


Space Transformations
---------------------

- TrfPlSym: creates a symmetry with respect to plane defined by a point and a normal vector
- TrfRot: creates a rotation about an axis
- TrfTrsl: creates a translation
- TrfInv: creates a field inversion
- TrfCmbL: multiplies original space transformation by another transformation from left
- TrfCmbR: multiplies original space transformation by another transformation from right
- TrfMlt: creates mlt-1 symmetry objects of a 3D object
- TrfOrnt: orients 3D object by applying a space transformation to it once
- TrfZerPara: creates an object mirror with respect to a plane. The object mirror possesses the same geometry as obj, but its magnetization and/or current densities are modified in such a way that the magnetic field produced by the obj and its mirror in the plane of mirroring is perpendicular to this plane
- TrfZerPerp: creates an object mirror with respect to a plane. The object mirror possesses the same geometry as obj, but its magnetization and/or current densities are modified in such a way that the magnetic field produced by the obj and its mirror in the plane of mirroring is parallel to this plane


Field Computation
-----------------

- RlxPre: builds interaction matrix for an object
- RlxMan: executes manual relaxation procedure on a given interaction matrix
- RlxAuto: executes automatic relaxation procedure on a given interaction matrix
- Fld: computes field created by the object obj at one or many points
- FldPrcCmp: Sets the precision for field calculations
- FldEnr: Calculates the energy in an object caused by a source of a magnetic field.
- FldEnrFrc: Calculates the force on an object caused by a source of a magnetic field. 
- FldInt: computes magnetic field integral produced by magnetic field source object along a straight line



Solvers
-------

- Solve: solves a magnetostatic problem, i.e. builds an interaction matrix and performs a relaxation procedure


Utility functions
-----------------

- UtiDmp: outputs information (in bnary or in ASCII format) about an object or list of objects
- UtiDmpPrs: parses byte-string produced previously by UtiDmp(elem,\"bin\") and attempts to instantiate objects(s) identical to elem
- UtiDel: deletes an object
- UtiDelAll: deletes all previously created objects
