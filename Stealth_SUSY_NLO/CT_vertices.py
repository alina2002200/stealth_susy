# This file was automatically created by FeynRules 1.7.221
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 7 Oct 2013 12:36:37

from object_library import all_CTvertices, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L

V_Sgg_r2 = CTVertex(name = 'V_Sgg_r2',
                    type = 'R2',
                    particles = [ P.g, P.g, P.S__tilde__ ],
                    color = [ 'Identity(1,2)' ],
                    lorentz = [ L.VVS1 ],
                    loop_particles = [ [ [P.Y], [P.Y__tilde__] ] ],
                    couplings = {(0,0,0):C.GC_Sgg_r2})

V_SYY_r2 = CTVertex(name = 'V_SYY_r2',
                    type = 'R2',
                    particles = [ P.S__tilde__, P.Y, P.Y__tilde__ ],
                    color = [ 'Identity(2,3)' ],
                    lorentz = [ L.FFS1, L.FFS12],
                    loop_particles = [ [ [P.Y], [P.Y__tilde__] ] ],
                    couplings = {(0,0,0):C.GC_SYY_r2, (1,0,0):C.GC_SYY_r2})

V_Sgg_ct = CTVertex(name = 'V_Sgg_ct',
                    type = 'UV',
                    particles = [ P.g, P.g, P.S__tilde__ ],
                    color = [ 'Identity(1,2)' ],
                    lorentz = [ L.VVS1 ],
                    loop_particles = [ [ [P.Y], [P.Y__tilde__] ] ],
                    couplings = {(0,0,0):C.GC_Sgg_ct})

V_SYY_ct = CTVertex(name = 'V_SYY_ct',
                    type = 'UV',
                    particles = [ P.S__tilde__, P.Y, P.Y__tilde__ ],
                    color = [ 'Identity(2,3)' ],
                    lorentz = [ L.FFS1, L.FFS12],
                    loop_particles = [ [ [P.Y], [P.Y__tilde__] ] ],
                    couplings = {(0,0,0):C.GC_SYY_ct, (1,0,0):C.GC_SYY_ct})

V_YYg_ct = CTVertex(name = 'V_YYg_ct',
                    type = 'UV',
                    particles = [ P.Y, P.Y__tilde__, P.g ],
                    color = [ 'T(1,2,3)' ],
                    lorentz = [ L.FFV1 ],
                    loop_particles = [ [ [P.Y], [P.Y__tilde__] ] ],
                    couplings = {(0,0,0):C.GC_YYg_ct})

