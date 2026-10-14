# This file was automatically created by FeynRules 2.4.43
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Wed 30 Nov 2016 08:56:01



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 10,
               texname = '\\text{tb}',
               lhablock = 'HMIX',
               lhacode = [ 2 ])

MstLR = Parameter(name = 'MstLR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{MstLR}',
                  lhablock = 'MSoft',
                  lhacode = [ 1 ])

NN1x1 = Parameter(name = 'NN1x1',
                  nature = 'external',
                  type = 'complex',
                  value = 0.999,
                  texname = '\\text{NN1x1}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 1 ])

NN1x2 = Parameter(name = 'NN1x2',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN1x2}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 2 ])

NN1x3 = Parameter(name = 'NN1x3',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN1x3}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 3 ])

NN1x4 = Parameter(name = 'NN1x4',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN1x4}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 4 ])

NN2x1 = Parameter(name = 'NN2x1',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN2x1}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 1 ])

NN2x2 = Parameter(name = 'NN2x2',
                  nature = 'external',
                  type = 'complex',
                  value = 1,
                  texname = '\\text{NN2x2}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 2 ])

NN2x3 = Parameter(name = 'NN2x3',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN2x3}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 3 ])

NN2x4 = Parameter(name = 'NN2x4',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN2x4}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 4 ])

NN3x1 = Parameter(name = 'NN3x1',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN3x1}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 1 ])

NN3x2 = Parameter(name = 'NN3x2',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN3x2}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 2 ])

NN3x3 = Parameter(name = 'NN3x3',
                  nature = 'external',
                  type = 'complex',
                  value = 0.707107,
                  texname = '\\text{NN3x3}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 3 ])

NN3x4 = Parameter(name = 'NN3x4',
                  nature = 'external',
                  type = 'complex',
                  value = 0.707107,
                  texname = '\\text{NN3x4}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 4 ])

NN4x1 = Parameter(name = 'NN4x1',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN4x1}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 1 ])

NN4x2 = Parameter(name = 'NN4x2',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{NN4x2}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 2 ])

