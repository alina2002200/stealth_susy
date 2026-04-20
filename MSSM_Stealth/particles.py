# ---------------------------------------------------------------------- 
# This model file was automatically created by SARAH version4.15.4
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840   
# (c) Florian Staub, Mark Goodsell, Werner Porod and Martin Gabelmann 2023 
# ---------------------------------------------------------------------- 
# File created at 0:6 on 21.4.2026  
# ---------------------------------------------------------------------- 


from __future__ import division
from object_library import all_particles,Particle
import parameters as Param


go = Particle(pdg_code =1000021,
    name = 'go' ,
    antiname = 'go' ,
    spin = 2 ,
    color = 8 ,
    mass = Param.Mgo ,
    width = Param.Wgo ,
    line = 'scurly' ,
    charge = 0 ,
    texname = '\\tilde{g}' ,
    antitexname = '\\tilde{g}' )

nu1 = Particle(pdg_code =12,
    name = 'nu1' ,
    antiname = 'nu1bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = 0 ,
    texname = '{\\nu}_1' ,
    antitexname = '{\\bar{\\nu}}_1' )

nu1bar = nu1.anti()


nu2 = Particle(pdg_code =14,
    name = 'nu2' ,
    antiname = 'nu2bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = 0 ,
    texname = '{\\nu}_2' ,
    antitexname = '{\\bar{\\nu}}_2' )

nu2bar = nu2.anti()


nu3 = Particle(pdg_code =16,
    name = 'nu3' ,
    antiname = 'nu3bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = 0 ,
    texname = '{\\nu}_3' ,
    antitexname = '{\\bar{\\nu}}_3' )

nu3bar = nu3.anti()


N1 = Particle(pdg_code =1000022,
    name = 'N1' ,
    antiname = 'N1' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.MN1 ,
    width = Param.WN1 ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\tilde{\\chi}^0}_1' ,
    antitexname = '{\\tilde{\\chi}^0}_1' )

N2 = Particle(pdg_code =1000023,
    name = 'N2' ,
    antiname = 'N2' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.MN2 ,
    width = Param.WN2 ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\tilde{\\chi}^0}_2' ,
    antitexname = '{\\tilde{\\chi}^0}_2' )

N3 = Particle(pdg_code =1000025,
    name = 'N3' ,
    antiname = 'N3' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.MN3 ,
    width = Param.WN3 ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\tilde{\\chi}^0}_3' ,
    antitexname = '{\\tilde{\\chi}^0}_3' )

N4 = Particle(pdg_code =1000035,
    name = 'N4' ,
    antiname = 'N4' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.MN4 ,
    width = Param.WN4 ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\tilde{\\chi}^0}_4' ,
    antitexname = '{\\tilde{\\chi}^0}_4' )

C1 = Particle(pdg_code =-1000024,
    name = 'C1' ,
    antiname = 'C1bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.MC1 ,
    width = Param.WC1 ,
    line = 'swavy' ,
    charge = -1 ,
    texname = '{\\tilde{\\chi}^-}_1' ,
    antitexname = '{\\tilde{\\chi}^+}_1' )

C1bar = C1.anti()


C2 = Particle(pdg_code =-1000037,
    name = 'C2' ,
    antiname = 'C2bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.MC2 ,
    width = Param.WC2 ,
    line = 'swavy' ,
    charge = -1 ,
    texname = '{\\tilde{\\chi}^-}_2' ,
    antitexname = '{\\tilde{\\chi}^+}_2' )

C2bar = C2.anti()


e1 = Particle(pdg_code =11,
    name = 'e1' ,
    antiname = 'e1bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Me1 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = -1 ,
    texname = '{e}_1' ,
    antitexname = '{\\bar{e}}_1' )

e1bar = e1.anti()


e2 = Particle(pdg_code =13,
    name = 'e2' ,
    antiname = 'e2bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Me2 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = -1 ,
    texname = '{e}_2' ,
    antitexname = '{\\bar{e}}_2' )

e2bar = e2.anti()


e3 = Particle(pdg_code =15,
    name = 'e3' ,
    antiname = 'e3bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Me3 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = -1 ,
    texname = '{e}_3' ,
    antitexname = '{\\bar{e}}_3' )

e3bar = e3.anti()


d1 = Particle(pdg_code =1,
    name = 'd1' ,
    antiname = 'd1bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Md1 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = -1/3 ,
    texname = '{d}_1' ,
    antitexname = '{\\bar{d}}_1' )

d1bar = d1.anti()


d2 = Particle(pdg_code =3,
    name = 'd2' ,
    antiname = 'd2bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Md2 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = -1/3 ,
    texname = '{d}_2' ,
    antitexname = '{\\bar{d}}_2' )

d2bar = d2.anti()


