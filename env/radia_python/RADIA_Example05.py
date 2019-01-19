
#############################################################################
# RADIA Python Example #5: Simple Dipole Magnet
# v 0.01
#############################################################################

from __future__ import absolute_import, division, print_function #Py 2.*/3.* compatibility
import radia as rad
from uti_plot import *
from time import *
from math import *
from array import *

print("""\
RADIA Python Example #5:

This example concerns geometries dominated by iron.

The field computation with Radia in the case of iron dominated geometries
presents a few specific difficulties and is usually less accurate than in
the case of coil or permanent magnet dominated structure. Nevertheless,
special methods have been developed to reach a reasonable precision within a
reasonable CPU time and memory.

The example below is that of a simple dipole steerer made of a closed
circuit of iron with a small gap and a coil wounded around the circuit that
drives some flux in the iron (see the graphics below). This example is more
delicate than all previous examples and we advise the beginner to first get
experienced with them before diving into this one.

Among the most important things to remember if one wants to reach a good
precision in a reasonable time are:

- Always segment the corners of the iron circuits as parallel or perpendicular
  to the flux line as possible. For right angle corners, this can be done
  with the circular or ellipsoidal mode of segmentation (see below). This is
  extremely important.

  In this example, we make use of the circular segmentation twice (the other
  two corners are segmented similarly by symmetry) it is made in the section
  entitled "Defining the Model" when calling

    "rad.ObjDivMag(g3,[nbr,nbp,n3[1]],\'cyl\',typ)" and
    "rad.ObjDivMag(g5,[nbr,nbp,n5[0]],\'cyl\',typ)".

- Use a narrower segmentation on the iron faces close to the region
  of interest.

- Start with low segmentation numbers and increase them gradually to check
  that the field is stable. Beware that the memory and cpu time tends to
  grow like the square number of elements.

- Use symmetries as much as possible. It saves both memory and CPU time.
  The steerer dipole shown below has a symmetry of order 2 x 2. 16 times
  more memory and 4 times more CPU time would have been needed without using
  the symmetries.
""")


#*********************************Geometry
def Geom(circ):

    eps=0
    ironcolor=[0,0.5,1]
    coilcolor=[1,0,0]

    #Pole faces
    lx1=thick/2; ly1=width; lz1=20; l1=[lx1,ly1,lz1]
    k1=[[thick/4-chamfer/2,0,gap/2],[thick/2-chamfer,ly1-2*chamfer]]
    k2=[[thick/4,0,gap/2+chamfer],[thick/2,ly1]]
    k3=[[thick/4,0,gap/2+lz1],[thick/2,ly1]]
    g1=rad.ObjMltExtRtg([k1,k2,k3])
    rad.ObjDivMag(g1,n1)

    #Vertical segment on top of pole faces
    lx2=thick/2;ly2=ly1;lz2=30;l2=[lx2,ly2,lz2]
    p2=[thick/4,0,lz1+gap/2+lz2/2+1*eps]
    g2=rad.ObjRecMag(p2,l2)
    rad.ObjDivMag(g2,n2)

    #Corner
    lx3=thick/2;ly3=ly2;lz3=ly2*1.25;l3=[lx3,ly3,lz3]
    p3=[thick/4,0,lz1+gap/2+lz2+lz3/2+2*eps]
    g3=rad.ObjRecMag(p3,l3)

    typ=[[p3[0],p3[1]+ly3/2,p3[2]-lz3/2],[1,0,0],[p3[0],p3[1]-ly3/2,p3[2]-lz3/2],lz3/ly3]

    if(circ==1): rad.ObjDivMag(g3,[nbr,nbp,n3[1]],'cyl',typ)
    else: rad.ObjDivMag(g3,n3)

    #Horizontal segment between the corners
    lx4=thick/2;ly4=80;lz4=lz3;l4=[lx4,ly4,lz4];p4=[thick/4,ly3/2+eps+ly4/2,p3[2]]
    g4=rad.ObjRecMag(p4,l4)
    rad.ObjDivMag(g4,n4)

    #The other corner
    lx5=thick/2;ly5=lz4*1.25;lz5=lz4;l5=[lx5,ly5,lz5]
    p5=[thick/4,p4[1]+eps+(ly4+ly5)/2,p4[2]]
    g5=rad.ObjRecMag(p5,l5)

    typ=[[p5[0],p5[1]-ly5/2,p5[2]-lz5/2],[1,0,0],[p5[0],p5[1]+ly5/2,p5[2]-lz5/2],lz5/ly5]

    if(circ==1): rad.ObjDivMag(g5,[nbr,nbp,n5[0]],'cyl',typ)
    else: rad.ObjDivMag(g5,n5)

    #Vertical segment inside the coil
    lx6=thick/2;ly6=ly5;lz6=gap/2+lz1+lz2;l6=[lx6,ly6,lz6]
    p6=[thick/4,p5[1],p5[2]-(lz6+lz5)/2-eps]
    g6=rad.ObjRecMag(p6,l6)
    rad.ObjDivMag(g6,n6)

    #Generation of the coil
    Rmin=5;Rmax=40;Nseg=4;H=2*lz6-5
    CurDens=current/H/(Rmax-Rmin)
    pc=[0,p6[1],0]
    coil=rad.ObjRaceTrk(pc,[Rmin,Rmax],[thick,ly6],H,3,CurDens)
    rad.ObjDrwAtr(coil,coilcolor)

    #Make container and set the colors
    g=rad.ObjCnt([g1,g2,g3,g4,g5,g6])
    rad.ObjDrwAtr(g,ironcolor)
    rad.MatApl(g,ironmat)
    t=rad.ObjCnt([g,coil])

    #Define the symmetries
    rad.TrfZerPerp(g,[0,0,0],[1,0,0])
    rad.TrfZerPara(g,[0,0,0],[0,0,1])
    return t

