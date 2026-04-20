# ----------------------------------------------------------------------
# This model file was automatically created by SARAH version4.15.4
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840
# (c) Florian Staub, Mark Goodsell, Werner Porod and Martin Gabelmann 2023
# ----------------------------------------------------------------------
# File created at 0:6 on 21.4.2026
# ----------------------------------------------------------------------

from object_library import all_parameters,Parameter

from function_library import complexconjugate,re,im,csc,sec,acsc,asec
ZERO = Parameter(name='ZERO',
    nature='internal',
    type='real',
    value='0.0',
    texname='0')

Mgo = Parameter(name = 'Mgo',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{\\tilde{g}}',
    lhablock = 'MASS',
    lhacode = [1000021])

Wgo = Parameter(name = 'Wgo',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{\\tilde{g}}',
    lhablock = 'DECAY',
    lhacode = [1000021])

MN1 = Parameter(name = 'MN1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\chi}^0}_1}',
    lhablock = 'MASS',
    lhacode = [1000022])

WN1 = Parameter(name = 'WN1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\chi}^0}_1}',
    lhablock = 'DECAY',
    lhacode = [1000022])

MN2 = Parameter(name = 'MN2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\chi}^0}_2}',
    lhablock = 'MASS',
    lhacode = [1000023])

WN2 = Parameter(name = 'WN2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\chi}^0}_2}',
    lhablock = 'DECAY',
    lhacode = [1000023])

MN3 = Parameter(name = 'MN3',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\chi}^0}_3}',
    lhablock = 'MASS',
    lhacode = [1000025])

WN3 = Parameter(name = 'WN3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\chi}^0}_3}',
    lhablock = 'DECAY',
    lhacode = [1000025])

MN4 = Parameter(name = 'MN4',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\chi}^0}_4}',
    lhablock = 'MASS',
    lhacode = [1000035])

WN4 = Parameter(name = 'WN4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\chi}^0}_4}',
    lhablock = 'DECAY',
    lhacode = [1000035])

MC1 = Parameter(name = 'MC1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\chi}^-}_1}',
    lhablock = 'MASS',
    lhacode = [1000024])

WC1 = Parameter(name = 'WC1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\chi}^-}_1}',
    lhablock = 'DECAY',
    lhacode = [1000024])

MC2 = Parameter(name = 'MC2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\chi}^-}_2}',
    lhablock = 'MASS',
    lhacode = [1000037])

WC2 = Parameter(name = 'WC2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\chi}^-}_2}',
    lhablock = 'DECAY',
    lhacode = [1000037])

Me1 = Parameter(name = 'Me1',
    nature = 'external',
    type = 'real',
    value = 0.000511,
    texname = 'M_{{e}_1}',
    lhablock = 'MASS',
    lhacode = [11])

Me2 = Parameter(name = 'Me2',
    nature = 'external',
    type = 'real',
    value = 0.105,
    texname = 'M_{{e}_2}',
    lhablock = 'MASS',
    lhacode = [13])

Me3 = Parameter(name = 'Me3',
    nature = 'external',
    type = 'real',
    value = 1.776,
    texname = 'M_{{e}_3}',
    lhablock = 'MASS',
    lhacode = [15])

Md1 = Parameter(name = 'Md1',
    nature = 'external',
    type = 'real',
    value = 0.0035,
    texname = 'M_{{d}_1}',
    lhablock = 'MASS',
    lhacode = [1])

Md2 = Parameter(name = 'Md2',
    nature = 'external',
    type = 'real',
    value = 0.104,
    texname = 'M_{{d}_2}',
    lhablock = 'MASS',
    lhacode = [3])

Md3 = Parameter(name = 'Md3',
    nature = 'external',
    type = 'real',
    value = 4.2,
    texname = 'M_{{d}_3}',
    lhablock = 'MASS',
    lhacode = [5])