d3 = Particle(pdg_code =5,
    name = 'd3' ,
    antiname = 'd3bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Md3 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = -1/3 ,
    texname = '{d}_3' ,
    antitexname = '{\\bar{d}}_3' )

d3bar = d3.anti()


u1 = Particle(pdg_code =2,
    name = 'u1' ,
    antiname = 'u1bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Mu1 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = 2/3 ,
    texname = '{u}_1' ,
    antitexname = '{\\bar{u}}_1' )

u1bar = u1.anti()


u2 = Particle(pdg_code =4,
    name = 'u2' ,
    antiname = 'u2bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Mu2 ,
    width = Param.ZERO ,
    line = 'straight' ,
    charge = 2/3 ,
    texname = '{u}_2' ,
    antitexname = '{\\bar{u}}_2' )

u2bar = u2.anti()


u3 = Particle(pdg_code =6,
    name = 'u3' ,
    antiname = 'u3bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Mu3 ,
    width = Param.Wu3 ,
    line = 'straight' ,
    charge = 2/3 ,
    texname = '{u}_3' ,
    antitexname = '{\\bar{u}}_3' )

u3bar = u3.anti()


SS = Particle(pdg_code =9000001,
    name = 'SS' ,
    antiname = 'SSc' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'dashed' ,
    charge = 0 ,
    texname = 'SS' ,
    antitexname = 'conj[SS]^*' )

SSc = SS.anti()


SY3 = Particle(pdg_code =9000002,
    name = 'SY3' ,
    antiname = 'SY3c' ,
    spin = 1 ,
    color = -3 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'dashed' ,
    charge = -1/3 ,
    texname = 'SY3' ,
    antitexname = 'conj[SY3]^*' )

SY3c = SY3.anti()


SY2 = Particle(pdg_code =9000003,
    name = 'SY2' ,
    antiname = 'SY2c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MSY2 ,
    width = Param.WSY2 ,
    line = 'dashed' ,
    charge = 1/2 ,
    texname = 'SY2' ,
    antitexname = 'conj[SY2]^*' )

SY2c = SY2.anti()


SYbar3 = Particle(pdg_code =9000004,
    name = 'SYbar3' ,
    antiname = 'SYbar3c' ,
    spin = 1 ,
    color = -3 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'dashed' ,
    charge = 1/3 ,
    texname = 'SYbar3' ,
    antitexname = 'conj[SYbar3]^*' )

SYbar3c = SYbar3.anti()


SYbar2 = Particle(pdg_code =9000005,
    name = 'SYbar2' ,
    antiname = 'SYbar2c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MSYbar2 ,
    width = Param.WSYbar2 ,
    line = 'dashed' ,
    charge = -1/2 ,
    texname = 'SYbar2' ,
    antitexname = 'conj[SYbar2]^*' )

SYbar2c = SYbar2.anti()


sd1 = Particle(pdg_code =1000001,
    name = 'sd1' ,
    antiname = 'sd1c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msd1 ,
    width = Param.Wsd1 ,
    line = 'dashed' ,
    charge = -1/3 ,
    texname = '{\\tilde{d}}_1' ,
    antitexname = '{{\\tilde{d}}^*}_1' )

sd1c = sd1.anti()


sd2 = Particle(pdg_code =1000003,
    name = 'sd2' ,
    antiname = 'sd2c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msd2 ,
    width = Param.Wsd2 ,
    line = 'dashed' ,
    charge = -1/3 ,
    texname = '{\\tilde{d}}_2' ,
    antitexname = '{{\\tilde{d}}^*}_2' )

sd2c = sd2.anti()


sd3 = Particle(pdg_code =1000005,
    name = 'sd3' ,
    antiname = 'sd3c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msd3 ,
    width = Param.Wsd3 ,
    line = 'dashed' ,
    charge = -1/3 ,
    texname = '{\\tilde{d}}_3' ,
    antitexname = '{{\\tilde{d}}^*}_3' )

sd3c = sd3.anti()


sd4 = Particle(pdg_code =2000001,
    name = 'sd4' ,
    antiname = 'sd4c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msd4 ,
    width = Param.Wsd4 ,
    line = 'dashed' ,
    charge = -1/3 ,
    texname = '{\\tilde{d}}_4' ,
    antitexname = '{{\\tilde{d}}^*}_4' )

sd4c = sd4.anti()


sd5 = Particle(pdg_code =2000003,
    name = 'sd5' ,
    antiname = 'sd5c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msd5 ,
    width = Param.Wsd5 ,
    line = 'dashed' ,
    charge = -1/3 ,
    texname = '{\\tilde{d}}_5' ,
    antitexname = '{{\\tilde{d}}^*}_5' )

sd5c = sd5.anti()