NN4x3 = Parameter(name = 'NN4x3',
                  nature = 'external',
                  type = 'complex',
                  value = -0.707107,
                  texname = '\\text{NN4x3}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 3 ])

NN4x4 = Parameter(name = 'NN4x4',
                  nature = 'external',
                  type = 'complex',
                  value = 0.707107,
                  texname = '\\text{NN4x4}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 4 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

Rtau1x1 = Parameter(name = 'Rtau1x1',
                    nature = 'external',
                    type = 'complex',
                    value = 0.707107,
                    texname = '\\text{Rtau1x1}',
                    lhablock = 'STAUMIX',
                    lhacode = [ 1, 1 ])

Rtau1x2 = Parameter(name = 'Rtau1x2',
                    nature = 'external',
                    type = 'complex',
                    value = 0.707107,
                    texname = '\\text{Rtau1x2}',
                    lhablock = 'STAUMIX',
                    lhacode = [ 1, 2 ])

Rtau2x1 = Parameter(name = 'Rtau2x1',
                    nature = 'external',
                    type = 'complex',
                    value = -0.707107,
                    texname = '\\text{Rtau2x1}',
                    lhablock = 'STAUMIX',
                    lhacode = [ 2, 1 ])

Rtau2x2 = Parameter(name = 'Rtau2x2',
                    nature = 'external',
                    type = 'complex',
                    value = 0.707107,
                    texname = '\\text{Rtau2x2}',
                    lhablock = 'STAUMIX',
                    lhacode = [ 2, 2 ])

UU1x1 = Parameter(name = 'UU1x1',
                  nature = 'external',
                  type = 'complex',
                  value = 1,
                  texname = '\\text{UU1x1}',
                  lhablock = 'UMIX',
                  lhacode = [ 1, 1 ])

UU1x2 = Parameter(name = 'UU1x2',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{UU1x2}',
                  lhablock = 'UMIX',
                  lhacode = [ 1, 2 ])

UU2x1 = Parameter(name = 'UU2x1',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{UU2x1}',
                  lhablock = 'UMIX',
                  lhacode = [ 2, 1 ])

UU2x2 = Parameter(name = 'UU2x2',
                  nature = 'external',
                  type = 'complex',
                  value = 1,
                  texname = '\\text{UU2x2}',
                  lhablock = 'UMIX',
                  lhacode = [ 2, 2 ])

VV1x1 = Parameter(name = 'VV1x1',
                  nature = 'external',
                  type = 'complex',
                  value = 1,
                  texname = '\\text{VV1x1}',
                  lhablock = 'VMIX',
                  lhacode = [ 1, 1 ])

VV1x2 = Parameter(name = 'VV1x2',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{VV1x2}',
                  lhablock = 'VMIX',
                  lhacode = [ 1, 2 ])

VV2x1 = Parameter(name = 'VV2x1',
                  nature = 'external',
                  type = 'complex',
                  value = 0,
                  texname = '\\text{VV2x1}',
                  lhablock = 'VMIX',
                  lhacode = [ 2, 1 ])

VV2x2 = Parameter(name = 'VV2x2',
                  nature = 'external',
                  type = 'complex',
                  value = 1,
                  texname = '\\text{VV2x2}',
                  lhablock = 'VMIX',
                  lhacode = [ 2, 2 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Mneu1 = Parameter(name = 'Mneu1',
                  nature = 'external',
                  type = 'real',
                  value = 50,
                  texname = '\\text{Mneu1}',
                  lhablock = 'MASS',
                  lhacode = [ 1000022 ])

Mneu2 = Parameter(name = 'Mneu2',
                  nature = 'external',
                  type = 'real',
                  value = 100,
                  texname = '\\text{Mneu2}',
                  lhablock = 'MASS',
                  lhacode = [ 1000023 ])

Mneu3 = Parameter(name = 'Mneu3',
                  nature = 'external',
                  type = 'real',
                  value = 100,
                  texname = '\\text{Mneu3}',
                  lhablock = 'MASS',
                  lhacode = [ 1000025 ])

Mneu4 = Parameter(name = 'Mneu4',
                  nature = 'external',
                  type = 'real',
                  value = 100,
                  texname = '\\text{Mneu4}',
                  lhablock = 'MASS',
                  lhacode = [ 1000035 ])

Mch1 = Parameter(name = 'Mch1',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{Mch1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000024 ])

Mch2 = Parameter(name = 'Mch2',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{Mch2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000037 ])

Mgo = Parameter(name = 'Mgo',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{Mgo}',
                lhablock = 'MASS',
                lhacode = [ 1000021 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

Msne = Parameter(name = 'Msne',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{Msne}',
                 lhablock = 'MASS',
                 lhacode = [ 1000012 ])

Msnm = Parameter(name = 'Msnm',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{Msnm}',
                 lhablock = 'MASS',
                 lhacode = [ 1000014 ])

Msnt = Parameter(name = 'Msnt',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{Msnt}',
                 lhablock = 'MASS',
                 lhacode = [ 1000016 ])

MseL = Parameter(name = 'MseL',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MseL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000011 ])

MsmuL = Parameter(name = 'MsmuL',
                  nature = 'external',
                  type = 'real',
                  value = 100,
                  texname = '\\text{MsmuL}',
                  lhablock = 'MASS',
                  lhacode = [ 1000013 ])

Mstau1 = Parameter(name = 'Mstau1',
                   nature = 'external',
                   type = 'real',
                   value = 100,
                   texname = '\\text{Mstau1}',
                   lhablock = 'MASS',
                   lhacode = [ 1000015 ])

MseR = Parameter(name = 'MseR',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MseR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000011 ])

MsmuR = Parameter(name = 'MsmuR',
                  nature = 'external',
                  type = 'real',
                  value = 100,
                  texname = '\\text{MsmuR}',
                  lhablock = 'MASS',
                  lhacode = [ 2000013 ])

Mstau2 = Parameter(name = 'Mstau2',
                   nature = 'external',
                   type = 'real',
                   value = 100,
                   texname = '\\text{Mstau2}',
                   lhablock = 'MASS',
                   lhacode = [ 2000015 ])

MsuL = Parameter(name = 'MsuL',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{MsuL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

MscL = Parameter(name = 'MscL',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{MscL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

MstL = Parameter(name = 'MstL',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{MstL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

MsuR = Parameter(name = 'MsuR',
                 nature = 'external',
                 type = 'real',
                 value = 1001,
                 texname = '\\text{MsuR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

MscR = Parameter(name = 'MscR',
                 nature = 'external',
                 type = 'real',
                 value = 1001,
                 texname = '\\text{MscR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

MstR = Parameter(name = 'MstR',
                 nature = 'external',
                 type = 'real',
                 value = 1001,
                 texname = '\\text{MstR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

MsdL = Parameter(name = 'MsdL',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{MsdL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

MssL = Parameter(name = 'MssL',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{MssL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

MsbL = Parameter(name = 'MsbL',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{MsbL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

MsdR = Parameter(name = 'MsdR',
                 nature = 'external',
                 type = 'real',
                 value = 1001,
                 texname = '\\text{MsdR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

MssR = Parameter(name = 'MssR',
                 nature = 'external',
                 type = 'real',
                 value = 1001,
                 texname = '\\text{MssR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

MsbR = Parameter(name = 'MsbR',
                 nature = 'external',
                 type = 'real',
                 value = 1001,
                 texname = '\\text{MsbR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

Wneu1 = Parameter(name = 'Wneu1',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{Wneu1}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000022 ])

Wneu2 = Parameter(name = 'Wneu2',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{Wneu2}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000023 ])

Wneu3 = Parameter(name = 'Wneu3',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{Wneu3}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000025 ])

Wneu4 = Parameter(name = 'Wneu4',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{Wneu4}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000035 ])

Wch1 = Parameter(name = 'Wch1',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{Wch1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000024 ])

Wch2 = Parameter(name = 'Wch2',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{Wch2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000037 ])

Wgo = Parameter(name = 'Wgo',
                nature = 'external',
                type = 'real',
                value = 10,
                texname = '\\text{Wgo}',
                lhablock = 'DECAY',
                lhacode = [ 1000021 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wsne = Parameter(name = 'Wsne',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{Wsne}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000012 ])

Wsnm = Parameter(name = 'Wsnm',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{Wsnm}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000014 ])

Wsnt = Parameter(name = 'Wsnt',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{Wsnt}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000016 ])

WseL = Parameter(name = 'WseL',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WseL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000011 ])

WsmuL = Parameter(name = 'WsmuL',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{WsmuL}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000013 ])

Wstau1 = Parameter(name = 'Wstau1',
                   nature = 'external',
                   type = 'real',
                   value = 5,
                   texname = '\\text{Wstau1}',
                   lhablock = 'DECAY',
                   lhacode = [ 1000015 ])

WseR = Parameter(name = 'WseR',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WseR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000011 ])

WsmuR = Parameter(name = 'WsmuR',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{WsmuR}',
                  lhablock = 'DECAY',
                  lhacode = [ 2000013 ])

Wstau2 = Parameter(name = 'Wstau2',
                   nature = 'external',
                   type = 'real',
                   value = 5,
                   texname = '\\text{Wstau2}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000015 ])

WsuL = Parameter(name = 'WsuL',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WsuL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

WscL = Parameter(name = 'WscL',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WscL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

WstL = Parameter(name = 'WstL',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WstL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

WsuR = Parameter(name = 'WsuR',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WsuR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

WscR = Parameter(name = 'WscR',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WscR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

WstR = Parameter(name = 'WstR',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WstR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

WsdL = Parameter(name = 'WsdL',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WsdL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

WssL = Parameter(name = 'WssL',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WssL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

WsbL = Parameter(name = 'WsbL',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WsbL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

WsdR = Parameter(name = 'WsdR',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WsdR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

WssR = Parameter(name = 'WssR',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WssR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

WsbR = Parameter(name = 'WsbR',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{WsbR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta')

MUH = Parameter(name = 'MUH',
                nature = 'internal',
                type = 'real',
                value = '200',
                texname = '\\text{MUH}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (cmath.pi*MZ**2)/(aEWM1*Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'MW/MZ',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cw**2)',
               texname = 's_w')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g\'')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*cw*MZ*sw)/ee',
                texname = 'v')

vd = Parameter(name = 'vd',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.cos(beta)',
               texname = 'v_d')

vu = Parameter(name = 'vu',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.sin(beta)',
               texname = 'v_u')

ye3x3 = Parameter(name = 'ye3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(MTA*cmath.sqrt(2))/vd',
                  texname = '\\text{ye3x3}')

yu3x3 = Parameter(name = 'yu3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(MT*cmath.sqrt(2))/vd',
                  texname = '\\text{yu3x3}')