Mu1 = Parameter(name = 'Mu1',
    nature = 'external',
    type = 'real',
    value = 0.0015,
    texname = 'M_{{u}_1}',
    lhablock = 'MASS',
    lhacode = [2])

Mu2 = Parameter(name = 'Mu2',
    nature = 'external',
    type = 'real',
    value = 1.27,
    texname = 'M_{{u}_2}',
    lhablock = 'MASS',
    lhacode = [4])

Mu3 = Parameter(name = 'Mu3',
    nature = 'external',
    type = 'real',
    value = 171.2,
    texname = 'M_{{u}_3}',
    lhablock = 'MASS',
    lhacode = [6])

Wu3 = Parameter(name = 'Wu3',
    nature = 'external',
    type = 'real',
    value = 1.51,
    texname = '\\Gamma_{{u}_3}',
    lhablock = 'DECAY',
    lhacode = [6])

MSY2 = Parameter(name = 'MSY2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{SY2}',
    lhablock = 'MASS',
    lhacode = [9000003])

WSY2 = Parameter(name = 'WSY2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{SY2}',
    lhablock = 'DECAY',
    lhacode = [9000003])

MSYbar2 = Parameter(name = 'MSYbar2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{SYbar2}',
    lhablock = 'MASS',
    lhacode = [9000005])

WSYbar2 = Parameter(name = 'WSYbar2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{SYbar2}',
    lhablock = 'DECAY',
    lhacode = [9000005])

Msd1 = Parameter(name = 'Msd1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{d}}_1}',
    lhablock = 'MASS',
    lhacode = [1000001])

Wsd1 = Parameter(name = 'Wsd1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{d}}_1}',
    lhablock = 'DECAY',
    lhacode = [1000001])

Msd2 = Parameter(name = 'Msd2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{d}}_2}',
    lhablock = 'MASS',
    lhacode = [1000003])

Wsd2 = Parameter(name = 'Wsd2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{d}}_2}',
    lhablock = 'DECAY',
    lhacode = [1000003])

Msd3 = Parameter(name = 'Msd3',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{d}}_3}',
    lhablock = 'MASS',
    lhacode = [1000005])

Wsd3 = Parameter(name = 'Wsd3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{d}}_3}',
    lhablock = 'DECAY',
    lhacode = [1000005])

Msd4 = Parameter(name = 'Msd4',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{d}}_4}',
    lhablock = 'MASS',
    lhacode = [2000001])

Wsd4 = Parameter(name = 'Wsd4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{d}}_4}',
    lhablock = 'DECAY',
    lhacode = [2000001])

Msd5 = Parameter(name = 'Msd5',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{d}}_5}',
    lhablock = 'MASS',
    lhacode = [2000003])

Wsd5 = Parameter(name = 'Wsd5',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{d}}_5}',
    lhablock = 'DECAY',
    lhacode = [2000003])

Msd6 = Parameter(name = 'Msd6',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{d}}_6}',
    lhablock = 'MASS',
    lhacode = [2000005])

Wsd6 = Parameter(name = 'Wsd6',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{d}}_6}',
    lhablock = 'DECAY',
    lhacode = [2000005])

Msv1 = Parameter(name = 'Msv1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\nu}}_1}',
    lhablock = 'MASS',
    lhacode = [1000012])

Wsv1 = Parameter(name = 'Wsv1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\nu}}_1}',
    lhablock = 'DECAY',
    lhacode = [1000012])

Msv2 = Parameter(name = 'Msv2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\nu}}_2}',
    lhablock = 'MASS',
    lhacode = [1000014])

Wsv2 = Parameter(name = 'Wsv2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\nu}}_2}',
    lhablock = 'DECAY',
    lhacode = [1000014])

Msv3 = Parameter(name = 'Msv3',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{\\nu}}_3}',
    lhablock = 'MASS',
    lhacode = [1000016])

Wsv3 = Parameter(name = 'Wsv3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{\\nu}}_3}',
    lhablock = 'DECAY',
    lhacode = [1000016])

