# This file was automatically created by FeynRules 1.7.221
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 7 Oct 2013 12:36:37

from object_library import all_CTvertices, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L

V_2_Sgg_R2 = CTVertex(name = 'V_2_Sgg_R2',
                      type = 'R2',
                      particles = [ P.g, P.g, P.S__tilde__ ],
                      color = [ 'Identity(1,2)' ],
                      lorentz = [ L.VVS1 ],
                      loop_particles = [ [ [P.Y] ] ],
                      couplings = {(0,0,0):C.R2GC_Sgg})

V_2_SYY_R2 = CTVertex(name = 'V_2_SYY_R2',
                      type = 'R2',
                      particles = [ P.Y__tilde__, P.Y, P.S__tilde__ ],
                      color = [ 'Identity(1,2)' ],
                      lorentz = [ L.FFS2 ],
                      loop_particles = [ [ [P.g, P.Y] ] ],
                      couplings = {(0,0,0):C.R2GC_SYY})

V_2_Sgg_UV = CTVertex(name = 'V_2_Sgg_UV',
                      type = 'R2',
                      particles = [ P.Y__tilde__, P.Y ],
                      color = [ 'Identity(1,2)' ],
                      lorentz = [ L.FF1 ],
                      loop_particles = [ [ [P.g, P.Y] ] ],
                      couplings = {(0,0,0):C.UVGC_Sgg})

V_2_SYY_UV = CTVertex(name = 'V_2_SYY_UV',
                      type = 'UV',
                      particles = [P.Y__tilde__, P.Y, P.S__tilde__ ],
                      color = [ 'Identity(1,2)' ],
                      lorentz = [ L.FFS2 ],
                      loop_particles = [ [ [P.g, P.Y] ] ],
                      couplings = {(0,0,0):C.UVGC_SYY})

V_2_YYg_UV = CTVertex(name = 'V_2_YYg_UV',
                      type = 'R2',
                      particles = [ P.Y__tilde__, P.Y, P.g ],
                      color = [ 'T(3,2,1)' ],
                      lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                      loop_particles = [ [ [P.g, P.Y] ] ],
                      couplings = {(0,2,1):C.UVGC_YYg})
