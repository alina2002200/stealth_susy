# This file was automatically created by FeynRules 2.4.43
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Wed 30 Nov 2016 08:56:01


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L

V_n1_a_S1 = Vertex(name = 'V_n1_a_S1',
    particles = [ P.n1, P.S1, P.a ],
    color = ['1'],
    lorentz = [ L.FFV_effective ],
    couplings = {(0,0): C.GC_n1_a_S1})

V_2195 = Vertex(name = 'V_2195',
              particles = [ P.S1, P.grv, P.S ],
              color = [ '1' ],
              lorentz = [ L.FRS4 ],
              couplings = {(0,0):C.GC_S1SGrav})

V_2196 = Vertex(name = 'V_2196',
              particles = [ P.S1__tilde__, P.grv, P.S__tilde__ ],
              color = [ '1' ],
               lorentz = [ L.FRS4],
               couplings = {(0,0):C.GC_S1SGrav})

V_Sgg = Vertex(name = 'V_Sgg',
              particles = [ P.g, P.g, P.S ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS_effective ],
              couplings = {(0,0): C.GC_Sgg})

V_Sgg1 = Vertex(name = 'V_Sgg1',
              particles = [ P.g, P.g, P.S__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS_effective ],
              couplings = {(0,0):C.GC_Sgg})


V_1 = Vertex(name = 'V_1',
             particles = [ P.seL__plus__, P.seL__plus__, P.seL__minus__, P.seL__minus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_81})

V_2 = Vertex(name = 'V_2',
             particles = [ P.seL__plus__, P.seL__minus__, P.smuL__plus__, P.smuL__minus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_79})

V_3 = Vertex(name = 'V_3',
             particles = [ P.smuL__plus__, P.smuL__plus__, P.smuL__minus__, P.smuL__minus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_81})

V_4 = Vertex(name = 'V_4',
             particles = [ P.seL__plus__, P.seL__minus__, P.sne__tilde__, P.sne ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_79})

V_5 = Vertex(name = 'V_5',
             particles = [ P.smuL__plus__, P.smuL__minus__, P.sne__tilde__, P.sne ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_109})

V_6 = Vertex(name = 'V_6',
             particles = [ P.sne__tilde__, P.sne__tilde__, P.sne, P.sne ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_81})

V_7 = Vertex(name = 'V_7',
             particles = [ P.seL__plus__, P.smuL__minus__, P.sne, P.snm__tilde__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_29})

V_8 = Vertex(name = 'V_8',
             particles = [ P.seL__minus__, P.smuL__plus__, P.sne__tilde__, P.snm ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_29})

V_9 = Vertex(name = 'V_9',
             particles = [ P.seL__plus__, P.seL__minus__, P.snm__tilde__, P.snm ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_109})

V_10 = Vertex(name = 'V_10',
              particles = [ P.smuL__plus__, P.smuL__minus__, P.snm__tilde__, P.snm ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_79})

V_11 = Vertex(name = 'V_11',
              particles = [ P.sne__tilde__, P.sne, P.snm__tilde__, P.snm ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_79})

V_12 = Vertex(name = 'V_12',
              particles = [ P.snm__tilde__, P.snm__tilde__, P.snm, P.snm ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_81})

V_13 = Vertex(name = 'V_13',
              particles = [ P.seL__plus__, P.seL__minus__, P.snt__tilde__, P.snt ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_109})

V_14 = Vertex(name = 'V_14',
              particles = [ P.smuL__plus__, P.smuL__minus__, P.snt__tilde__, P.snt ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_109})

V_15 = Vertex(name = 'V_15',
              particles = [ P.sne__tilde__, P.sne, P.snt__tilde__, P.snt ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_79})

V_16 = Vertex(name = 'V_16',
              particles = [ P.snm__tilde__, P.snm, P.snt__tilde__, P.snt ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_79})

V_17 = Vertex(name = 'V_17',
              particles = [ P.snt__tilde__, P.snt__tilde__, P.snt, P.snt ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_81})