Msu1 = Parameter(name = 'Msu1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{u}}_1}',
    lhablock = 'MASS',
    lhacode = [1000002])

Wsu1 = Parameter(name = 'Wsu1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{u}}_1}',
    lhablock = 'DECAY',
    lhacode = [1000002])

Msu2 = Parameter(name = 'Msu2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{u}}_2}',
    lhablock = 'MASS',
    lhacode = [1000004])

Wsu2 = Parameter(name = 'Wsu2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{u}}_2}',
    lhablock = 'DECAY',
    lhacode = [1000004])

Msu3 = Parameter(name = 'Msu3',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{u}}_3}',
    lhablock = 'MASS',
    lhacode = [1000006])

Wsu3 = Parameter(name = 'Wsu3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{u}}_3}',
    lhablock = 'DECAY',
    lhacode = [1000006])

Msu4 = Parameter(name = 'Msu4',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{u}}_4}',
    lhablock = 'MASS',
    lhacode = [2000002])

Wsu4 = Parameter(name = 'Wsu4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{u}}_4}',
    lhablock = 'DECAY',
    lhacode = [2000002])

Msu5 = Parameter(name = 'Msu5',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{u}}_5}',
    lhablock = 'MASS',
    lhacode = [2000004])

Wsu5 = Parameter(name = 'Wsu5',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{u}}_5}',
    lhablock = 'DECAY',
    lhacode = [2000004])

Msu6 = Parameter(name = 'Msu6',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{u}}_6}',
    lhablock = 'MASS',
    lhacode = [2000006])

Wsu6 = Parameter(name = 'Wsu6',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{u}}_6}',
    lhablock = 'DECAY',
    lhacode = [2000006])

Mse1 = Parameter(name = 'Mse1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{e}}_1}',
    lhablock = 'MASS',
    lhacode = [1000011])

Wse1 = Parameter(name = 'Wse1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{e}}_1}',
    lhablock = 'DECAY',
    lhacode = [1000011])

Mse2 = Parameter(name = 'Mse2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{e}}_2}',
    lhablock = 'MASS',
    lhacode = [1000013])

Wse2 = Parameter(name = 'Wse2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{e}}_2}',
    lhablock = 'DECAY',
    lhacode = [1000013])

Mse3 = Parameter(name = 'Mse3',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{e}}_3}',
    lhablock = 'MASS',
    lhacode = [1000015])

Wse3 = Parameter(name = 'Wse3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{e}}_3}',
    lhablock = 'DECAY',
    lhacode = [1000015])

Mse4 = Parameter(name = 'Mse4',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{e}}_4}',
    lhablock = 'MASS',
    lhacode = [2000011])

Wse4 = Parameter(name = 'Wse4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{e}}_4}',
    lhablock = 'DECAY',
    lhacode = [2000011])

Mse5 = Parameter(name = 'Mse5',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{e}}_5}',
    lhablock = 'MASS',
    lhacode = [2000013])

Wse5 = Parameter(name = 'Wse5',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{e}}_5}',
    lhablock = 'DECAY',
    lhacode = [2000013])

Mse6 = Parameter(name = 'Mse6',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\tilde{e}}_6}',
    lhablock = 'MASS',
    lhacode = [2000015])

Wse6 = Parameter(name = 'Wse6',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\tilde{e}}_6}',
    lhablock = 'DECAY',
    lhacode = [2000015])

Mh1 = Parameter(name = 'Mh1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{h}_1}',
    lhablock = 'MASS',
    lhacode = [25])

Wh1 = Parameter(name = 'Wh1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{h}_1}',
    lhablock = 'DECAY',
    lhacode = [25])

Mh2 = Parameter(name = 'Mh2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{h}_2}',
    lhablock = 'MASS',
    lhacode = [35])

Wh2 = Parameter(name = 'Wh2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{h}_2}',
    lhablock = 'DECAY',
    lhacode = [35])

