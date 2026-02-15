from object_library import all_vertices_ct, VertexCT
import particles as P
import couplings as C
import lorentz as L


V_Sgg_ct = VertexCT(name = 'V_Sgg_ct',
                    particles = [ P.S, P.g, P.g ],
                    color = [ 'f(1,2,3)' ],
                    lorentz = [ L.VVS1 ],
                    couplings = {(0,0):C.GC_Sgg_ct})

V_SYY_ct = VertexCT(name = 'V_SYY_ct',
                    particles = [ P.S, P.Y, P.Y__tilde__ ],
                    color = [ 'Identity(2,3)' ],
                    lorentz = [ L.FFS1, L.FFS12 ],
                    couplings = {(0,0):C.GC_SYY_ct, (0,1):C.GC_SYY_ct})

all_vertices_ct = [ V_Sgg_ct, V_SYY_ct ]