V_18 = Vertex(name = 'V_18',
              particles = [ P.seL__plus__, P.seL__minus__, P.seR__plus__, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_19 = Vertex(name = 'V_19',
              particles = [ P.seR__plus__, P.seR__plus__, P.seR__minus__, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_62})

V_20 = Vertex(name = 'V_20',
              particles = [ P.seR__plus__, P.seR__minus__, P.smuL__plus__, P.smuL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_21 = Vertex(name = 'V_21',
              particles = [ P.seL__plus__, P.seL__minus__, P.smuR__plus__, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_22 = Vertex(name = 'V_22',
              particles = [ P.seR__plus__, P.seR__minus__, P.smuR__plus__, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_61})

V_23 = Vertex(name = 'V_23',
              particles = [ P.smuL__plus__, P.smuL__minus__, P.smuR__plus__, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_24 = Vertex(name = 'V_24',
              particles = [ P.smuR__plus__, P.smuR__plus__, P.smuR__minus__, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_62})

V_25 = Vertex(name = 'V_25',
              particles = [ P.seR__plus__, P.seR__minus__, P.sne__tilde__, P.sne ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_26 = Vertex(name = 'V_26',
              particles = [ P.smuR__plus__, P.smuR__minus__, P.sne__tilde__, P.sne ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_27 = Vertex(name = 'V_27',
              particles = [ P.seR__plus__, P.seR__minus__, P.snm__tilde__, P.snm ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_28 = Vertex(name = 'V_28',
              particles = [ P.smuR__plus__, P.smuR__minus__, P.snm__tilde__, P.snm ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_29 = Vertex(name = 'V_29',
              particles = [ P.seR__plus__, P.seR__minus__, P.snt__tilde__, P.snt ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_30 = Vertex(name = 'V_30',
              particles = [ P.smuR__plus__, P.smuR__minus__, P.snt__tilde__, P.snt ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.a, P.seL__plus__, P.seL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_32 = Vertex(name = 'V_32',
              particles = [ P.a, P.a, P.seR__plus__, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_33 = Vertex(name = 'V_33',
              particles = [ P.a, P.a, P.smuL__plus__, P.smuL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_34 = Vertex(name = 'V_34',
              particles = [ P.a, P.a, P.smuR__plus__, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.seL__plus__, P.seL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_6})

V_36 = Vertex(name = 'V_36',
              particles = [ P.a, P.seR__plus__, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_6})

V_37 = Vertex(name = 'V_37',
              particles = [ P.a, P.smuL__plus__, P.smuL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_6})

V_38 = Vertex(name = 'V_38',
              particles = [ P.a, P.smuR__plus__, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_6})

V_39 = Vertex(name = 'V_39',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_11})

V_40 = Vertex(name = 'V_40',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_11})

V_41 = Vertex(name = 'V_41',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV4, L.VVVV7, L.VVVV8 ],
              couplings = {(1,1):C.GC_19,(0,0):C.GC_19,(2,2):C.GC_19})

V_42 = Vertex(name = 'V_42',
              particles = [ P.n1, P.e__minus__, P.seR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_67})

V_43 = Vertex(name = 'V_43',
              particles = [ P.n1, P.mu__minus__, P.smuR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_67})

V_44 = Vertex(name = 'V_44',
              particles = [ P.e__plus__, P.n1, P.seL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_149})

V_45 = Vertex(name = 'V_45',
              particles = [ P.mu__plus__, P.n1, P.smuL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_149})

V_46 = Vertex(name = 'V_46',
              particles = [ P.ve__tilde__, P.n1, P.sne ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_147})

V_47 = Vertex(name = 'V_47',
              particles = [ P.vm__tilde__, P.n1, P.snm ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_147})

V_48 = Vertex(name = 'V_48',
              particles = [ P.vt__tilde__, P.n1, P.snt ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_147})

V_49 = Vertex(name = 'V_49',
              particles = [ P.n2, P.e__minus__, P.seR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_70})

V_50 = Vertex(name = 'V_50',
              particles = [ P.n2, P.mu__minus__, P.smuR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_70})

V_51 = Vertex(name = 'V_51',
              particles = [ P.e__plus__, P.n2, P.seL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_153})

V_52 = Vertex(name = 'V_52',
              particles = [ P.mu__plus__, P.n2, P.smuL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_153})

V_53 = Vertex(name = 'V_53',
              particles = [ P.ve__tilde__, P.n2, P.sne ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_151})

V_54 = Vertex(name = 'V_54',
              particles = [ P.vm__tilde__, P.n2, P.snm ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_151})

V_55 = Vertex(name = 'V_55',
              particles = [ P.vt__tilde__, P.n2, P.snt ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_151})

V_56 = Vertex(name = 'V_56',
              particles = [ P.n3, P.e__minus__, P.seR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_73})

V_57 = Vertex(name = 'V_57',
              particles = [ P.n3, P.mu__minus__, P.smuR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_73})

V_58 = Vertex(name = 'V_58',
              particles = [ P.e__plus__, P.n3, P.seL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_157})

V_59 = Vertex(name = 'V_59',
              particles = [ P.mu__plus__, P.n3, P.smuL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_157})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ve__tilde__, P.n3, P.sne ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_155})

V_61 = Vertex(name = 'V_61',
              particles = [ P.vm__tilde__, P.n3, P.snm ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_155})

V_62 = Vertex(name = 'V_62',
              particles = [ P.vt__tilde__, P.n3, P.snt ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_155})

V_63 = Vertex(name = 'V_63',
              particles = [ P.n4, P.e__minus__, P.seR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_76})

V_64 = Vertex(name = 'V_64',
              particles = [ P.n4, P.mu__minus__, P.smuR__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_76})

V_65 = Vertex(name = 'V_65',
              particles = [ P.e__plus__, P.n4, P.seL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_161})

V_66 = Vertex(name = 'V_66',
              particles = [ P.mu__plus__, P.n4, P.smuL__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_161})

V_67 = Vertex(name = 'V_67',
              particles = [ P.ve__tilde__, P.n4, P.sne ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_159})

V_68 = Vertex(name = 'V_68',
              particles = [ P.vm__tilde__, P.n4, P.snm ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_159})

V_69 = Vertex(name = 'V_69',
              particles = [ P.vt__tilde__, P.n4, P.snt ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_159})

V_70 = Vertex(name = 'V_70',
              particles = [ P.n1, P.e__minus__, P.seL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_149})

V_71 = Vertex(name = 'V_71',
              particles = [ P.n1, P.mu__minus__, P.smuL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_149})

V_72 = Vertex(name = 'V_72',
              particles = [ P.e__plus__, P.n1, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_67})

V_73 = Vertex(name = 'V_73',
              particles = [ P.mu__plus__, P.n1, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_67})

V_74 = Vertex(name = 'V_74',
              particles = [ P.n1, P.ve, P.sne__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_147})

V_75 = Vertex(name = 'V_75',
              particles = [ P.n1, P.vm, P.snm__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_147})

V_76 = Vertex(name = 'V_76',
              particles = [ P.n1, P.vt, P.snt__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_147})

V_77 = Vertex(name = 'V_77',
              particles = [ P.n2, P.e__minus__, P.seL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_153})

V_78 = Vertex(name = 'V_78',
              particles = [ P.n2, P.mu__minus__, P.smuL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_153})

V_79 = Vertex(name = 'V_79',
              particles = [ P.e__plus__, P.n2, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_70})

V_80 = Vertex(name = 'V_80',
              particles = [ P.mu__plus__, P.n2, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_70})

V_81 = Vertex(name = 'V_81',
              particles = [ P.n2, P.ve, P.sne__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_151})

V_82 = Vertex(name = 'V_82',
              particles = [ P.n2, P.vm, P.snm__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_151})

V_83 = Vertex(name = 'V_83',
              particles = [ P.n2, P.vt, P.snt__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_151})

V_84 = Vertex(name = 'V_84',
              particles = [ P.n3, P.e__minus__, P.seL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_157})

V_85 = Vertex(name = 'V_85',
              particles = [ P.n3, P.mu__minus__, P.smuL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_157})

V_86 = Vertex(name = 'V_86',
              particles = [ P.e__plus__, P.n3, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_73})

V_87 = Vertex(name = 'V_87',
              particles = [ P.mu__plus__, P.n3, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_73})

V_88 = Vertex(name = 'V_88',
              particles = [ P.n3, P.ve, P.sne__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_155})

V_89 = Vertex(name = 'V_89',
              particles = [ P.n3, P.vm, P.snm__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_155})

V_90 = Vertex(name = 'V_90',
              particles = [ P.n3, P.vt, P.snt__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_155})

V_91 = Vertex(name = 'V_91',
              particles = [ P.n4, P.e__minus__, P.seL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_161})

V_92 = Vertex(name = 'V_92',
              particles = [ P.n4, P.mu__minus__, P.smuL__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_161})

V_93 = Vertex(name = 'V_93',
              particles = [ P.e__plus__, P.n4, P.seR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_76})

V_94 = Vertex(name = 'V_94',
              particles = [ P.mu__plus__, P.n4, P.smuR__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_76})

V_95 = Vertex(name = 'V_95',
              particles = [ P.n4, P.ve, P.sne__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_159})

V_96 = Vertex(name = 'V_96',
              particles = [ P.n4, P.vm, P.snm__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_159})

V_97 = Vertex(name = 'V_97',
              particles = [ P.n4, P.vt, P.snt__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_159})

V_98 = Vertex(name = 'V_98',
              particles = [ P.seL__minus__, P.sne__tilde__, P.snt, P.stau1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_32})

V_99 = Vertex(name = 'V_99',
              particles = [ P.smuL__minus__, P.snm__tilde__, P.snt, P.stau1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_32})

V_100 = Vertex(name = 'V_100',
               particles = [ P.seL__plus__, P.sne, P.snt__tilde__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_101 = Vertex(name = 'V_101',
               particles = [ P.smuL__plus__, P.snm, P.snt__tilde__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_102 = Vertex(name = 'V_102',
               particles = [ P.tau__plus__, P.n1, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_215,(0,1):C.GC_211})

V_103 = Vertex(name = 'V_103',
               particles = [ P.tau__plus__, P.n2, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_212})

V_104 = Vertex(name = 'V_104',
               particles = [ P.tau__plus__, P.n3, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_213})

V_105 = Vertex(name = 'V_105',
               particles = [ P.tau__plus__, P.n4, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_218,(0,1):C.GC_214})

V_106 = Vertex(name = 'V_106',
               particles = [ P.n1, P.tau__minus__, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_211,(0,1):C.GC_215})

V_107 = Vertex(name = 'V_107',
               particles = [ P.n2, P.tau__minus__, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_212,(0,1):C.GC_216})

V_108 = Vertex(name = 'V_108',
               particles = [ P.n3, P.tau__minus__, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_217})

V_109 = Vertex(name = 'V_109',
               particles = [ P.n4, P.tau__minus__, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_218})

V_110 = Vertex(name = 'V_110',
               particles = [ P.seL__plus__, P.seL__minus__, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_116})

V_111 = Vertex(name = 'V_111',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_116})

V_112 = Vertex(name = 'V_112',
               particles = [ P.sne__tilde__, P.sne, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_114})

V_113 = Vertex(name = 'V_113',
               particles = [ P.snm__tilde__, P.snm, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_114})

V_114 = Vertex(name = 'V_114',
               particles = [ P.snt__tilde__, P.snt, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_231})

V_115 = Vertex(name = 'V_115',
               particles = [ P.seR__plus__, P.seR__minus__, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_100})

V_116 = Vertex(name = 'V_116',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_100})

V_117 = Vertex(name = 'V_117',
               particles = [ P.a, P.a, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_21})

V_118 = Vertex(name = 'V_118',
               particles = [ P.a, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_20})

V_119 = Vertex(name = 'V_119',
               particles = [ P.stau1__plus__, P.stau1__plus__, P.stau1__minus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_232})

V_120 = Vertex(name = 'V_120',
               particles = [ P.seL__minus__, P.sne__tilde__, P.snt, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_121 = Vertex(name = 'V_121',
               particles = [ P.smuL__minus__, P.snm__tilde__, P.snt, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_122 = Vertex(name = 'V_122',
               particles = [ P.seL__plus__, P.sne, P.snt__tilde__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_123 = Vertex(name = 'V_123',
               particles = [ P.smuL__plus__, P.snm, P.snt__tilde__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_124 = Vertex(name = 'V_124',
               particles = [ P.tau__plus__, P.n1, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_223,(0,1):C.GC_219})

V_125 = Vertex(name = 'V_125',
               particles = [ P.tau__plus__, P.n2, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_220})

V_126 = Vertex(name = 'V_126',
               particles = [ P.tau__plus__, P.n3, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_225,(0,1):C.GC_221})

V_127 = Vertex(name = 'V_127',
               particles = [ P.tau__plus__, P.n4, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_226,(0,1):C.GC_222})

V_128 = Vertex(name = 'V_128',
               particles = [ P.n1, P.tau__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_223})

V_129 = Vertex(name = 'V_129',
               particles = [ P.n2, P.tau__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_220,(0,1):C.GC_224})

V_130 = Vertex(name = 'V_130',
               particles = [ P.n3, P.tau__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_221,(0,1):C.GC_225})

V_131 = Vertex(name = 'V_131',
               particles = [ P.n4, P.tau__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_226})

V_132 = Vertex(name = 'V_132',
               particles = [ P.seL__plus__, P.seL__minus__, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_120})

V_133 = Vertex(name = 'V_133',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_120})

V_134 = Vertex(name = 'V_134',
               particles = [ P.sne__tilde__, P.sne, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_118})

V_135 = Vertex(name = 'V_135',
               particles = [ P.snm__tilde__, P.snm, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_118})

V_136 = Vertex(name = 'V_136',
               particles = [ P.snt__tilde__, P.snt, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_233})

V_137 = Vertex(name = 'V_137',
               particles = [ P.seL__plus__, P.seL__minus__, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_120})

V_138 = Vertex(name = 'V_138',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_120})

V_139 = Vertex(name = 'V_139',
               particles = [ P.sne__tilde__, P.sne, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_118})

V_140 = Vertex(name = 'V_140',
               particles = [ P.snm__tilde__, P.snm, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_118})

V_141 = Vertex(name = 'V_141',
               particles = [ P.snt__tilde__, P.snt, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_233})

V_142 = Vertex(name = 'V_142',
               particles = [ P.seR__plus__, P.seR__minus__, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_103})

V_143 = Vertex(name = 'V_143',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_103})

V_144 = Vertex(name = 'V_144',
               particles = [ P.seR__plus__, P.seR__minus__, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_103})

V_145 = Vertex(name = 'V_145',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_103})

V_146 = Vertex(name = 'V_146',
               particles = [ P.a, P.a, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_24})

V_147 = Vertex(name = 'V_147',
               particles = [ P.a, P.a, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_24})

V_148 = Vertex(name = 'V_148',
               particles = [ P.a, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_23})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_22})

V_150 = Vertex(name = 'V_150',
               particles = [ P.stau1__plus__, P.stau1__minus__, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_234})

V_151 = Vertex(name = 'V_151',
               particles = [ P.stau1__plus__, P.stau1__plus__, P.stau1__minus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_234})

V_152 = Vertex(name = 'V_152',
               particles = [ P.seL__plus__, P.seL__minus__, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_124})

V_153 = Vertex(name = 'V_153',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_124})

V_154 = Vertex(name = 'V_154',
               particles = [ P.sne__tilde__, P.sne, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_122})

V_155 = Vertex(name = 'V_155',
               particles = [ P.snm__tilde__, P.snm, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_122})

V_156 = Vertex(name = 'V_156',
               particles = [ P.snt__tilde__, P.snt, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_236})

V_157 = Vertex(name = 'V_157',
               particles = [ P.seR__plus__, P.seR__minus__, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_106})

V_158 = Vertex(name = 'V_158',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_106})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.a, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_160 = Vertex(name = 'V_160',
               particles = [ P.a, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_25})

V_161 = Vertex(name = 'V_161',
               particles = [ P.stau1__minus__, P.stau1__minus__, P.stau2__plus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_235})

V_162 = Vertex(name = 'V_162',
               particles = [ P.stau1__plus__, P.stau1__minus__, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_237})

V_163 = Vertex(name = 'V_163',
               particles = [ P.stau1__plus__, P.stau1__plus__, P.stau2__minus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_235})

V_164 = Vertex(name = 'V_164',
               particles = [ P.stau1__minus__, P.stau2__plus__, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_238})

V_165 = Vertex(name = 'V_165',
               particles = [ P.stau1__plus__, P.stau2__plus__, P.stau2__minus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_238})

V_166 = Vertex(name = 'V_166',
               particles = [ P.stau2__plus__, P.stau2__plus__, P.stau2__minus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_239})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.sbL__tilde__, P.sbL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_168 = Vertex(name = 'V_168',
               particles = [ P.n1, P.b, P.sbL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_148})

V_169 = Vertex(name = 'V_169',
               particles = [ P.n2, P.b, P.sbL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_152})

V_170 = Vertex(name = 'V_170',
               particles = [ P.n3, P.b, P.sbL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_156})

V_171 = Vertex(name = 'V_171',
               particles = [ P.n4, P.b, P.sbL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_160})

V_172 = Vertex(name = 'V_172',
               particles = [ P.b__tilde__, P.n1, P.sbL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_148})

V_173 = Vertex(name = 'V_173',
               particles = [ P.b__tilde__, P.n2, P.sbL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_152})

V_174 = Vertex(name = 'V_174',
               particles = [ P.b__tilde__, P.n3, P.sbL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_156})

V_175 = Vertex(name = 'V_175',
               particles = [ P.b__tilde__, P.n4, P.sbL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_160})

V_176 = Vertex(name = 'V_176',
               particles = [ P.sbL__tilde__, P.sbL, P.seL__plus__, P.seL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_177 = Vertex(name = 'V_177',
               particles = [ P.sbL__tilde__, P.sbL, P.smuL__plus__, P.smuL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_178 = Vertex(name = 'V_178',
               particles = [ P.sbL__tilde__, P.sbL, P.sne__tilde__, P.sne ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_179 = Vertex(name = 'V_179',
               particles = [ P.sbL__tilde__, P.sbL, P.snm__tilde__, P.snm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_180 = Vertex(name = 'V_180',
               particles = [ P.sbL__tilde__, P.sbL, P.snt__tilde__, P.snt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_181 = Vertex(name = 'V_181',
               particles = [ P.sbL__tilde__, P.sbL, P.seR__plus__, P.seR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_182 = Vertex(name = 'V_182',
               particles = [ P.sbL__tilde__, P.sbL, P.smuR__plus__, P.smuR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_183 = Vertex(name = 'V_183',
               particles = [ P.a, P.a, P.sbL__tilde__, P.sbL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_184 = Vertex(name = 'V_184',
               particles = [ P.sbL__tilde__, P.sbL, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_115})

V_185 = Vertex(name = 'V_185',
               particles = [ P.sbL__tilde__, P.sbL, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_119})

V_186 = Vertex(name = 'V_186',
               particles = [ P.sbL__tilde__, P.sbL, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_119})

V_187 = Vertex(name = 'V_187',
               particles = [ P.sbL__tilde__, P.sbL, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_123})

V_188 = Vertex(name = 'V_188',
               particles = [ P.sbL__tilde__, P.sbL__tilde__, P.sbL, P.sbL ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_110,(0,0):C.GC_110,(3,0):C.GC_172,(2,0):C.GC_172})

V_189 = Vertex(name = 'V_189',
               particles = [ P.a, P.sbR__tilde__, P.sbR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_190 = Vertex(name = 'V_190',
               particles = [ P.n1, P.b, P.sbR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_65})

V_191 = Vertex(name = 'V_191',
               particles = [ P.n2, P.b, P.sbR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_68})

V_192 = Vertex(name = 'V_192',
               particles = [ P.n3, P.b, P.sbR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_71})

V_193 = Vertex(name = 'V_193',
               particles = [ P.n4, P.b, P.sbR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_74})

V_194 = Vertex(name = 'V_194',
               particles = [ P.b__tilde__, P.n1, P.sbR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_65})

V_195 = Vertex(name = 'V_195',
               particles = [ P.b__tilde__, P.n2, P.sbR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_68})

V_196 = Vertex(name = 'V_196',
               particles = [ P.b__tilde__, P.n3, P.sbR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_71})

V_197 = Vertex(name = 'V_197',
               particles = [ P.b__tilde__, P.n4, P.sbR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_74})

V_198 = Vertex(name = 'V_198',
               particles = [ P.sbR__tilde__, P.sbR, P.seL__plus__, P.seL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_199 = Vertex(name = 'V_199',
               particles = [ P.sbR__tilde__, P.sbR, P.seR__plus__, P.seR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_200 = Vertex(name = 'V_200',
               particles = [ P.sbR__tilde__, P.sbR, P.smuL__plus__, P.smuL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_201 = Vertex(name = 'V_201',
               particles = [ P.sbR__tilde__, P.sbR, P.smuR__plus__, P.smuR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_202 = Vertex(name = 'V_202',
               particles = [ P.sbR__tilde__, P.sbR, P.sne__tilde__, P.sne ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_203 = Vertex(name = 'V_203',
               particles = [ P.sbR__tilde__, P.sbR, P.snm__tilde__, P.snm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_204 = Vertex(name = 'V_204',
               particles = [ P.sbR__tilde__, P.sbR, P.snt__tilde__, P.snt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_205 = Vertex(name = 'V_205',
               particles = [ P.a, P.a, P.sbR__tilde__, P.sbR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_206 = Vertex(name = 'V_206',
               particles = [ P.sbR__tilde__, P.sbR, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_98})

V_207 = Vertex(name = 'V_207',
               particles = [ P.sbR__tilde__, P.sbR, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_101})

V_208 = Vertex(name = 'V_208',
               particles = [ P.sbR__tilde__, P.sbR, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_101})

V_209 = Vertex(name = 'V_209',
               particles = [ P.sbR__tilde__, P.sbR, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_104})

V_210 = Vertex(name = 'V_210',
               particles = [ P.sbL__tilde__, P.sbL, P.sbR__tilde__, P.sbR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_211 = Vertex(name = 'V_211',
               particles = [ P.sbR__tilde__, P.sbR__tilde__, P.sbR, P.sbR ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_53,(0,0):C.GC_53,(3,0):C.GC_172,(2,0):C.GC_172})

V_212 = Vertex(name = 'V_212',
               particles = [ P.a, P.scL__tilde__, P.scL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_213 = Vertex(name = 'V_213',
               particles = [ P.n1, P.c, P.scL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_146})

V_214 = Vertex(name = 'V_214',
               particles = [ P.n2, P.c, P.scL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_150})

V_215 = Vertex(name = 'V_215',
               particles = [ P.n3, P.c, P.scL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_154})

V_216 = Vertex(name = 'V_216',
               particles = [ P.n4, P.c, P.scL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_158})

V_217 = Vertex(name = 'V_217',
               particles = [ P.c__tilde__, P.n1, P.scL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_146})

V_218 = Vertex(name = 'V_218',
               particles = [ P.c__tilde__, P.n2, P.scL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_150})

V_219 = Vertex(name = 'V_219',
               particles = [ P.c__tilde__, P.n3, P.scL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_154})

V_220 = Vertex(name = 'V_220',
               particles = [ P.c__tilde__, P.n4, P.scL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_158})

V_221 = Vertex(name = 'V_221',
               particles = [ P.scL__tilde__, P.scL, P.seL__plus__, P.seL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_222 = Vertex(name = 'V_222',
               particles = [ P.scL__tilde__, P.scL, P.smuL__plus__, P.smuL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_223 = Vertex(name = 'V_223',
               particles = [ P.scL__tilde__, P.scL, P.sne__tilde__, P.sne ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_224 = Vertex(name = 'V_224',
               particles = [ P.scL__tilde__, P.scL, P.snm__tilde__, P.snm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_225 = Vertex(name = 'V_225',
               particles = [ P.scL__tilde__, P.scL, P.snt__tilde__, P.snt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_226 = Vertex(name = 'V_226',
               particles = [ P.scL__tilde__, P.scL, P.seR__plus__, P.seR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_227 = Vertex(name = 'V_227',
               particles = [ P.scL__tilde__, P.scL, P.smuR__plus__, P.smuR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_228 = Vertex(name = 'V_228',
               particles = [ P.a, P.a, P.scL__tilde__, P.scL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_229 = Vertex(name = 'V_229',
               particles = [ P.scL__tilde__, P.scL, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_113})

V_230 = Vertex(name = 'V_230',
               particles = [ P.scL__tilde__, P.scL, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_117})

V_231 = Vertex(name = 'V_231',
               particles = [ P.scL__tilde__, P.scL, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_117})

V_232 = Vertex(name = 'V_232',
               particles = [ P.scL__tilde__, P.scL, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_121})

V_233 = Vertex(name = 'V_233',
               particles = [ P.sbL__tilde__, P.sbL, P.scL__tilde__, P.scL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_108,(1,0):C.GC_172})

V_234 = Vertex(name = 'V_234',
               particles = [ P.sbR__tilde__, P.sbR, P.scL__tilde__, P.scL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_235 = Vertex(name = 'V_235',
               particles = [ P.scL__tilde__, P.scL__tilde__, P.scL, P.scL ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_110,(0,0):C.GC_110,(3,0):C.GC_172,(2,0):C.GC_172})

V_236 = Vertex(name = 'V_236',
               particles = [ P.a, P.scR__tilde__, P.scR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_237 = Vertex(name = 'V_237',
               particles = [ P.n1, P.c, P.scR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_66})

V_238 = Vertex(name = 'V_238',
               particles = [ P.n2, P.c, P.scR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_69})

V_239 = Vertex(name = 'V_239',
               particles = [ P.n3, P.c, P.scR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_72})

V_240 = Vertex(name = 'V_240',
               particles = [ P.n4, P.c, P.scR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_75})

V_241 = Vertex(name = 'V_241',
               particles = [ P.c__tilde__, P.n1, P.scR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_66})

V_242 = Vertex(name = 'V_242',
               particles = [ P.c__tilde__, P.n2, P.scR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_69})

V_243 = Vertex(name = 'V_243',
               particles = [ P.c__tilde__, P.n3, P.scR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_72})

V_244 = Vertex(name = 'V_244',
               particles = [ P.c__tilde__, P.n4, P.scR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_75})

V_245 = Vertex(name = 'V_245',
               particles = [ P.scR__tilde__, P.scR, P.seL__plus__, P.seL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_246 = Vertex(name = 'V_246',
               particles = [ P.scR__tilde__, P.scR, P.seR__plus__, P.seR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_60})

V_247 = Vertex(name = 'V_247',
               particles = [ P.scR__tilde__, P.scR, P.smuL__plus__, P.smuL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_248 = Vertex(name = 'V_248',
               particles = [ P.scR__tilde__, P.scR, P.smuR__plus__, P.smuR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_60})

V_249 = Vertex(name = 'V_249',
               particles = [ P.scR__tilde__, P.scR, P.sne__tilde__, P.sne ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_250 = Vertex(name = 'V_250',
               particles = [ P.scR__tilde__, P.scR, P.snm__tilde__, P.snm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_251 = Vertex(name = 'V_251',
               particles = [ P.scR__tilde__, P.scR, P.snt__tilde__, P.snt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_252 = Vertex(name = 'V_252',
               particles = [ P.a, P.a, P.scR__tilde__, P.scR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_253 = Vertex(name = 'V_253',
               particles = [ P.scR__tilde__, P.scR, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_99})

V_254 = Vertex(name = 'V_254',
               particles = [ P.scR__tilde__, P.scR, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_102})

V_255 = Vertex(name = 'V_255',
               particles = [ P.scR__tilde__, P.scR, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_102})

V_256 = Vertex(name = 'V_256',
               particles = [ P.scR__tilde__, P.scR, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_105})

V_257 = Vertex(name = 'V_257',
               particles = [ P.sbL__tilde__, P.sbL, P.scR__tilde__, P.scR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_258 = Vertex(name = 'V_258',
               particles = [ P.sbR__tilde__, P.sbR, P.scR__tilde__, P.scR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_259 = Vertex(name = 'V_259',
               particles = [ P.scL__tilde__, P.scL, P.scR__tilde__, P.scR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_260 = Vertex(name = 'V_260',
               particles = [ P.scR__tilde__, P.scR__tilde__, P.scR, P.scR ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_58,(0,0):C.GC_58,(3,0):C.GC_172,(2,0):C.GC_172})

V_261 = Vertex(name = 'V_261',
               particles = [ P.a, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_262 = Vertex(name = 'V_262',
               particles = [ P.n1, P.d, P.sdL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_148})

V_263 = Vertex(name = 'V_263',
               particles = [ P.n2, P.d, P.sdL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_152})

V_264 = Vertex(name = 'V_264',
               particles = [ P.n3, P.d, P.sdL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_156})

V_265 = Vertex(name = 'V_265',
               particles = [ P.n4, P.d, P.sdL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_160})

V_266 = Vertex(name = 'V_266',
               particles = [ P.d__tilde__, P.n1, P.sdL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_148})

V_267 = Vertex(name = 'V_267',
               particles = [ P.d__tilde__, P.n2, P.sdL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_152})

V_268 = Vertex(name = 'V_268',
               particles = [ P.d__tilde__, P.n3, P.sdL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_156})

V_269 = Vertex(name = 'V_269',
               particles = [ P.d__tilde__, P.n4, P.sdL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_160})

V_270 = Vertex(name = 'V_270',
               particles = [ P.sdL__tilde__, P.sdL, P.seL__plus__, P.seL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_271 = Vertex(name = 'V_271',
               particles = [ P.sdL__tilde__, P.sdL, P.smuL__plus__, P.smuL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_272 = Vertex(name = 'V_272',
               particles = [ P.sdL__tilde__, P.sdL, P.sne__tilde__, P.sne ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_273 = Vertex(name = 'V_273',
               particles = [ P.sdL__tilde__, P.sdL, P.snm__tilde__, P.snm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_274 = Vertex(name = 'V_274',
               particles = [ P.sdL__tilde__, P.sdL, P.snt__tilde__, P.snt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_275 = Vertex(name = 'V_275',
               particles = [ P.sdL__tilde__, P.sdL, P.seR__plus__, P.seR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_276 = Vertex(name = 'V_276',
               particles = [ P.sdL__tilde__, P.sdL, P.smuR__plus__, P.smuR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_277 = Vertex(name = 'V_277',
               particles = [ P.a, P.a, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_278 = Vertex(name = 'V_278',
               particles = [ P.sdL__tilde__, P.sdL, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_115})

V_279 = Vertex(name = 'V_279',
               particles = [ P.sdL__tilde__, P.sdL, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_119})

V_280 = Vertex(name = 'V_280',
               particles = [ P.sdL__tilde__, P.sdL, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_119})

V_281 = Vertex(name = 'V_281',
               particles = [ P.sdL__tilde__, P.sdL, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_123})

V_282 = Vertex(name = 'V_282',
               particles = [ P.sbL__tilde__, P.sbL, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_110,(1,0):C.GC_172})

V_283 = Vertex(name = 'V_283',
               particles = [ P.sbR__tilde__, P.sbR, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_284 = Vertex(name = 'V_284',
               particles = [ P.scL__tilde__, P.scL, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_108,(1,0):C.GC_172})

V_285 = Vertex(name = 'V_285',
               particles = [ P.scR__tilde__, P.scR, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_286 = Vertex(name = 'V_286',
               particles = [ P.sdL__tilde__, P.sdL__tilde__, P.sdL, P.sdL ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_110,(0,0):C.GC_110,(3,0):C.GC_172,(2,0):C.GC_172})

V_287 = Vertex(name = 'V_287',
               particles = [ P.a, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_288 = Vertex(name = 'V_288',
               particles = [ P.n1, P.d, P.sdR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_65})

V_289 = Vertex(name = 'V_289',
               particles = [ P.n2, P.d, P.sdR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_68})

V_290 = Vertex(name = 'V_290',
               particles = [ P.n3, P.d, P.sdR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_71})

V_291 = Vertex(name = 'V_291',
               particles = [ P.n4, P.d, P.sdR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_74})

V_292 = Vertex(name = 'V_292',
               particles = [ P.d__tilde__, P.n1, P.sdR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_65})

V_293 = Vertex(name = 'V_293',
               particles = [ P.d__tilde__, P.n2, P.sdR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_68})

V_294 = Vertex(name = 'V_294',
               particles = [ P.d__tilde__, P.n3, P.sdR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_71})

V_295 = Vertex(name = 'V_295',
               particles = [ P.d__tilde__, P.n4, P.sdR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_74})

V_296 = Vertex(name = 'V_296',
               particles = [ P.sdR__tilde__, P.sdR, P.seL__plus__, P.seL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_297 = Vertex(name = 'V_297',
               particles = [ P.sdR__tilde__, P.sdR, P.seR__plus__, P.seR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_298 = Vertex(name = 'V_298',
               particles = [ P.sdR__tilde__, P.sdR, P.smuL__plus__, P.smuL__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_299 = Vertex(name = 'V_299',
               particles = [ P.sdR__tilde__, P.sdR, P.smuR__plus__, P.smuR__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_300 = Vertex(name = 'V_300',
               particles = [ P.sdR__tilde__, P.sdR, P.sne__tilde__, P.sne ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_301 = Vertex(name = 'V_301',
               particles = [ P.sdR__tilde__, P.sdR, P.snm__tilde__, P.snm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_302 = Vertex(name = 'V_302',
               particles = [ P.sdR__tilde__, P.sdR, P.snt__tilde__, P.snt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_303 = Vertex(name = 'V_303',
               particles = [ P.a, P.a, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_304 = Vertex(name = 'V_304',
               particles = [ P.sdR__tilde__, P.sdR, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_98})

V_305 = Vertex(name = 'V_305',
               particles = [ P.sdR__tilde__, P.sdR, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_101})

V_306 = Vertex(name = 'V_306',
               particles = [ P.sdR__tilde__, P.sdR, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_101})

V_307 = Vertex(name = 'V_307',
               particles = [ P.sdR__tilde__, P.sdR, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_104})

V_308 = Vertex(name = 'V_308',
               particles = [ P.sbR__tilde__, P.sbR, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_53,(1,0):C.GC_172})

V_309 = Vertex(name = 'V_309',
               particles = [ P.scL__tilde__, P.scL, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_310 = Vertex(name = 'V_310',
               particles = [ P.scR__tilde__, P.scR, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_311 = Vertex(name = 'V_311',
               particles = [ P.sbL__tilde__, P.sbL, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_312 = Vertex(name = 'V_312',
               particles = [ P.sdL__tilde__, P.sdL, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_313 = Vertex(name = 'V_313',
               particles = [ P.sdR__tilde__, P.sdR__tilde__, P.sdR, P.sdR ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_53,(0,0):C.GC_53,(3,0):C.GC_172,(2,0):C.GC_172})

V_314 = Vertex(name = 'V_314',
               particles = [ P.a, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_315 = Vertex(name = 'V_315',
               particles = [ P.n1, P.s, P.ssL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_148})

V_316 = Vertex(name = 'V_316',
               particles = [ P.n2, P.s, P.ssL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_152})

V_317 = Vertex(name = 'V_317',
               particles = [ P.n3, P.s, P.ssL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_156})

V_318 = Vertex(name = 'V_318',
               particles = [ P.n4, P.s, P.ssL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_160})

V_319 = Vertex(name = 'V_319',
               particles = [ P.scL, P.seL__minus__, P.sne__tilde__, P.ssL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_320 = Vertex(name = 'V_320',
               particles = [ P.scL, P.smuL__minus__, P.snm__tilde__, P.ssL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_321 = Vertex(name = 'V_321',
               particles = [ P.scL, P.snt__tilde__, P.ssL__tilde__, P.stau1__minus__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_322 = Vertex(name = 'V_322',
               particles = [ P.scL, P.snt__tilde__, P.ssL__tilde__, P.stau2__minus__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_323 = Vertex(name = 'V_323',
               particles = [ P.s__tilde__, P.n1, P.ssL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_148})

V_324 = Vertex(name = 'V_324',
               particles = [ P.s__tilde__, P.n2, P.ssL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_152})

V_325 = Vertex(name = 'V_325',
               particles = [ P.s__tilde__, P.n3, P.ssL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_156})

V_326 = Vertex(name = 'V_326',
               particles = [ P.s__tilde__, P.n4, P.ssL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_160})

V_327 = Vertex(name = 'V_327',
               particles = [ P.scL__tilde__, P.seL__plus__, P.sne, P.ssL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_328 = Vertex(name = 'V_328',
               particles = [ P.scL__tilde__, P.smuL__plus__, P.snm, P.ssL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_329 = Vertex(name = 'V_329',
               particles = [ P.scL__tilde__, P.snt, P.ssL, P.stau1__plus__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_330 = Vertex(name = 'V_330',
               particles = [ P.scL__tilde__, P.snt, P.ssL, P.stau2__plus__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_331 = Vertex(name = 'V_331',
               particles = [ P.seL__plus__, P.seL__minus__, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_332 = Vertex(name = 'V_332',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_333 = Vertex(name = 'V_333',
               particles = [ P.sne__tilde__, P.sne, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_334 = Vertex(name = 'V_334',
               particles = [ P.snm__tilde__, P.snm, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_335 = Vertex(name = 'V_335',
               particles = [ P.snt__tilde__, P.snt, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_336 = Vertex(name = 'V_336',
               particles = [ P.seR__plus__, P.seR__minus__, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_337 = Vertex(name = 'V_337',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_338 = Vertex(name = 'V_338',
               particles = [ P.a, P.a, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_339 = Vertex(name = 'V_339',
               particles = [ P.ssL__tilde__, P.ssL, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_115})

V_340 = Vertex(name = 'V_340',
               particles = [ P.ssL__tilde__, P.ssL, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_119})

V_341 = Vertex(name = 'V_341',
               particles = [ P.ssL__tilde__, P.ssL, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_119})

V_342 = Vertex(name = 'V_342',
               particles = [ P.ssL__tilde__, P.ssL, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_123})

V_343 = Vertex(name = 'V_343',
               particles = [ P.sbL__tilde__, P.sbL, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_110,(1,0):C.GC_172})

V_344 = Vertex(name = 'V_344',
               particles = [ P.sbR__tilde__, P.sbR, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_345 = Vertex(name = 'V_345',
               particles = [ P.scL__tilde__, P.scL, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_112,(0,0):C.GC_108,(2,0):C.GC_172})

V_346 = Vertex(name = 'V_346',
               particles = [ P.scR__tilde__, P.scR, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_347 = Vertex(name = 'V_347',
               particles = [ P.sdL__tilde__, P.sdL, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_110,(1,0):C.GC_172})

V_348 = Vertex(name = 'V_348',
               particles = [ P.sdR__tilde__, P.sdR, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_349 = Vertex(name = 'V_349',
               particles = [ P.ssL__tilde__, P.ssL__tilde__, P.ssL, P.ssL ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_110,(0,0):C.GC_110,(3,0):C.GC_172,(2,0):C.GC_172})

V_350 = Vertex(name = 'V_350',
               particles = [ P.a, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_351 = Vertex(name = 'V_351',
               particles = [ P.n1, P.s, P.ssR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_65})

V_352 = Vertex(name = 'V_352',
               particles = [ P.n2, P.s, P.ssR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_68})

V_353 = Vertex(name = 'V_353',
               particles = [ P.n3, P.s, P.ssR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_71})

V_354 = Vertex(name = 'V_354',
               particles = [ P.n4, P.s, P.ssR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_74})

V_355 = Vertex(name = 'V_355',
               particles = [ P.s__tilde__, P.n1, P.ssR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_65})

V_356 = Vertex(name = 'V_356',
               particles = [ P.s__tilde__, P.n2, P.ssR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_68})

V_357 = Vertex(name = 'V_357',
               particles = [ P.s__tilde__, P.n3, P.ssR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_71})

V_358 = Vertex(name = 'V_358',
               particles = [ P.s__tilde__, P.n4, P.ssR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_74})

V_359 = Vertex(name = 'V_359',
               particles = [ P.seL__plus__, P.seL__minus__, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_360 = Vertex(name = 'V_360',
               particles = [ P.seR__plus__, P.seR__minus__, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_361 = Vertex(name = 'V_361',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_362 = Vertex(name = 'V_362',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_363 = Vertex(name = 'V_363',
               particles = [ P.sne__tilde__, P.sne, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_364 = Vertex(name = 'V_364',
               particles = [ P.snm__tilde__, P.snm, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_365 = Vertex(name = 'V_365',
               particles = [ P.snt__tilde__, P.snt, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_366 = Vertex(name = 'V_366',
               particles = [ P.a, P.a, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_367 = Vertex(name = 'V_367',
               particles = [ P.ssR__tilde__, P.ssR, P.stau1__plus__, P.stau1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_98})

V_368 = Vertex(name = 'V_368',
               particles = [ P.ssR__tilde__, P.ssR, P.stau1__minus__, P.stau2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_101})

V_369 = Vertex(name = 'V_369',
               particles = [ P.ssR__tilde__, P.ssR, P.stau1__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_101})

V_370 = Vertex(name = 'V_370',
               particles = [ P.ssR__tilde__, P.ssR, P.stau2__plus__, P.stau2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_104})

V_371 = Vertex(name = 'V_371',
               particles = [ P.sbR__tilde__, P.sbR, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_53,(1,0):C.GC_172})

V_372 = Vertex(name = 'V_372',
               particles = [ P.scL__tilde__, P.scL, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_373 = Vertex(name = 'V_373',
               particles = [ P.scR__tilde__, P.scR, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_374 = Vertex(name = 'V_374',
               particles = [ P.sdR__tilde__, P.sdR, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_53,(1,0):C.GC_172})

V_375 = Vertex(name = 'V_375',
               particles = [ P.sbL__tilde__, P.sbL, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_376 = Vertex(name = 'V_376',
               particles = [ P.sdL__tilde__, P.sdL, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_377 = Vertex(name = 'V_377',
               particles = [ P.ssL__tilde__, P.ssL, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_378 = Vertex(name = 'V_378',
               particles = [ P.ssR__tilde__, P.ssR__tilde__, P.ssR, P.ssR ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_53,(0,0):C.GC_53,(3,0):C.GC_172,(2,0):C.GC_172})

V_379 = Vertex(name = 'V_379',
               particles = [ P.a, P.stL__tilde__, P.stL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_380 = Vertex(name = 'V_380',
               particles = [ P.n1, P.t, P.stL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_242,(0,1):C.GC_146})

V_381 = Vertex(name = 'V_381',
               particles = [ P.n2, P.t, P.stL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_243,(0,1):C.GC_150})

V_382 = Vertex(name = 'V_382',
               particles = [ P.n3, P.t, P.stL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_244,(0,1):C.GC_154})

V_383 = Vertex(name = 'V_383',
               particles = [ P.n4, P.t, P.stL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_245,(0,1):C.GC_158})

V_384 = Vertex(name = 'V_384',
               particles = [ P.sbL, P.seL__plus__, P.sne, P.stL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_385 = Vertex(name = 'V_385',
               particles = [ P.sbL, P.smuL__plus__, P.snm, P.stL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_386 = Vertex(name = 'V_386',
               particles = [ P.sbL, P.snt, P.stau1__plus__, P.stL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_387 = Vertex(name = 'V_387',
               particles = [ P.sbL, P.snt, P.stau2__plus__, P.stL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_388 = Vertex(name = 'V_388',
               particles = [ P.sbL, P.scL, P.ssL__tilde__, P.stL__tilde__ ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_389 = Vertex(name = 'V_389',
               particles = [ P.t__tilde__, P.n1, P.stL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_242,(0,0):C.GC_146})

V_390 = Vertex(name = 'V_390',
               particles = [ P.t__tilde__, P.n2, P.stL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_243,(0,0):C.GC_150})

V_391 = Vertex(name = 'V_391',
               particles = [ P.t__tilde__, P.n3, P.stL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_244,(0,0):C.GC_154})

V_392 = Vertex(name = 'V_392',
               particles = [ P.t__tilde__, P.n4, P.stL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_245,(0,0):C.GC_158})

V_393 = Vertex(name = 'V_393',
               particles = [ P.sbL__tilde__, P.seL__minus__, P.sne__tilde__, P.stL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_394 = Vertex(name = 'V_394',
               particles = [ P.sbL__tilde__, P.smuL__minus__, P.snm__tilde__, P.stL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_395 = Vertex(name = 'V_395',
               particles = [ P.sbL__tilde__, P.snt__tilde__, P.stau1__minus__, P.stL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_396 = Vertex(name = 'V_396',
               particles = [ P.sbL__tilde__, P.snt__tilde__, P.stau2__minus__, P.stL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_397 = Vertex(name = 'V_397',
               particles = [ P.sbL__tilde__, P.scL__tilde__, P.ssL, P.stL ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_398 = Vertex(name = 'V_398',
               particles = [ P.seL__plus__, P.seL__minus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_399 = Vertex(name = 'V_399',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_400 = Vertex(name = 'V_400',
               particles = [ P.sne__tilde__, P.sne, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_401 = Vertex(name = 'V_401',
               particles = [ P.snm__tilde__, P.snm, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_402 = Vertex(name = 'V_402',
               particles = [ P.snt__tilde__, P.snt, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_403 = Vertex(name = 'V_403',
               particles = [ P.seR__plus__, P.seR__minus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_404 = Vertex(name = 'V_404',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_405 = Vertex(name = 'V_405',
               particles = [ P.a, P.a, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_406 = Vertex(name = 'V_406',
               particles = [ P.stau1__plus__, P.stau1__minus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_113})

V_407 = Vertex(name = 'V_407',
               particles = [ P.stau1__minus__, P.stau2__plus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_117})

V_408 = Vertex(name = 'V_408',
               particles = [ P.stau1__plus__, P.stau2__minus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_117})

V_409 = Vertex(name = 'V_409',
               particles = [ P.stau2__plus__, P.stau2__minus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_121})

V_410 = Vertex(name = 'V_410',
               particles = [ P.scL__tilde__, P.scL, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_110,(1,0):C.GC_172})

V_411 = Vertex(name = 'V_411',
               particles = [ P.scR__tilde__, P.scR, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_412 = Vertex(name = 'V_412',
               particles = [ P.sbL__tilde__, P.sbL, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_112,(0,0):C.GC_108,(2,0):C.GC_172})

V_413 = Vertex(name = 'V_413',
               particles = [ P.sbR__tilde__, P.sbR, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_414 = Vertex(name = 'V_414',
               particles = [ P.sdL__tilde__, P.sdL, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_108,(1,0):C.GC_172})

V_415 = Vertex(name = 'V_415',
               particles = [ P.sdR__tilde__, P.sdR, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_416 = Vertex(name = 'V_416',
               particles = [ P.ssL__tilde__, P.ssL, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_108,(1,0):C.GC_172})

V_417 = Vertex(name = 'V_417',
               particles = [ P.ssR__tilde__, P.ssR, P.stL__tilde__, P.stL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_418 = Vertex(name = 'V_418',
               particles = [ P.stL__tilde__, P.stL__tilde__, P.stL, P.stL ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_110,(0,0):C.GC_110,(3,0):C.GC_172,(2,0):C.GC_172})

V_419 = Vertex(name = 'V_419',
               particles = [ P.a, P.stR__tilde__, P.stR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_420 = Vertex(name = 'V_420',
               particles = [ P.n1, P.t, P.stR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_242,(0,0):C.GC_66})

V_421 = Vertex(name = 'V_421',
               particles = [ P.n2, P.t, P.stR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_243,(0,0):C.GC_69})

V_422 = Vertex(name = 'V_422',
               particles = [ P.n3, P.t, P.stR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_244,(0,0):C.GC_72})

V_423 = Vertex(name = 'V_423',
               particles = [ P.n4, P.t, P.stR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_245,(0,0):C.GC_75})

V_424 = Vertex(name = 'V_424',
               particles = [ P.t__tilde__, P.n1, P.stR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_242,(0,1):C.GC_66})

V_425 = Vertex(name = 'V_425',
               particles = [ P.t__tilde__, P.n2, P.stR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_243,(0,1):C.GC_69})

V_426 = Vertex(name = 'V_426',
               particles = [ P.t__tilde__, P.n3, P.stR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_244,(0,1):C.GC_72})

V_427 = Vertex(name = 'V_427',
               particles = [ P.t__tilde__, P.n4, P.stR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_245,(0,1):C.GC_75})

V_428 = Vertex(name = 'V_428',
               particles = [ P.seL__plus__, P.seL__minus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_429 = Vertex(name = 'V_429',
               particles = [ P.seR__plus__, P.seR__minus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_60})

V_430 = Vertex(name = 'V_430',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_431 = Vertex(name = 'V_431',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_60})

V_432 = Vertex(name = 'V_432',
               particles = [ P.sne__tilde__, P.sne, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_433 = Vertex(name = 'V_433',
               particles = [ P.snm__tilde__, P.snm, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_434 = Vertex(name = 'V_434',
               particles = [ P.snt__tilde__, P.snt, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_435 = Vertex(name = 'V_435',
               particles = [ P.a, P.a, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_436 = Vertex(name = 'V_436',
               particles = [ P.stau1__plus__, P.stau1__minus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_99})

V_437 = Vertex(name = 'V_437',
               particles = [ P.stau1__minus__, P.stau2__plus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_102})

V_438 = Vertex(name = 'V_438',
               particles = [ P.stau1__plus__, P.stau2__minus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_102})

V_439 = Vertex(name = 'V_439',
               particles = [ P.stau2__plus__, P.stau2__minus__, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_105})

V_440 = Vertex(name = 'V_440',
               particles = [ P.scR__tilde__, P.scR, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_58,(1,0):C.GC_172})

V_441 = Vertex(name = 'V_441',
               particles = [ P.sbL__tilde__, P.sbL, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_246,(0,0):C.GC_52,(2,0):C.GC_173})

V_442 = Vertex(name = 'V_442',
               particles = [ P.sbR__tilde__, P.sbR, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_443 = Vertex(name = 'V_443',
               particles = [ P.scL__tilde__, P.scL, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_444 = Vertex(name = 'V_444',
               particles = [ P.sdL__tilde__, P.sdL, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_445 = Vertex(name = 'V_445',
               particles = [ P.sdR__tilde__, P.sdR, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_446 = Vertex(name = 'V_446',
               particles = [ P.ssL__tilde__, P.ssL, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_447 = Vertex(name = 'V_447',
               particles = [ P.ssR__tilde__, P.ssR, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_448 = Vertex(name = 'V_448',
               particles = [ P.stL__tilde__, P.stL, P.stR__tilde__, P.stR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_246,(0,0):C.GC_52,(2,0):C.GC_173})

V_449 = Vertex(name = 'V_449',
               particles = [ P.stR__tilde__, P.stR__tilde__, P.stR, P.stR ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_58,(0,0):C.GC_58,(3,0):C.GC_172,(2,0):C.GC_172})

V_450 = Vertex(name = 'V_450',
               particles = [ P.a, P.suL__tilde__, P.suL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_451 = Vertex(name = 'V_451',
               particles = [ P.n1, P.u, P.suL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_146})

V_452 = Vertex(name = 'V_452',
               particles = [ P.n2, P.u, P.suL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_150})

V_453 = Vertex(name = 'V_453',
               particles = [ P.n3, P.u, P.suL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_154})

V_454 = Vertex(name = 'V_454',
               particles = [ P.n4, P.u, P.suL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_158})

V_455 = Vertex(name = 'V_455',
               particles = [ P.sdL, P.seL__plus__, P.sne, P.suL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_456 = Vertex(name = 'V_456',
               particles = [ P.sdL, P.smuL__plus__, P.snm, P.suL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_457 = Vertex(name = 'V_457',
               particles = [ P.sdL, P.snt, P.stau1__plus__, P.suL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_458 = Vertex(name = 'V_458',
               particles = [ P.sdL, P.snt, P.stau2__plus__, P.suL__tilde__ ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_459 = Vertex(name = 'V_459',
               particles = [ P.scL, P.sdL, P.ssL__tilde__, P.suL__tilde__ ],
               color = [ 'Identity(1,3)*Identity(2,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_460 = Vertex(name = 'V_460',
               particles = [ P.sbL__tilde__, P.sdL, P.stL, P.suL__tilde__ ],
               color = [ 'Identity(1,3)*Identity(2,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_461 = Vertex(name = 'V_461',
               particles = [ P.u__tilde__, P.n1, P.suL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_146})

V_462 = Vertex(name = 'V_462',
               particles = [ P.u__tilde__, P.n2, P.suL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_150})

V_463 = Vertex(name = 'V_463',
               particles = [ P.u__tilde__, P.n3, P.suL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_154})

V_464 = Vertex(name = 'V_464',
               particles = [ P.u__tilde__, P.n4, P.suL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_158})

V_465 = Vertex(name = 'V_465',
               particles = [ P.sdL__tilde__, P.seL__minus__, P.sne__tilde__, P.suL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_466 = Vertex(name = 'V_466',
               particles = [ P.sdL__tilde__, P.smuL__minus__, P.snm__tilde__, P.suL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_467 = Vertex(name = 'V_467',
               particles = [ P.sdL__tilde__, P.snt__tilde__, P.stau1__minus__, P.suL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_468 = Vertex(name = 'V_468',
               particles = [ P.sdL__tilde__, P.snt__tilde__, P.stau2__minus__, P.suL ],
               color = [ 'Identity(1,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_469 = Vertex(name = 'V_469',
               particles = [ P.scL__tilde__, P.sdL__tilde__, P.ssL, P.suL ],
               color = [ 'Identity(1,3)*Identity(2,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_470 = Vertex(name = 'V_470',
               particles = [ P.sbL, P.sdL__tilde__, P.stL__tilde__, P.suL ],
               color = [ 'Identity(1,3)*Identity(2,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_471 = Vertex(name = 'V_471',
               particles = [ P.seL__plus__, P.seL__minus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_472 = Vertex(name = 'V_472',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_473 = Vertex(name = 'V_473',
               particles = [ P.sne__tilde__, P.sne, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_474 = Vertex(name = 'V_474',
               particles = [ P.snm__tilde__, P.snm, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_475 = Vertex(name = 'V_475',
               particles = [ P.snt__tilde__, P.snt, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_476 = Vertex(name = 'V_476',
               particles = [ P.seR__plus__, P.seR__minus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_477 = Vertex(name = 'V_477',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_478 = Vertex(name = 'V_478',
               particles = [ P.a, P.a, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_479 = Vertex(name = 'V_479',
               particles = [ P.stau1__plus__, P.stau1__minus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_113})

V_480 = Vertex(name = 'V_480',
               particles = [ P.stau1__minus__, P.stau2__plus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_117})

V_481 = Vertex(name = 'V_481',
               particles = [ P.stau1__plus__, P.stau2__minus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_117})

V_482 = Vertex(name = 'V_482',
               particles = [ P.stau2__plus__, P.stau2__minus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_121})

V_483 = Vertex(name = 'V_483',
               particles = [ P.scL__tilde__, P.scL, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_110,(1,0):C.GC_172})

V_484 = Vertex(name = 'V_484',
               particles = [ P.scR__tilde__, P.scR, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_485 = Vertex(name = 'V_485',
               particles = [ P.stL__tilde__, P.stL, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_110,(1,0):C.GC_172})

V_486 = Vertex(name = 'V_486',
               particles = [ P.stR__tilde__, P.stR, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_487 = Vertex(name = 'V_487',
               particles = [ P.sdL__tilde__, P.sdL, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_112,(0,0):C.GC_108,(2,0):C.GC_172})

V_488 = Vertex(name = 'V_488',
               particles = [ P.sbL__tilde__, P.sbL, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_108,(1,0):C.GC_172})

V_489 = Vertex(name = 'V_489',
               particles = [ P.sbR__tilde__, P.sbR, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_490 = Vertex(name = 'V_490',
               particles = [ P.sdR__tilde__, P.sdR, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_491 = Vertex(name = 'V_491',
               particles = [ P.ssL__tilde__, P.ssL, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_108,(1,0):C.GC_172})

V_492 = Vertex(name = 'V_492',
               particles = [ P.ssR__tilde__, P.ssR, P.suL__tilde__, P.suL ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51,(1,0):C.GC_173})

V_493 = Vertex(name = 'V_493',
               particles = [ P.suL__tilde__, P.suL__tilde__, P.suL, P.suL ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_110,(0,0):C.GC_110,(3,0):C.GC_172,(2,0):C.GC_172})

V_494 = Vertex(name = 'V_494',
               particles = [ P.a, P.suR__tilde__, P.suR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_495 = Vertex(name = 'V_495',
               particles = [ P.n1, P.u, P.suR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_66})

V_496 = Vertex(name = 'V_496',
               particles = [ P.n2, P.u, P.suR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_69})

V_497 = Vertex(name = 'V_497',
               particles = [ P.n3, P.u, P.suR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_72})

V_498 = Vertex(name = 'V_498',
               particles = [ P.n4, P.u, P.suR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_75})

V_499 = Vertex(name = 'V_499',
               particles = [ P.u__tilde__, P.n1, P.suR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_66})

V_500 = Vertex(name = 'V_500',
               particles = [ P.u__tilde__, P.n2, P.suR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_69})

V_501 = Vertex(name = 'V_501',
               particles = [ P.u__tilde__, P.n3, P.suR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_72})

V_502 = Vertex(name = 'V_502',
               particles = [ P.u__tilde__, P.n4, P.suR ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_75})

V_503 = Vertex(name = 'V_503',
               particles = [ P.seL__plus__, P.seL__minus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_504 = Vertex(name = 'V_504',
               particles = [ P.seR__plus__, P.seR__minus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_60})

V_505 = Vertex(name = 'V_505',
               particles = [ P.smuL__plus__, P.smuL__minus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_506 = Vertex(name = 'V_506',
               particles = [ P.smuR__plus__, P.smuR__minus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_60})

V_507 = Vertex(name = 'V_507',
               particles = [ P.sne__tilde__, P.sne, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_508 = Vertex(name = 'V_508',
               particles = [ P.snm__tilde__, P.snm, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_509 = Vertex(name = 'V_509',
               particles = [ P.snt__tilde__, P.snt, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_510 = Vertex(name = 'V_510',
               particles = [ P.a, P.a, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_511 = Vertex(name = 'V_511',
               particles = [ P.stau1__plus__, P.stau1__minus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_99})

V_512 = Vertex(name = 'V_512',
               particles = [ P.stau1__minus__, P.stau2__plus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_102})

V_513 = Vertex(name = 'V_513',
               particles = [ P.stau1__plus__, P.stau2__minus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_102})

V_514 = Vertex(name = 'V_514',
               particles = [ P.stau2__plus__, P.stau2__minus__, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_105})

V_515 = Vertex(name = 'V_515',
               particles = [ P.scR__tilde__, P.scR, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_58,(1,0):C.GC_172})

V_516 = Vertex(name = 'V_516',
               particles = [ P.stR__tilde__, P.stR, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_58,(1,0):C.GC_172})

V_517 = Vertex(name = 'V_517',
               particles = [ P.sbL__tilde__, P.sbL, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_518 = Vertex(name = 'V_518',
               particles = [ P.sbR__tilde__, P.sbR, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_519 = Vertex(name = 'V_519',
               particles = [ P.scL__tilde__, P.scL, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_520 = Vertex(name = 'V_520',
               particles = [ P.sdL__tilde__, P.sdL, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_521 = Vertex(name = 'V_521',
               particles = [ P.sdR__tilde__, P.sdR, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_522 = Vertex(name = 'V_522',
               particles = [ P.ssL__tilde__, P.ssL, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_523 = Vertex(name = 'V_523',
               particles = [ P.ssR__tilde__, P.ssR, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56,(1,0):C.GC_172})

V_524 = Vertex(name = 'V_524',
               particles = [ P.stL__tilde__, P.stL, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_525 = Vertex(name = 'V_525',
               particles = [ P.suL__tilde__, P.suL, P.suR__tilde__, P.suR ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52,(1,0):C.GC_173})

V_526 = Vertex(name = 'V_526',
               particles = [ P.suR__tilde__, P.suR__tilde__, P.suR, P.suR ],
               color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,3,1)*T(-1,4,2)', 'T(-1,3,2)*T(-1,4,1)' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(1,0):C.GC_58,(0,0):C.GC_58,(3,0):C.GC_172,(2,0):C.GC_172})

V_527 = Vertex(name = 'V_527',
               particles = [ P.g, P.sbL__tilde__, P.sbL ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_528 = Vertex(name = 'V_528',
               particles = [ P.go, P.b, P.sbL__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_15})

V_529 = Vertex(name = 'V_529',
               particles = [ P.g, P.sbR__tilde__, P.sbR ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_530 = Vertex(name = 'V_530',
               particles = [ P.go, P.b, P.sbR__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_16})

V_531 = Vertex(name = 'V_531',
               particles = [ P.g, P.scL__tilde__, P.scL ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_532 = Vertex(name = 'V_532',
               particles = [ P.go, P.c, P.scL__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_15})

V_533 = Vertex(name = 'V_533',
               particles = [ P.g, P.scR__tilde__, P.scR ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_534 = Vertex(name = 'V_534',
               particles = [ P.go, P.c, P.scR__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_16})

V_535 = Vertex(name = 'V_535',
               particles = [ P.g, P.sdL__tilde__, P.sdL ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_536 = Vertex(name = 'V_536',
               particles = [ P.go, P.d, P.sdL__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_15})

V_537 = Vertex(name = 'V_537',
               particles = [ P.g, P.sdR__tilde__, P.sdR ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_538 = Vertex(name = 'V_538',
               particles = [ P.go, P.d, P.sdR__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_16})

V_539 = Vertex(name = 'V_539',
               particles = [ P.g, P.ssL__tilde__, P.ssL ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_540 = Vertex(name = 'V_540',
               particles = [ P.go, P.s, P.ssL__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_15})

V_541 = Vertex(name = 'V_541',
               particles = [ P.g, P.ssR__tilde__, P.ssR ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_542 = Vertex(name = 'V_542',
               particles = [ P.go, P.s, P.ssR__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_16})

V_543 = Vertex(name = 'V_543',
               particles = [ P.g, P.stL__tilde__, P.stL ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_544 = Vertex(name = 'V_544',
               particles = [ P.go, P.t, P.stL__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_15})

V_545 = Vertex(name = 'V_545',
               particles = [ P.g, P.stR__tilde__, P.stR ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_546 = Vertex(name = 'V_546',
               particles = [ P.go, P.t, P.stR__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_16})

V_547 = Vertex(name = 'V_547',
               particles = [ P.g, P.suL__tilde__, P.suL ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_548 = Vertex(name = 'V_548',
               particles = [ P.go, P.u, P.suL__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_15})

V_549 = Vertex(name = 'V_549',
               particles = [ P.g, P.suR__tilde__, P.suR ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_12})

V_550 = Vertex(name = 'V_550',
               particles = [ P.go, P.u, P.suR__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_16})

V_551 = Vertex(name = 'V_551',
               particles = [ P.b__tilde__, P.go, P.sbL ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_15})

V_552 = Vertex(name = 'V_552',
               particles = [ P.a, P.g, P.sbL__tilde__, P.sbL ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_17})

V_553 = Vertex(name = 'V_553',
               particles = [ P.b__tilde__, P.go, P.sbR ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_16})

V_554 = Vertex(name = 'V_554',
               particles = [ P.a, P.g, P.sbR__tilde__, P.sbR ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_17})

V_555 = Vertex(name = 'V_555',
               particles = [ P.c__tilde__, P.go, P.scL ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_15})

V_556 = Vertex(name = 'V_556',
               particles = [ P.a, P.g, P.scL__tilde__, P.scL ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_557 = Vertex(name = 'V_557',
               particles = [ P.c__tilde__, P.go, P.scR ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_16})

V_558 = Vertex(name = 'V_558',
               particles = [ P.a, P.g, P.scR__tilde__, P.scR ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_559 = Vertex(name = 'V_559',
               particles = [ P.d__tilde__, P.go, P.sdL ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_15})

V_560 = Vertex(name = 'V_560',
               particles = [ P.a, P.g, P.sdL__tilde__, P.sdL ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_17})

V_561 = Vertex(name = 'V_561',
               particles = [ P.d__tilde__, P.go, P.sdR ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_16})

V_562 = Vertex(name = 'V_562',
               particles = [ P.a, P.g, P.sdR__tilde__, P.sdR ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_17})

V_563 = Vertex(name = 'V_563',
               particles = [ P.s__tilde__, P.go, P.ssL ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_15})

V_564 = Vertex(name = 'V_564',
               particles = [ P.a, P.g, P.ssL__tilde__, P.ssL ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_17})

V_565 = Vertex(name = 'V_565',
               particles = [ P.s__tilde__, P.go, P.ssR ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_16})

V_566 = Vertex(name = 'V_566',
               particles = [ P.a, P.g, P.ssR__tilde__, P.ssR ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_17})

V_567 = Vertex(name = 'V_567',
               particles = [ P.t__tilde__, P.go, P.stL ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_15})

V_568 = Vertex(name = 'V_568',
               particles = [ P.a, P.g, P.stL__tilde__, P.stL ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_569 = Vertex(name = 'V_569',
               particles = [ P.t__tilde__, P.go, P.stR ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_16})

V_570 = Vertex(name = 'V_570',
               particles = [ P.a, P.g, P.stR__tilde__, P.stR ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_571 = Vertex(name = 'V_571',
               particles = [ P.u__tilde__, P.go, P.suL ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_15})

V_572 = Vertex(name = 'V_572',
               particles = [ P.a, P.g, P.suL__tilde__, P.suL ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_573 = Vertex(name = 'V_573',
               particles = [ P.u__tilde__, P.go, P.suR ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_16})

V_574 = Vertex(name = 'V_574',
               particles = [ P.a, P.g, P.suR__tilde__, P.suR ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_575 = Vertex(name = 'V_575',
               particles = [ P.g, P.g, P.sbR__tilde__, P.sbR ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_576 = Vertex(name = 'V_576',
               particles = [ P.g, P.g, P.scR__tilde__, P.scR ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_577 = Vertex(name = 'V_577',
               particles = [ P.g, P.g, P.sdR__tilde__, P.sdR ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_578 = Vertex(name = 'V_578',
               particles = [ P.g, P.g, P.ssR__tilde__, P.ssR ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_579 = Vertex(name = 'V_579',
               particles = [ P.g, P.g, P.stR__tilde__, P.stR ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_580 = Vertex(name = 'V_580',
               particles = [ P.g, P.g, P.suR__tilde__, P.suR ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_581 = Vertex(name = 'V_581',
               particles = [ P.g, P.g, P.sbL__tilde__, P.sbL ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_582 = Vertex(name = 'V_582',
               particles = [ P.g, P.g, P.scL__tilde__, P.scL ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_583 = Vertex(name = 'V_583',
               particles = [ P.g, P.g, P.sdL__tilde__, P.sdL ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_584 = Vertex(name = 'V_584',
               particles = [ P.g, P.g, P.ssL__tilde__, P.ssL ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_585 = Vertex(name = 'V_585',
               particles = [ P.g, P.g, P.stL__tilde__, P.stL ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_586 = Vertex(name = 'V_586',
               particles = [ P.g, P.g, P.suL__tilde__, P.suL ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_19,(0,0):C.GC_19})

V_587 = Vertex(name = 'V_587',
               particles = [ P.ve__tilde__, P.x1__plus__, P.seL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_177})

V_588 = Vertex(name = 'V_588',
               particles = [ P.vm__tilde__, P.x1__plus__, P.smuL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_177})

V_589 = Vertex(name = 'V_589',
               particles = [ P.x1__minus__, P.ve, P.seL__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_177})

V_590 = Vertex(name = 'V_590',
               particles = [ P.x1__minus__, P.vm, P.smuL__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_177})

V_591 = Vertex(name = 'V_591',
               particles = [ P.vt__tilde__, P.x1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_227})

V_592 = Vertex(name = 'V_592',
               particles = [ P.x1__minus__, P.vt, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_227})

V_593 = Vertex(name = 'V_593',
               particles = [ P.vt__tilde__, P.x1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_228})

V_594 = Vertex(name = 'V_594',
               particles = [ P.x1__minus__, P.vt, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_228})

V_595 = Vertex(name = 'V_595',
               particles = [ P.x1__minus__, P.t, P.sbL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_177})

V_596 = Vertex(name = 'V_596',
               particles = [ P.t__tilde__, P.x1__plus__, P.sbL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_177,(0,1):C.GC_240})

V_597 = Vertex(name = 'V_597',
               particles = [ P.x1__minus__, P.u, P.sdL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_177})

V_598 = Vertex(name = 'V_598',
               particles = [ P.u__tilde__, P.x1__plus__, P.sdL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_177})

V_599 = Vertex(name = 'V_599',
               particles = [ P.x1__minus__, P.c, P.ssL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_177})

V_600 = Vertex(name = 'V_600',
               particles = [ P.c__tilde__, P.x1__plus__, P.ssL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_177})

V_601 = Vertex(name = 'V_601',
               particles = [ P.ve__tilde__, P.x2__plus__, P.seL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_184})

V_602 = Vertex(name = 'V_602',
               particles = [ P.vm__tilde__, P.x2__plus__, P.smuL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_184})

V_603 = Vertex(name = 'V_603',
               particles = [ P.x2__minus__, P.ve, P.seL__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_184})

V_604 = Vertex(name = 'V_604',
               particles = [ P.x2__minus__, P.vm, P.smuL__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_184})

V_605 = Vertex(name = 'V_605',
               particles = [ P.vt__tilde__, P.x2__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_229})

V_606 = Vertex(name = 'V_606',
               particles = [ P.x2__minus__, P.vt, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_229})

V_607 = Vertex(name = 'V_607',
               particles = [ P.vt__tilde__, P.x2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_230})

V_608 = Vertex(name = 'V_608',
               particles = [ P.x2__minus__, P.vt, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_230})

V_609 = Vertex(name = 'V_609',
               particles = [ P.x2__minus__, P.t, P.sbL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_241,(0,1):C.GC_184})

V_610 = Vertex(name = 'V_610',
               particles = [ P.t__tilde__, P.x2__plus__, P.sbL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_184,(0,1):C.GC_241})

V_611 = Vertex(name = 'V_611',
               particles = [ P.x2__minus__, P.u, P.sdL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_184})

V_612 = Vertex(name = 'V_612',
               particles = [ P.u__tilde__, P.x2__plus__, P.sdL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_184})

V_613 = Vertex(name = 'V_613',
               particles = [ P.x2__minus__, P.c, P.ssL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_184})

V_614 = Vertex(name = 'V_614',
               particles = [ P.c__tilde__, P.x2__plus__, P.ssL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_184})

V_615 = Vertex(name = 'V_615',
               particles = [ P.e__plus__, P.x1__minus__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_193})

V_616 = Vertex(name = 'V_616',
               particles = [ P.mu__plus__, P.x1__minus__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_193})

V_617 = Vertex(name = 'V_617',
               particles = [ P.tau__plus__, P.x1__minus__, P.snt ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_193,(0,1):C.GC_209})

V_618 = Vertex(name = 'V_618',
               particles = [ P.e__minus__, P.x1__plus__, P.sne__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_193})

V_619 = Vertex(name = 'V_619',
               particles = [ P.mu__minus__, P.x1__plus__, P.snm__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_193})

V_620 = Vertex(name = 'V_620',
               particles = [ P.tau__minus__, P.x1__plus__, P.snt__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_209,(0,1):C.GC_193})

V_621 = Vertex(name = 'V_621',
               particles = [ P.s, P.x1__plus__, P.scL__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_193})

V_622 = Vertex(name = 'V_622',
               particles = [ P.s__tilde__, P.x1__minus__, P.scL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_193})

V_623 = Vertex(name = 'V_623',
               particles = [ P.x1__plus__, P.b, P.stL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_193})

V_624 = Vertex(name = 'V_624',
               particles = [ P.x1__minus__, P.b__tilde__, P.stL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_193})

V_625 = Vertex(name = 'V_625',
               particles = [ P.d, P.x1__plus__, P.suL__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_193})

V_626 = Vertex(name = 'V_626',
               particles = [ P.d__tilde__, P.x1__minus__, P.suL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_193})

V_627 = Vertex(name = 'V_627',
               particles = [ P.e__plus__, P.x2__minus__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_200})

V_628 = Vertex(name = 'V_628',
               particles = [ P.mu__plus__, P.x2__minus__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_200})

V_629 = Vertex(name = 'V_629',
               particles = [ P.tau__plus__, P.x2__minus__, P.snt ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_200,(0,1):C.GC_210})

V_630 = Vertex(name = 'V_630',
               particles = [ P.e__minus__, P.x2__plus__, P.sne__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_200})

V_631 = Vertex(name = 'V_631',
               particles = [ P.mu__minus__, P.x2__plus__, P.snm__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_200})

V_632 = Vertex(name = 'V_632',
               particles = [ P.tau__minus__, P.x2__plus__, P.snt__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_210,(0,1):C.GC_200})

V_633 = Vertex(name = 'V_633',
               particles = [ P.s, P.x2__plus__, P.scL__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_200})

V_634 = Vertex(name = 'V_634',
               particles = [ P.s__tilde__, P.x2__minus__, P.scL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_200})

V_635 = Vertex(name = 'V_635',
               particles = [ P.x2__plus__, P.b, P.stL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_200})

V_636 = Vertex(name = 'V_636',
               particles = [ P.x2__minus__, P.b__tilde__, P.stL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_200})

V_637 = Vertex(name = 'V_637',
               particles = [ P.d, P.x2__plus__, P.suL__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_200})

V_638 = Vertex(name = 'V_638',
               particles = [ P.d__tilde__, P.x2__minus__, P.suL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_200})

V_639 = Vertex(name = 'V_639',
               particles = [ P.a, P.W__minus__, P.seL__plus__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_41})

V_640 = Vertex(name = 'V_640',
               particles = [ P.a, P.W__minus__, P.smuL__plus__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_41})

V_641 = Vertex(name = 'V_641',
               particles = [ P.W__minus__, P.seL__plus__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_37})

V_642 = Vertex(name = 'V_642',
               particles = [ P.W__minus__, P.smuL__plus__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_37})

V_643 = Vertex(name = 'V_643',
               particles = [ P.a, P.W__minus__, P.snt, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_47})

V_644 = Vertex(name = 'V_644',
               particles = [ P.W__minus__, P.snt, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_46})

V_645 = Vertex(name = 'V_645',
               particles = [ P.a, P.W__minus__, P.snt, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_50})

V_646 = Vertex(name = 'V_646',
               particles = [ P.W__minus__, P.snt, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_49})

V_647 = Vertex(name = 'V_647',
               particles = [ P.W__minus__, P.sbL__tilde__, P.stL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_37})

V_648 = Vertex(name = 'V_648',
               particles = [ P.W__minus__, P.scL, P.ssL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_38})

V_649 = Vertex(name = 'V_649',
               particles = [ P.W__minus__, P.sdL__tilde__, P.suL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_37})

V_650 = Vertex(name = 'V_650',
               particles = [ P.a, P.W__minus__, P.scL, P.ssL__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_651 = Vertex(name = 'V_651',
               particles = [ P.a, P.W__minus__, P.sbL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_652 = Vertex(name = 'V_652',
               particles = [ P.a, P.W__minus__, P.sdL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_653 = Vertex(name = 'V_653',
               particles = [ P.g, P.W__minus__, P.scL, P.ssL__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_44})

V_654 = Vertex(name = 'V_654',
               particles = [ P.g, P.W__minus__, P.sbL__tilde__, P.stL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_44})

V_655 = Vertex(name = 'V_655',
               particles = [ P.g, P.W__minus__, P.sdL__tilde__, P.suL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_44})

V_656 = Vertex(name = 'V_656',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_6})

V_657 = Vertex(name = 'V_657',
               particles = [ P.a, P.W__plus__, P.seL__minus__, P.sne__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_41})

V_658 = Vertex(name = 'V_658',
               particles = [ P.a, P.W__plus__, P.smuL__minus__, P.snm__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_41})

V_659 = Vertex(name = 'V_659',
               particles = [ P.W__plus__, P.seL__minus__, P.sne__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_38})

V_660 = Vertex(name = 'V_660',
               particles = [ P.W__plus__, P.smuL__minus__, P.snm__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_38})

V_661 = Vertex(name = 'V_661',
               particles = [ P.a, P.W__plus__, P.snt__tilde__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_47})

V_662 = Vertex(name = 'V_662',
               particles = [ P.W__plus__, P.snt__tilde__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_45})

V_663 = Vertex(name = 'V_663',
               particles = [ P.a, P.W__plus__, P.snt__tilde__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_50})

V_664 = Vertex(name = 'V_664',
               particles = [ P.W__plus__, P.snt__tilde__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_48})

V_665 = Vertex(name = 'V_665',
               particles = [ P.W__plus__, P.sbL, P.stL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_38})

V_666 = Vertex(name = 'V_666',
               particles = [ P.W__plus__, P.scL__tilde__, P.ssL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_37})

V_667 = Vertex(name = 'V_667',
               particles = [ P.W__plus__, P.sdL, P.suL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_38})

V_668 = Vertex(name = 'V_668',
               particles = [ P.a, P.W__plus__, P.scL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_669 = Vertex(name = 'V_669',
               particles = [ P.a, P.W__plus__, P.sbL, P.stL__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_670 = Vertex(name = 'V_670',
               particles = [ P.a, P.W__plus__, P.sdL, P.suL__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_671 = Vertex(name = 'V_671',
               particles = [ P.g, P.W__plus__, P.scL__tilde__, P.ssL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_44})

V_672 = Vertex(name = 'V_672',
               particles = [ P.g, P.W__plus__, P.sbL, P.stL__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_44})

V_673 = Vertex(name = 'V_673',
               particles = [ P.g, P.W__plus__, P.sdL, P.suL__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_44})

V_674 = Vertex(name = 'V_674',
               particles = [ P.W__minus__, P.W__plus__, P.seL__plus__, P.seL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_675 = Vertex(name = 'V_675',
               particles = [ P.W__minus__, P.W__plus__, P.smuL__plus__, P.smuL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_676 = Vertex(name = 'V_676',
               particles = [ P.W__minus__, P.W__plus__, P.sne__tilde__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_677 = Vertex(name = 'V_677',
               particles = [ P.W__minus__, P.W__plus__, P.snm__tilde__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_678 = Vertex(name = 'V_678',
               particles = [ P.W__minus__, P.W__plus__, P.snt__tilde__, P.snt ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_679 = Vertex(name = 'V_679',
               particles = [ P.W__minus__, P.W__plus__, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_33})

V_680 = Vertex(name = 'V_680',
               particles = [ P.W__minus__, P.W__plus__, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_35})

V_681 = Vertex(name = 'V_681',
               particles = [ P.W__minus__, P.W__plus__, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_35})

V_682 = Vertex(name = 'V_682',
               particles = [ P.W__minus__, P.W__plus__, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_36})

V_683 = Vertex(name = 'V_683',
               particles = [ P.W__minus__, P.W__plus__, P.sbL__tilde__, P.sbL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_684 = Vertex(name = 'V_684',
               particles = [ P.W__minus__, P.W__plus__, P.scL__tilde__, P.scL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_685 = Vertex(name = 'V_685',
               particles = [ P.W__minus__, P.W__plus__, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_686 = Vertex(name = 'V_686',
               particles = [ P.W__minus__, P.W__plus__, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_687 = Vertex(name = 'V_687',
               particles = [ P.W__minus__, P.W__plus__, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_688 = Vertex(name = 'V_688',
               particles = [ P.W__minus__, P.W__plus__, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_689 = Vertex(name = 'V_689',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_9})

V_690 = Vertex(name = 'V_690',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_39})

V_691 = Vertex(name = 'V_691',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_31})

V_692 = Vertex(name = 'V_692',
               particles = [ P.x1__plus__, P.b, P.stR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_240})

V_693 = Vertex(name = 'V_693',
               particles = [ P.x1__minus__, P.b__tilde__, P.stR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_240})

V_694 = Vertex(name = 'V_694',
               particles = [ P.x2__plus__, P.b, P.stR__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_241})

V_695 = Vertex(name = 'V_695',
               particles = [ P.x2__minus__, P.b__tilde__, P.stR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_241})

V_696 = Vertex(name = 'V_696',
               particles = [ P.a, P.Z, P.seL__plus__, P.seL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_143})

V_697 = Vertex(name = 'V_697',
               particles = [ P.a, P.Z, P.smuL__plus__, P.smuL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_143})

V_698 = Vertex(name = 'V_698',
               particles = [ P.a, P.Z, P.seR__plus__, P.seR__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_92})

V_699 = Vertex(name = 'V_699',
               particles = [ P.a, P.Z, P.smuR__plus__, P.smuR__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_92})

V_700 = Vertex(name = 'V_700',
               particles = [ P.Z, P.seL__plus__, P.seL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_140})

V_701 = Vertex(name = 'V_701',
               particles = [ P.Z, P.seR__plus__, P.seR__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_89})

V_702 = Vertex(name = 'V_702',
               particles = [ P.Z, P.smuL__plus__, P.smuL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_140})

V_703 = Vertex(name = 'V_703',
               particles = [ P.Z, P.smuR__plus__, P.smuR__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_89})

V_704 = Vertex(name = 'V_704',
               particles = [ P.Z, P.sne__tilde__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_83})

V_705 = Vertex(name = 'V_705',
               particles = [ P.Z, P.snm__tilde__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_83})

V_706 = Vertex(name = 'V_706',
               particles = [ P.Z, P.snt__tilde__, P.snt ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_83})

V_707 = Vertex(name = 'V_707',
               particles = [ P.a, P.Z, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_163})

V_708 = Vertex(name = 'V_708',
               particles = [ P.Z, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_162})

V_709 = Vertex(name = 'V_709',
               particles = [ P.a, P.Z, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_166})

V_710 = Vertex(name = 'V_710',
               particles = [ P.a, P.Z, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_166})

V_711 = Vertex(name = 'V_711',
               particles = [ P.Z, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_165})

V_712 = Vertex(name = 'V_712',
               particles = [ P.Z, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_164})

V_713 = Vertex(name = 'V_713',
               particles = [ P.a, P.Z, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_168})

V_714 = Vertex(name = 'V_714',
               particles = [ P.Z, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_167})

V_715 = Vertex(name = 'V_715',
               particles = [ P.Z, P.sbL__tilde__, P.sbL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_136})

V_716 = Vertex(name = 'V_716',
               particles = [ P.a, P.Z, P.sbL__tilde__, P.sbL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_141})

V_717 = Vertex(name = 'V_717',
               particles = [ P.Z, P.sbR__tilde__, P.sbR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_85})

V_718 = Vertex(name = 'V_718',
               particles = [ P.a, P.Z, P.sbR__tilde__, P.sbR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_90})

V_719 = Vertex(name = 'V_719',
               particles = [ P.Z, P.scL__tilde__, P.scL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_137})

V_720 = Vertex(name = 'V_720',
               particles = [ P.a, P.Z, P.scL__tilde__, P.scL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_142})

V_721 = Vertex(name = 'V_721',
               particles = [ P.Z, P.scR__tilde__, P.scR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_86})

V_722 = Vertex(name = 'V_722',
               particles = [ P.a, P.Z, P.scR__tilde__, P.scR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_723 = Vertex(name = 'V_723',
               particles = [ P.Z, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_136})

V_724 = Vertex(name = 'V_724',
               particles = [ P.a, P.Z, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_141})

V_725 = Vertex(name = 'V_725',
               particles = [ P.Z, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_85})

V_726 = Vertex(name = 'V_726',
               particles = [ P.a, P.Z, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_90})

V_727 = Vertex(name = 'V_727',
               particles = [ P.Z, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_136})

V_728 = Vertex(name = 'V_728',
               particles = [ P.a, P.Z, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_141})

V_729 = Vertex(name = 'V_729',
               particles = [ P.Z, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_85})

V_730 = Vertex(name = 'V_730',
               particles = [ P.a, P.Z, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_90})

V_731 = Vertex(name = 'V_731',
               particles = [ P.Z, P.stL__tilde__, P.stL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_137})

V_732 = Vertex(name = 'V_732',
               particles = [ P.a, P.Z, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_142})

V_733 = Vertex(name = 'V_733',
               particles = [ P.Z, P.stR__tilde__, P.stR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_86})

V_734 = Vertex(name = 'V_734',
               particles = [ P.a, P.Z, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_735 = Vertex(name = 'V_735',
               particles = [ P.Z, P.suL__tilde__, P.suL ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_137})

V_736 = Vertex(name = 'V_736',
               particles = [ P.a, P.Z, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_142})

V_737 = Vertex(name = 'V_737',
               particles = [ P.Z, P.suR__tilde__, P.suR ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_86})

V_738 = Vertex(name = 'V_738',
               particles = [ P.a, P.Z, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_739 = Vertex(name = 'V_739',
               particles = [ P.g, P.Z, P.sbL__tilde__, P.sbL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_144})

V_740 = Vertex(name = 'V_740',
               particles = [ P.g, P.Z, P.sbR__tilde__, P.sbR ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_93})

V_741 = Vertex(name = 'V_741',
               particles = [ P.g, P.Z, P.scL__tilde__, P.scL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_145})

V_742 = Vertex(name = 'V_742',
               particles = [ P.g, P.Z, P.scR__tilde__, P.scR ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_94})

V_743 = Vertex(name = 'V_743',
               particles = [ P.g, P.Z, P.sdL__tilde__, P.sdL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_144})

V_744 = Vertex(name = 'V_744',
               particles = [ P.g, P.Z, P.sdR__tilde__, P.sdR ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_93})

V_745 = Vertex(name = 'V_745',
               particles = [ P.g, P.Z, P.ssL__tilde__, P.ssL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_144})

V_746 = Vertex(name = 'V_746',
               particles = [ P.g, P.Z, P.ssR__tilde__, P.ssR ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_93})

V_747 = Vertex(name = 'V_747',
               particles = [ P.g, P.Z, P.stL__tilde__, P.stL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_145})

V_748 = Vertex(name = 'V_748',
               particles = [ P.g, P.Z, P.stR__tilde__, P.stR ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_94})

V_749 = Vertex(name = 'V_749',
               particles = [ P.g, P.Z, P.suL__tilde__, P.suL ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_145})

V_750 = Vertex(name = 'V_750',
               particles = [ P.g, P.Z, P.suR__tilde__, P.suR ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_94})

V_751 = Vertex(name = 'V_751',
               particles = [ P.W__minus__, P.Z, P.seL__plus__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_64})

V_752 = Vertex(name = 'V_752',
               particles = [ P.W__minus__, P.Z, P.smuL__plus__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_64})

V_753 = Vertex(name = 'V_753',
               particles = [ P.W__minus__, P.Z, P.snt, P.stau1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_77})

V_754 = Vertex(name = 'V_754',
               particles = [ P.W__minus__, P.Z, P.snt, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_78})

V_755 = Vertex(name = 'V_755',
               particles = [ P.W__minus__, P.Z, P.scL, P.ssL__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_756 = Vertex(name = 'V_756',
               particles = [ P.W__minus__, P.Z, P.sbL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_757 = Vertex(name = 'V_757',
               particles = [ P.W__minus__, P.Z, P.sdL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_758 = Vertex(name = 'V_758',
               particles = [ P.W__plus__, P.Z, P.seL__minus__, P.sne__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_64})

V_759 = Vertex(name = 'V_759',
               particles = [ P.W__plus__, P.Z, P.smuL__minus__, P.snm__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_64})

V_760 = Vertex(name = 'V_760',
               particles = [ P.W__plus__, P.Z, P.snt__tilde__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_77})

V_761 = Vertex(name = 'V_761',
               particles = [ P.W__plus__, P.Z, P.snt__tilde__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_78})

V_762 = Vertex(name = 'V_762',
               particles = [ P.W__plus__, P.Z, P.scL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_763 = Vertex(name = 'V_763',
               particles = [ P.W__plus__, P.Z, P.sbL, P.stL__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_764 = Vertex(name = 'V_764',
               particles = [ P.W__plus__, P.Z, P.sdL, P.suL__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_765 = Vertex(name = 'V_765',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
               couplings = {(0,0):C.GC_43,(0,1):C.GC_42,(0,2):C.GC_42})

V_766 = Vertex(name = 'V_766',
               particles = [ P.Z, P.Z, P.seL__plus__, P.seL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_767 = Vertex(name = 'V_767',
               particles = [ P.Z, P.Z, P.smuL__plus__, P.smuL__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_768 = Vertex(name = 'V_768',
               particles = [ P.Z, P.Z, P.sne__tilde__, P.sne ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_80})

V_769 = Vertex(name = 'V_769',
               particles = [ P.Z, P.Z, P.snm__tilde__, P.snm ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_80})

V_770 = Vertex(name = 'V_770',
               particles = [ P.Z, P.Z, P.snt__tilde__, P.snt ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_80})

V_771 = Vertex(name = 'V_771',
               particles = [ P.Z, P.Z, P.seR__plus__, P.seR__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_97})

V_772 = Vertex(name = 'V_772',
               particles = [ P.Z, P.Z, P.smuR__plus__, P.smuR__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_97})

V_773 = Vertex(name = 'V_773',
               particles = [ P.Z, P.Z, P.stau1__plus__, P.stau1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_174})

V_774 = Vertex(name = 'V_774',
               particles = [ P.Z, P.Z, P.stau1__minus__, P.stau2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_175})

V_775 = Vertex(name = 'V_775',
               particles = [ P.Z, P.Z, P.stau1__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_175})

V_776 = Vertex(name = 'V_776',
               particles = [ P.Z, P.Z, P.stau2__plus__, P.stau2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_176})

V_777 = Vertex(name = 'V_777',
               particles = [ P.Z, P.Z, P.sbL__tilde__, P.sbL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_169})

V_778 = Vertex(name = 'V_778',
               particles = [ P.Z, P.Z, P.sbR__tilde__, P.sbR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_779 = Vertex(name = 'V_779',
               particles = [ P.Z, P.Z, P.scL__tilde__, P.scL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_170})

V_780 = Vertex(name = 'V_780',
               particles = [ P.Z, P.Z, P.scR__tilde__, P.scR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_781 = Vertex(name = 'V_781',
               particles = [ P.Z, P.Z, P.sdL__tilde__, P.sdL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_169})

V_782 = Vertex(name = 'V_782',
               particles = [ P.Z, P.Z, P.sdR__tilde__, P.sdR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_783 = Vertex(name = 'V_783',
               particles = [ P.Z, P.Z, P.ssL__tilde__, P.ssL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_169})

V_784 = Vertex(name = 'V_784',
               particles = [ P.Z, P.Z, P.ssR__tilde__, P.ssR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_785 = Vertex(name = 'V_785',
               particles = [ P.Z, P.Z, P.stL__tilde__, P.stL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_170})

V_786 = Vertex(name = 'V_786',
               particles = [ P.Z, P.Z, P.stR__tilde__, P.stR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_787 = Vertex(name = 'V_787',
               particles = [ P.Z, P.Z, P.suL__tilde__, P.suL ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_170})

V_788 = Vertex(name = 'V_788',
               particles = [ P.Z, P.Z, P.suR__tilde__, P.suR ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_96})

V_789 = Vertex(name = 'V_789',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
               couplings = {(0,0):C.GC_27,(0,1):C.GC_27,(0,2):C.GC_28})

V_790 = Vertex(name = 'V_790',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_791 = Vertex(name = 'V_791',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_792 = Vertex(name = 'V_792',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_793 = Vertex(name = 'V_793',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_794 = Vertex(name = 'V_794',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_795 = Vertex(name = 'V_795',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_796 = Vertex(name = 'V_796',
               particles = [ P.tau__plus__, P.tau__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_797 = Vertex(name = 'V_797',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_798 = Vertex(name = 'V_798',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_799 = Vertex(name = 'V_799',
               particles = [ P.go, P.go, P.g ],
               color = [ 'f(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_14,(0,1):C.GC_14,(0,2):C.GC_14})

V_800 = Vertex(name = 'V_800',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_801 = Vertex(name = 'V_801',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_802 = Vertex(name = 'V_802',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_803 = Vertex(name = 'V_803',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_804 = Vertex(name = 'V_804',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_805 = Vertex(name = 'V_805',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_806 = Vertex(name = 'V_806',
               particles = [ P.x1__minus__, P.x1__plus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_198,(0,1):C.GC_182})

V_807 = Vertex(name = 'V_807',
               particles = [ P.x2__minus__, P.x1__plus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_205,(0,1):C.GC_189})

V_808 = Vertex(name = 'V_808',
               particles = [ P.x1__minus__, P.x2__plus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_205,(0,1):C.GC_189})

V_809 = Vertex(name = 'V_809',
               particles = [ P.x2__minus__, P.x2__plus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_207,(0,1):C.GC_191})

V_810 = Vertex(name = 'V_810',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_811 = Vertex(name = 'V_811',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_812 = Vertex(name = 'V_812',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_813 = Vertex(name = 'V_813',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_814 = Vertex(name = 'V_814',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_815 = Vertex(name = 'V_815',
               particles = [ P.tau__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_816 = Vertex(name = 'V_816',
               particles = [ P.n1, P.x1__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_194,(0,1):C.GC_178})

V_817 = Vertex(name = 'V_817',
               particles = [ P.n2, P.x1__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_195,(0,1):C.GC_179})

V_818 = Vertex(name = 'V_818',
               particles = [ P.n3, P.x1__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_196,(0,1):C.GC_180})

V_819 = Vertex(name = 'V_819',
               particles = [ P.n4, P.x1__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_197,(0,1):C.GC_181})

V_820 = Vertex(name = 'V_820',
               particles = [ P.n1, P.x2__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_201,(0,1):C.GC_185})

V_821 = Vertex(name = 'V_821',
               particles = [ P.n2, P.x2__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_202,(0,1):C.GC_186})

V_822 = Vertex(name = 'V_822',
               particles = [ P.n3, P.x2__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_203,(0,1):C.GC_187})

V_823 = Vertex(name = 'V_823',
               particles = [ P.n4, P.x2__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_204,(0,1):C.GC_188})

V_824 = Vertex(name = 'V_824',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_825 = Vertex(name = 'V_825',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_826 = Vertex(name = 'V_826',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_827 = Vertex(name = 'V_827',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_828 = Vertex(name = 'V_828',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_829 = Vertex(name = 'V_829',
               particles = [ P.vt__tilde__, P.tau__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_830 = Vertex(name = 'V_830',
               particles = [ P.x1__minus__, P.n1, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_194,(0,1):C.GC_178})

V_831 = Vertex(name = 'V_831',
               particles = [ P.x1__minus__, P.n2, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_195,(0,1):C.GC_179})

V_832 = Vertex(name = 'V_832',
               particles = [ P.x1__minus__, P.n3, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_196,(0,1):C.GC_180})

V_833 = Vertex(name = 'V_833',
               particles = [ P.x1__minus__, P.n4, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_197,(0,1):C.GC_181})

V_834 = Vertex(name = 'V_834',
               particles = [ P.x2__minus__, P.n1, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_201,(0,1):C.GC_185})

V_835 = Vertex(name = 'V_835',
               particles = [ P.x2__minus__, P.n2, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_202,(0,1):C.GC_186})

V_836 = Vertex(name = 'V_836',
               particles = [ P.x2__minus__, P.n3, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_203,(0,1):C.GC_187})

V_837 = Vertex(name = 'V_837',
               particles = [ P.x2__minus__, P.n4, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_204,(0,1):C.GC_188})

V_838 = Vertex(name = 'V_838',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_135,(0,1):C.GC_84})

V_839 = Vertex(name = 'V_839',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_87})

V_840 = Vertex(name = 'V_840',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_135,(0,1):C.GC_84})

V_841 = Vertex(name = 'V_841',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_139,(0,1):C.GC_88})

V_842 = Vertex(name = 'V_842',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_139,(0,1):C.GC_88})

V_843 = Vertex(name = 'V_843',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_135,(0,1):C.GC_84})

V_844 = Vertex(name = 'V_844',
               particles = [ P.tau__plus__, P.tau__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_139,(0,1):C.GC_88})

V_845 = Vertex(name = 'V_845',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_87})

V_846 = Vertex(name = 'V_846',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_87})

V_847 = Vertex(name = 'V_847',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_82})

V_848 = Vertex(name = 'V_848',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_82})

V_849 = Vertex(name = 'V_849',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_82})

V_850 = Vertex(name = 'V_850',
               particles = [ P.n1, P.n1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_125})

V_851 = Vertex(name = 'V_851',
               particles = [ P.n2, P.n1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_126})

V_852 = Vertex(name = 'V_852',
               particles = [ P.n2, P.n2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_127})

V_853 = Vertex(name = 'V_853',
               particles = [ P.n3, P.n1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_128})

V_854 = Vertex(name = 'V_854',
               particles = [ P.n3, P.n2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_129})

V_855 = Vertex(name = 'V_855',
               particles = [ P.n3, P.n3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_130})

V_856 = Vertex(name = 'V_856',
               particles = [ P.n4, P.n1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_131})

V_857 = Vertex(name = 'V_857',
               particles = [ P.n4, P.n2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_132})

V_858 = Vertex(name = 'V_858',
               particles = [ P.n4, P.n3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_133})

V_859 = Vertex(name = 'V_859',
               particles = [ P.n4, P.n4, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_134})

V_860 = Vertex(name = 'V_860',
               particles = [ P.x1__minus__, P.x1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_199,(0,1):C.GC_183})

V_861 = Vertex(name = 'V_861',
               particles = [ P.x2__minus__, P.x1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_206,(0,1):C.GC_190})

V_862 = Vertex(name = 'V_862',
               particles = [ P.x1__minus__, P.x2__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_206,(0,1):C.GC_190})

V_863 = Vertex(name = 'V_863',
               particles = [ P.x2__minus__, P.x2__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_208,(0,1):C.GC_192})