MAh2 = Parameter(name = 'MAh2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{A^0}_2}',
    lhablock = 'MASS',
    lhacode = [36])

WAh2 = Parameter(name = 'WAh2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{A^0}_2}',
    lhablock = 'DECAY',
    lhacode = [36])

MHm2 = Parameter(name = 'MHm2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{H^-}_2}',
    lhablock = 'MASS',
    lhacode = [37])

WHm2 = Parameter(name = 'WHm2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{H^-}_2}',
    lhablock = 'DECAY',
    lhacode = [37])

MZ = Parameter(name = 'MZ',
    nature = 'external',
    type = 'real',
    value = 91.1876,
    texname = 'M_{Z}',
    lhablock = 'MASS',
    lhacode = [23])

WZ = Parameter(name = 'WZ',
    nature = 'external',
    type = 'real',
    value = 2.4952,
    texname = '\\Gamma_{Z}',
    lhablock = 'DECAY',
    lhacode = [23])

WWm = Parameter(name = 'WWm',
    nature = 'external',
    type = 'real',
    value = 2.141,
    texname = '\\Gamma_{W^-}',
    lhablock = 'DECAY',
    lhacode = [24])

alphaH = Parameter(name='alphaH',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{alphaH}',
    lhablock = 'HMIX',
    lhacode = [11] )

betaH = Parameter(name='betaH',
    nature = 'external',
    type = 'real',
    value = 1.,
    texname = '\\text{betaH}',
    lhablock = 'HMIX',
    lhacode = [10] )

aS = Parameter(name='aS',
    nature = 'external',
    type = 'real',
    value = 0.119,
    texname = '\\text{aS}',
    lhablock = 'SMINPUTS',
    lhacode = [3] )

aEWM1 = Parameter(name='aEWM1',
    nature = 'external',
    type = 'real',
    value = 137.035999679,
    texname = '\\text{aEWM1}',
    lhablock = 'SMINPUTS',
    lhacode = [1] )

Gf = Parameter(name='Gf',
    nature = 'external',
    type = 'real',
    value = 0.0000116639,
    texname = 'G_f',
    lhablock = 'SMINPUTS',
    lhacode = [2] )

G = Parameter(name='G',
    nature = 'internal',
    type = 'real',
    value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
    texname = 'g_3')

ZH11 = Parameter(name='ZH11',
    nature = 'internal',
    type = 'real',
    value = '-cmath.sin(alphaH)',
    texname = '\\text{ZH11}')

ZH12 = Parameter(name='ZH12',
    nature = 'internal',
    type = 'real',
    value = 'cmath.cos(alphaH)',
    texname = '\\text{ZH12}')

ZH21 = Parameter(name='ZH21',
    nature = 'internal',
    type = 'real',
    value = 'cmath.cos(alphaH)',
    texname = '\\text{ZH21}')

ZH22 = Parameter(name='ZH22',
    nature = 'internal',
    type = 'real',
    value = 'cmath.sin(alphaH)',
    texname = '\\text{ZH22}')

ZA11 = Parameter(name='ZA11',
    nature = 'internal',
    type = 'real',
    value = '-cmath.cos(betaH)',
    texname = '\\text{ZA11}')

ZA12 = Parameter(name='ZA12',
    nature = 'internal',
    type = 'real',
    value = 'cmath.sin(betaH)',
    texname = '\\text{ZA12}')

ZA21 = Parameter(name='ZA21',
    nature = 'internal',
    type = 'real',
    value = 'cmath.sin(betaH)',
    texname = '\\text{ZA21}')

ZA22 = Parameter(name='ZA22',
    nature = 'internal',
    type = 'real',
    value = 'cmath.cos(betaH)',
    texname = '\\text{ZA22}')

ZP11 = Parameter(name='ZP11',
    nature = 'internal',
    type = 'real',
    value = '-cmath.cos(betaH)',
    texname = '\\text{ZP11}')

