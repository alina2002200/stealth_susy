from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L

# R2 член для S -> g g
V_Sgg_r2 = Vertex(name = 'V_Sgg_r2',
                  particles = [ P.S, P.g, P.g ],
                  color = [ 'f(1,2,3)' ],
                  lorentz = [ L.VVS1 ],
                  couplings = {(0,0):C.GC_Sgg_r2})

# R2 член для S -> Y Y~
V_SYY_r2 = Vertex(name = 'V_SYY_r2',
                  particles = [ P.S, P.Y, P.Y__tilde__ ],
                  color = [ 'Identity(2,3)' ],
                  lorentz = [ L.FFS1, L.FFS12 ],
                  couplings = {(0,0):C.GC_SYY_r2, (0,1):C.GC_SYY_r2})
