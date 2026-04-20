# ------------------------------------------------------------------------------ 
# This model file was automatically created by SARAH version4.15.4
# SARAH References: arXiv:0806.0538, 0909.2863, 1002.0840, 1207.0906, 1309.7223  
# (c) Florian Staub, Mark Goodsell, Werner Porod and Martin Gabelmann 2023 
# ------------------------------------------------------------------------------- 
# File created at 0:06 on 21.4.2026  
# ---------------------------------------------------------------------- 


from object_library import all_vertices,Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
    particles = [P.{}, P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[2,1]], P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[3,1]]],
    color = ['ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][3][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_1,(1,0):C.GC_2,(2,0):C.GC_3,(3,0):C.GC_4,(4,0):C.GC_5,(5,0):C.GC_6})


V_2 = Vertex(name = 'V_2',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_16,(1,0):C.GC_17,(2,0):C.GC_18})


V_3 = Vertex(name = 'V_3',
    particles = [P.{}, P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[2,1]], P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[3,1]]],
    color = ['ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][3][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_21,(1,0):C.GC_22,(2,0):C.GC_23,(3,0):C.GC_24,(4,0):C.GC_25,(5,0):C.GC_26})


V_4 = Vertex(name = 'V_4',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_36,(1,0):C.GC_37,(2,0):C.GC_38})


V_5 = Vertex(name = 'V_5',
    particles = [P.{}, P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[2,1]], P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[3,1]]],
    color = ['ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][3][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_41,(1,0):C.GC_42,(2,0):C.GC_43,(3,0):C.GC_44,(4,0):C.GC_45,(5,0):C.GC_46})


V_6 = Vertex(name = 'V_6',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_56,(1,0):C.GC_57,(2,0):C.GC_58})


V_7 = Vertex(name = 'V_7',
    particles = [P.{}, P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[2,1]], P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[3,1]]],
    color = ['ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][3][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_61,(1,0):C.GC_62,(2,0):C.GC_63,(3,0):C.GC_64,(4,0):C.GC_65,(5,0):C.GC_66})


V_8 = Vertex(name = 'V_8',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_76,(1,0):C.GC_77,(2,0):C.GC_78})


V_9 = Vertex(name = 'V_9',
    particles = [],
    color = ['ReplaceAll(List(),List("MSSM_Stealth"))[1][1][1][1]', 'ReplaceAll(List(),List("MSSM_Stealth"))[1][1][2][1]', 'ReplaceAll(List(),List("MSSM_Stealth"))[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_81,(1,0):C.GC_82,(2,0):C.GC_83})


V_10 = Vertex(name = 'V_10',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_86,(1,0):C.GC_87,(2,0):C.GC_88})


V_11 = Vertex(name = 'V_11',
    particles = [P.{}, P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[2,1]], P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[3,1]]],
    color = ['ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][3][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_91,(1,0):C.GC_92,(2,0):C.GC_93,(3,0):C.GC_94,(4,0):C.GC_95,(5,0):C.GC_96})


V_12 = Vertex(name = 'V_12',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_106,(1,0):C.GC_107,(2,0):C.GC_108})


V_13 = Vertex(name = 'V_13',
    particles = [P.{}, P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[2,1]], P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[3,1]]],
    color = ['ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][3][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_111,(1,0):C.GC_112,(2,0):C.GC_113,(3,0):C.GC_114,(4,0):C.GC_115,(5,0):C.GC_116})


V_14 = Vertex(name = 'V_14',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_126,(1,0):C.GC_127,(2,0):C.GC_128})


V_15 = Vertex(name = 'V_15',
    particles = [P.{}, P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[2,1]], P.({} //. ({} /. {MSSM_Stealth}))[[1,1]][[3,1]]],
    color = ['ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][2][1][3][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][1][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][2][1]', 'ReplaceRepeated(List(),ReplaceAll(List(),List("MSSM_Stealth")))[1][2][3][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_131,(1,0):C.GC_132,(2,0):C.GC_133,(3,0):C.GC_134,(4,0):C.GC_135,(5,0):C.GC_136})


V_16 = Vertex(name = 'V_16',
    particles = [],
    color = ['List("MSSM_Stealth")[1][1][1][1]', 'List("MSSM_Stealth")[1][1][2][1]', 'List("MSSM_Stealth")[1][1][3][1]'],
    lorentz = [L.List()[List()[1][1]][2]],
    couplings = {(0,0):C.GC_146,(1,0):C.GC_147,(2,0):C.GC_148})