ZP12 = Parameter(name='ZP12',
    nature = 'internal',
    type = 'real',
    value = 'cmath.sin(betaH)',
    texname = '\\text{ZP12}')

ZP21 = Parameter(name='ZP21',
    nature = 'internal',
    type = 'real',
    value = 'cmath.sin(betaH)',
    texname = '\\text{ZP21}')

ZP22 = Parameter(name='ZP22',
    nature = 'internal',
    type = 'real',
    value = 'cmath.cos(betaH)',
    texname = '\\text{ZP22}')

el = Parameter(name='el',
    nature = 'internal',
    type = 'real',
    value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
    texname = '\\text{el}')

MWm = Parameter(name='MWm',
    nature = 'internal',
    type = 'real',
    value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (MZ**2*cmath.pi)/(cmath.sqrt(2)*aEWM1*Gf)))',
    texname = '\\text{MWm}')

TW = Parameter(name='TW',
    nature = 'internal',
    type = 'real',
    value = 'cmath.asin(cmath.sqrt(1 - MWm**2/MZ**2))',
    texname = '\\text{TW}')

g1 = Parameter(name='g1',
    nature = 'internal',
    type = 'real',
    value = 'el*1./cmath.cos(TW)',
    texname = 'g_1')

g2 = Parameter(name='g2',
    nature = 'internal',
    type = 'real',
    value = 'el*1./cmath.sin(TW)',
    texname = 'g_2')

v = Parameter(name='v',
    nature = 'internal',
    type = 'real',
    value = '2*cmath.sqrt(MWm**2/g2**2)',
    texname = 'v')

vd = Parameter(name='vd',
    nature = 'internal',
    type = 'real',
    value = 'v*cmath.cos(betaH)',
    texname = 'v_d')

vu = Parameter(name='vu',
    nature = 'internal',
    type = 'real',
    value = 'v*cmath.sin(betaH)',
    texname = 'v_u')

# Ghost and Goldstone parameters (needed for MadGraph)
MgZ = Parameter(name = 'MgZ',
    nature = 'external',
    type = 'real',
    value = 91.1876,
    texname = 'M_{gZ}',
    lhablock = 'MASS',
    lhacode = [0])

MgWm = Parameter(name = 'MgWm',
    nature = 'external',
    type = 'real',
    value = 80.385,
    texname = 'M_{gWm}',
    lhablock = 'MASS',
    lhacode = [0])

MgWpC = Parameter(name = 'MgWpC',
    nature = 'external',
    type = 'real',
    value = 80.385,
    texname = 'M_{gWpC}',
    lhablock = 'MASS',
    lhacode = [0])

MAh1 = Parameter(name = 'MAh1',
    nature = 'external',
    type = 'real',
    value = 0.0,
    texname = 'M_{A^0_1}',
    lhablock = 'MASS',
    lhacode = [0])

WAh1 = Parameter(name = 'WAh1',
    nature = 'external',
    type = 'real',
    value = 0.0,
    texname = '\\Gamma_{A^0_1}',
    lhablock = 'DECAY',
    lhacode = [0])

MHm1 = Parameter(name = 'MHm1',
    nature = 'external',
    type = 'real',
    value = 0.0,
    texname = 'M_{H^-_1}',
    lhablock = 'MASS',
    lhacode = [0])

WHm1 = Parameter(name = 'WHm1',
    nature = 'external',
    type = 'real',
    value = 0.0,
    texname = '\\Gamma_{H^-_1}',
    lhablock = 'DECAY',
    lhacode = [0])

WZ = Parameter(name = 'WZ',
    nature = 'external',
    type = 'real',
    value = 2.4952,
    texname = '\\Gamma_{Z}',
    lhablock = 'DECAY',
    lhacode = [23])

WWm = Parameter(name = 'WWm',
    nature = 'external',
    type = 'real',
    value = 2.141,
    texname = '\\Gamma_{W^-}',
    lhablock = 'DECAY',
    lhacode = [24])