sd6 = Particle(pdg_code =2000005,
    name = 'sd6' ,
    antiname = 'sd6c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msd6 ,
    width = Param.Wsd6 ,
    line = 'dashed' ,
    charge = -1/3 ,
    texname = '{\\tilde{d}}_6' ,
    antitexname = '{{\\tilde{d}}^*}_6' )

sd6c = sd6.anti()


sv1 = Particle(pdg_code =1000012,
    name = 'sv1' ,
    antiname = 'sv1c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Msv1 ,
    width = Param.Wsv1 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{\\tilde{\\nu}}_1' ,
    antitexname = '{{\\tilde{\\nu}}^*}_1' )

sv1c = sv1.anti()


sv2 = Particle(pdg_code =1000014,
    name = 'sv2' ,
    antiname = 'sv2c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Msv2 ,
    width = Param.Wsv2 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{\\tilde{\\nu}}_2' ,
    antitexname = '{{\\tilde{\\nu}}^*}_2' )

sv2c = sv2.anti()


sv3 = Particle(pdg_code =1000016,
    name = 'sv3' ,
    antiname = 'sv3c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Msv3 ,
    width = Param.Wsv3 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{\\tilde{\\nu}}_3' ,
    antitexname = '{{\\tilde{\\nu}}^*}_3' )

sv3c = sv3.anti()


su1 = Particle(pdg_code =1000002,
    name = 'su1' ,
    antiname = 'su1c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msu1 ,
    width = Param.Wsu1 ,
    line = 'dashed' ,
    charge = 2/3 ,
    texname = '{\\tilde{u}}_1' ,
    antitexname = '{{\\tilde{u}}^*}_1' )

su1c = su1.anti()


su2 = Particle(pdg_code =1000004,
    name = 'su2' ,
    antiname = 'su2c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msu2 ,
    width = Param.Wsu2 ,
    line = 'dashed' ,
    charge = 2/3 ,
    texname = '{\\tilde{u}}_2' ,
    antitexname = '{{\\tilde{u}}^*}_2' )

su2c = su2.anti()


su3 = Particle(pdg_code =1000006,
    name = 'su3' ,
    antiname = 'su3c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msu3 ,
    width = Param.Wsu3 ,
    line = 'dashed' ,
    charge = 2/3 ,
    texname = '{\\tilde{u}}_3' ,
    antitexname = '{{\\tilde{u}}^*}_3' )

su3c = su3.anti()


su4 = Particle(pdg_code =2000002,
    name = 'su4' ,
    antiname = 'su4c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msu4 ,
    width = Param.Wsu4 ,
    line = 'dashed' ,
    charge = 2/3 ,
    texname = '{\\tilde{u}}_4' ,
    antitexname = '{{\\tilde{u}}^*}_4' )

su4c = su4.anti()


su5 = Particle(pdg_code =2000004,
    name = 'su5' ,
    antiname = 'su5c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msu5 ,
    width = Param.Wsu5 ,
    line = 'dashed' ,
    charge = 2/3 ,
    texname = '{\\tilde{u}}_5' ,
    antitexname = '{{\\tilde{u}}^*}_5' )

su5c = su5.anti()


su6 = Particle(pdg_code =2000006,
    name = 'su6' ,
    antiname = 'su6c' ,
    spin = 1 ,
    color = 3 ,
    mass = Param.Msu6 ,
    width = Param.Wsu6 ,
    line = 'dashed' ,
    charge = 2/3 ,
    texname = '{\\tilde{u}}_6' ,
    antitexname = '{{\\tilde{u}}^*}_6' )

su6c = su6.anti()


se1 = Particle(pdg_code =1000011,
    name = 'se1' ,
    antiname = 'se1c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mse1 ,
    width = Param.Wse1 ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{\\tilde{e}}_1' ,
    antitexname = '{{\\tilde{e}}^*}_1' )

se1c = se1.anti()


se2 = Particle(pdg_code =1000013,
    name = 'se2' ,
    antiname = 'se2c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mse2 ,
    width = Param.Wse2 ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{\\tilde{e}}_2' ,
    antitexname = '{{\\tilde{e}}^*}_2' )

se2c = se2.anti()


se3 = Particle(pdg_code =1000015,
    name = 'se3' ,
    antiname = 'se3c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mse3 ,
    width = Param.Wse3 ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{\\tilde{e}}_3' ,
    antitexname = '{{\\tilde{e}}^*}_3' )

se3c = se3.anti()


se4 = Particle(pdg_code =2000011,
    name = 'se4' ,
    antiname = 'se4c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mse4 ,
    width = Param.Wse4 ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{\\tilde{e}}_4' ,
    antitexname = '{{\\tilde{e}}^*}_4' )

se4c = se4.anti()


se5 = Particle(pdg_code =2000013,
    name = 'se5' ,
    antiname = 'se5c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mse5 ,
    width = Param.Wse5 ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{\\tilde{e}}_5' ,
    antitexname = '{{\\tilde{e}}^*}_5' )

