from object_library import all_vertices, all_CTvertices, CTVertex
from object_library import all_CTvertices, CTVertex
import particles as P
import couplings as C
import lorentz as L

V_Sgg_ct = CTVertex(name = 'V_Sgg_ct',
                    type = 'CT',
                    particles = [ P.S, P.g, P.g ],
                    color = [ 'f(1,2,3)' ],
                    lorentz = [ L.VVS1 ],
                    couplings = {(0,0):C.GC_Sgg_ct},
                    loop_particles = [ [ [P.Y] ] ])

V_SYY_ct = CTVertex(name = 'V_SYY_ct',
                    type = 'CT',
                    particles = [ P.S, P.Y, P.Y__tilde__ ],
                    color = [ 'Identity(2,3)' ],
                    lorentz = [ L.FFS1, L.FFS12 ],
                    couplings = {(0,0):C.GC_SYY_ct, (0,1):C.GC_SYY_ct},
                    loop_particles = [ [ [P.Y] ] ])

all_CTvertices = [V_Sgg_ct, V_SYY_ct]
