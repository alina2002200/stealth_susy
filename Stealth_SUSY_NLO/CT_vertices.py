# This file was automatically created by FeynRules 1.7.221
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 7 Oct 2013 12:36:37

from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L

# R2 вершина для S -> gg (бесконечная часть)
V_Sgg_R2 = CTVertex(name = 'V_Sgg_R2',
                    type = 'R2',
                    particles = [ P.g, P.g, P.S ],
                    color = [ 'Identity(1,2)' ],
                    lorentz = [ L.VVS1 ],
                    loop_particles = [ [ [P.Y] ] ],
                    couplings = {(0,0,0):C.R2GC_Sgg})

# R2 вершина для S Y Y 
V_SYY_R2 = CTVertex(name = 'V_SYY_R2',
                    type = 'R2',
                    particles = [ P.Y__tilde__, P.Y, P.S ],
                    color = [ 'Identity(1,2)' ],
                    lorentz = [ L.FFS2 ],
                    loop_particles = [ [ [P.g, P.Y] ] ],
                    couplings = {(0,0,0):C.R2GC_SYY})

# UV вершина для пропагатора Y
V_YY_UV = CTVertex(name = 'V_YY_UV',
                   type = 'UV',
                   particles = [ P.Y__tilde__, P.Y ],
                   color = [ 'Identity(1,2)' ],
                   lorentz = [ L.FF1 ],
                   loop_particles = [ [ [P.g, P.Y] ] ],
                   couplings = {(0,0,0):C.UVGC_Sgg})

# UV вершина для S Y Y (контрчлен)
V_SYY_UV = CTVertex(name = 'V_SYY_UV',
                    type = 'UV',
                    particles = [ P.Y__tilde__, P.Y, P.S ],
                    color = [ 'Identity(1,2)' ],
                    lorentz = [ L.FFS2 ],
                    loop_particles = [ [ [P.g, P.Y] ] ],
                    couplings = {(0,0,0):C.UVGC_SYY})

# UV вершина для Y Y g (контрчлен)
V_YYg_UV = CTVertex(name = 'V_YYg_UV',
                    type = 'UV',
                    particles = [ P.Y__tilde__, P.Y, P.g ],
                    color = [ 'T(3,2,1)' ],
                    lorentz = [ L.FFV1 ],
                    loop_particles = [ [ [P.g, P.Y] ] ],
                    couplings = {(0,0,0):C.UVGC_YYg})

# UV вершина для S -> gg (контрчлен)
V_Sgg_UV = CTVertex(name = 'V_Sgg_UV',
                    type = 'UV',
                    particles = [ P.g, P.g, P.S ],
                    color = [ 'Identity(1,2)' ],
                    lorentz = [ L.VVS1 ],
                    loop_particles = [ [ [P.Y] ] ],
                    couplings = {(0,0,0):C.UVGC_Sgg})

# Список всех CT-вершин для экспорта
all_CTvertices = [
    V_Sgg_R2,
    V_SYY_R2,
    V_YY_UV,
    V_SYY_UV,
    V_YYg_UV,
    V_Sgg_UV
]