#*********************************Entry point
if __name__=="__main__":

    #Geometry Parameters
    gap=10 #(mm)
    thick=50
    width=40
    chamfer=8 #(mm)
    current=-2000 #(A)

    #Segmentation Parameters
    nx=2
    nbp=2; nbr=2 #for corners
    n1=[nx,3,2] #pole faces
    n2=[nx,2,2] #small vertical arm
    n3=[nx,2,2]
    n4=[nx,2,2] #horizontal arm
    n5=[nx,2,2]
    n6=[nx,2,2] #inside the coil

    #Build the geometry
    t0=time()
    rad.UtiDelAll()
    ironmat=rad.MatSatIsoFrm([20000,2],[0.1,2],[0.1,2])
    t = Geom(1)
    size=rad.ObjDegFre(t)

    #Display the geometry
    rad.ObjDrwOpenGL(t)

    #Solve the geometry
    t1=time()
    res=rad.Solve(t,0.0001,1500)
    t2=time()

    #Print the results
    b0=rad.Fld(t,'Bz',[0,0,0])
    bampere=(-4*pi*current/gap)/10000
    r=b0/bampere

    print('Solving results for the segmentation by elliptical cylinders in the corners:')
    print('Mag_Max  H_Max  N_Iter =', round(res[1], 5), 'T ', round(res[2], 5), 'T ', round(res[3]))
    print('Built & Solved in', round(t1-t0, 2), '&', round(t2-t1, 2), 'seconds')
    print('Interaction Matrix :', size, 'X', size, 'or', round(size*size*4/1000000, 3), 'MBytes')
    print('Bz =', round(b0, 4), 'T,   Bz Computed / Bz Ampere Law =', round(r, 4))

    #Calculate magnetic field after the solving, and plot of the results
    t1=time()
    z=1;rmax=30;np=40
    rstep=2*rmax/(np-1)
    BzVsXY = rad.Fld(t, 'bz', [[-rmax+ix*rstep,-rmax+iy*rstep,z] for iy in range(np) for ix in range(np)])

    uti_plot2d1d(BzVsXY, [-rmax,rmax,np], [-rmax,rmax,np], x=0, y=0,
                 labels=('X', 'Y', 'Bz in Magnet Gap at Z = ' + repr(z) + ' mm'), units=['mm','mm','T'])
    
    z=3
    IBzVsY = [rad.FldInt(t, 'inf', 'ibz', [-1,-rmax+iy*rstep,z], [1,-rmax+iy*rstep,z]) for iy in range(np)]
    print('Field calculation after solving (post-processing) done in', round(t1-t0, 2), 'seconds')

    uti_plot1d(IBzVsY, [-rmax,rmax,np],
               ['Y', 'Vertical Field Integral', 'Vertical Field Integral along X at Z = ' + repr(z) + ' mm'], ['mm', 'T'])

    print('')
    print('Close all magnetic field graphs to continue this example.')
    uti_plot_show() #show all graphs (and block further execution, if any)

    #Creating the Model and Solving with Rectangular Segmentation in the Corners
    t = Geom(0)
    rad.ObjDrwOpenGL(t)

    t1=time()
    res=rad.Solve(t,0.0001,1500)
    t2=time()

    b0=rad.Fld(t,'Bz',[0,0,0])
    bampere=(-4*pi*current/gap)/10000
    r=b0/bampere

    print('')
    print('Solving results for the rectangular segmentation in the corners:')
    print('Mag_Max  H_Max  N_Iter =', round(res[1], 5), 'T ', round(res[2], 5), 'T ', round(res[3]))
    print('Built & Solved in', round(t1-t0, 2), '&', round(t2-t1, 2), 'seconds')
    print('Bz =', round(b0, 4), 'T,   Bz Computed / Bz Ampere Law =', round(r, 4))
    print('')
    print('Segmenting iron corners into parallellepipeds should be avoided. Instead, one should use a circular or ellipsoidal segmentation, or triangulation.')