se5c = se5.anti()


se6 = Particle(pdg_code =2000015,
    name = 'se6' ,
    antiname = 'se6c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mse6 ,
    width = Param.Wse6 ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{\\tilde{e}}_6' ,
    antitexname = '{{\\tilde{e}}^*}_6' )

se6c = se6.anti()


h1 = Particle(pdg_code =25,
    name = 'h1' ,
    antiname = 'h1' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mh1 ,
    width = Param.Wh1 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{h}_1' ,
    antitexname = '{h}_1' )

h2 = Particle(pdg_code =35,
    name = 'h2' ,
    antiname = 'h2' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mh2 ,
    width = Param.Wh2 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{h}_2' ,
    antitexname = '{h}_2' )

Ah1 = Particle(pdg_code =999900,
    name = 'Ah1' ,
    antiname = 'Ah1' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MAh1 ,
    width = Param.ZERO,
    goldstone = True ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{A^0}_1' ,
    antitexname = '{A^0}_1' )

Ah2 = Particle(pdg_code =36,
    name = 'Ah2' ,
    antiname = 'Ah2' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MAh2 ,
    width = Param.WAh2 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{A^0}_2' ,
    antitexname = '{A^0}_2' )

Hm1 = Particle(pdg_code =999901,
    name = 'Hm1' ,
    antiname = 'Hm1c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MHm1 ,
    width = Param.ZERO,
    goldstone = True ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{H^-}_1' ,
    antitexname = '{H^+}_1' )

Hm1c = Hm1.anti()


Hm2 = Particle(pdg_code =-37,
    name = 'Hm2' ,
    antiname = 'Hm2c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MHm2 ,
    width = Param.WHm2 ,
    line = 'dashed' ,
    charge = -1 ,
    texname = '{H^-}_2' ,
    antitexname = '{H^+}_2' )

Hm2c = Hm2.anti()


g = Particle(pdg_code =21,
    name = 'g' ,
    antiname = 'g' ,
    spin = 3 ,
    color = 8 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'wavy' ,
    charge = 0 ,
    texname = 'g' ,
    antitexname = 'g' )

A = Particle(pdg_code =22,
    name = 'A' ,
    antiname = 'A' ,
    spin = 3 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'wavy' ,
    charge = 0 ,
    texname = '\\gamma' ,
    antitexname = '\\gamma' )

Z = Particle(pdg_code =23,
    name = 'Z' ,
    antiname = 'Z' ,
    spin = 3 ,
    color = 1 ,
    mass = Param.MZ ,
    width = Param.WZ ,
    line = 'wavy' ,
    charge = 0 ,
    texname = 'Z' ,
    antitexname = 'Z' )

Wm = Particle(pdg_code =-24,
    name = 'Wm' ,
    antiname = 'Wmc' ,
    spin = 3 ,
    color = 1 ,
    mass = Param.MWm ,
    width = Param.WWm ,
    line = 'wavy' ,
    charge = -1 ,
    texname = 'W^-' ,
    antitexname = 'W^+' )

Wmc = Wm.anti()


gG = Particle(pdg_code =999902,
    name = 'gG' ,
    antiname = 'gGc' ,
    spin = -1 ,
    color = 8 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    propagating = False,
    line = 'dotted' ,
    charge = 0 ,
    texname = '\\eta^G' ,
    antitexname = '\\bar{\\eta^G}' )

gGc = gG.anti()


gA = Particle(pdg_code =999903,
    name = 'gA' ,
    antiname = 'gAc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    propagating = False,
    line = 'dotted' ,
    charge = 0 ,
    texname = '\\eta^{\\gamma}' ,
    antitexname = '\\bar{\\eta^{\\gamma}}' )

gAc = gA.anti()


gZ = Particle(pdg_code =999904,
    name = 'gZ' ,
    antiname = 'gZc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.MgZ ,
    width = Param.WZ ,
    propagating = False,
    line = 'dotted' ,
    charge = 0 ,
    texname = '\\eta^Z' ,
    antitexname = '\\bar{\\eta^Z}' )

gZc = gZ.anti()


gWm = Particle(pdg_code =999905,
    name = 'gWm' ,
    antiname = 'gWmc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.MgWm ,
    width = Param.WWm ,
    propagating = False,
    line = 'dotted' ,
    charge = -1 ,
    texname = '\\eta^-' ,
    antitexname = '\\bar{\\eta^-}' )

gWmc = gWm.anti()


gWpC = Particle(pdg_code =999906,
    name = 'gWpC' ,
    antiname = 'gWpCc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.MgWpC ,
    width = Param.WWm ,
    propagating = False,
    line = 'dotted' ,
    charge = 1 ,
    texname = '\\eta^+' ,
    antitexname = '\\bar{\\eta^+}' )

gWpCc = gWpC.anti()


