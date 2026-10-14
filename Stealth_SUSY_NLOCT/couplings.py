# This file was automatically created by FeynRules 2.4.43
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Wed 30 Nov 2016 08:56:02


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

GC_n1_a_S1 = Coupling(name = 'GC_n1_a_S1',
                      value = 'complex(0,1)*lambda_n1aS1 * alpha_em / (16**cmath.pi * MY)',
                      order = {'QED': 1})

GC_S1SGrav = Coupling(name = 'GC_S1SGrav',
                      value = 'complex(0,1)*c_S1SGrav',
                      order = {'QED': 1})


GC_Sgg = Coupling(name = 'GC_Sgg',
                  value = 'complex(0,1)*lambda_SYY * alpha_S / (6*cmath.sqrt(2)*cmath.pi * MY)',
                  order = {'QCD': 2})

GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '2*ee**2*complex(0,1)',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(ee**2*complex(0,1)*Rtau1x1**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(ee**2*complex(0,1)*Rtau2x1**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x2**2)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '(ee**2*complex(0,1)*Rtau2x1**2)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau2x2**2)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(ee**2*complex(0,1)*Rtau2x1**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x2**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '(ee**2*complex(0,1))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '(5*ee**2*complex(0,1))/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(ee**2*complex(0,1))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-G',
                 order = {'QCD':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(-2*ee**2*complex(0,1))/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(ee**2*complex(0,1))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(ee**2*complex(0,1))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '(ee**2*complex(0,1)*Rtau1x1**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '(ee**2*complex(0,1)*Rtau1x1**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x2**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '-(ee**2*complex(0,1)*Rtau1x1**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '-(ee**2*complex(0,1)*Rtau1x2**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '(ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '(ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '-(ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(complex(0,1)*G)',
                 order = {'QCD':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(ee**2*complex(0,1)*Rtau2x1**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x2**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau2x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '(ee**2*complex(0,1)*Rtau2x1**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau2x2**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau2x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '-(ee**2*complex(0,1)*Rtau2x1**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x2**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(ee**2*complex(0,1)*Rtau2x2**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(cw*ee*complex(0,1)*NN1x3**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN1x4**2)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(cw*ee*complex(0,1)*NN1x3*NN2x3)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN1x4*NN2x4)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(cw*ee*complex(0,1)*NN2x3**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN2x4**2)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(cw*ee*complex(0,1)*NN1x3*NN3x3)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN1x4*NN3x4)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(cw*ee*complex(0,1)*NN2x3*NN3x3)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN2x4*NN3x4)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(cw*ee*complex(0,1)*NN3x3**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN3x4**2)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(cw*ee*complex(0,1)*NN1x3*NN4x3)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN1x4*NN4x4)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(cw*ee*complex(0,1)*NN2x3*NN4x3)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN2x4*NN4x4)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(cw*ee*complex(0,1)*NN3x3*NN4x3)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN3x4*NN4x4)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(cw*ee*complex(0,1)*NN4x3**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN4x4**2)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'G/2.',
                 order = {'QCD':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-(cw*ee**2*complex(0,1))/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(-2*cw*ee**2*complex(0,1))/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((cw*ee**2*complex(0,1))/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '(cw*ee*complex(0,1)*G)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((cw*ee*complex(0,1)*G)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cw*ee*complex(0,1)*NN1x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((cw*ee*complex(0,1)*NN1x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN1x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(cw*ee*complex(0,1)*NN1x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((cw*ee*complex(0,1)*NN1x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN1x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(complex(0,1)*G*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(cw*ee*complex(0,1)*NN2x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((cw*ee*complex(0,1)*NN2x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN2x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(cw*ee*complex(0,1)*NN2x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((cw*ee*complex(0,1)*NN2x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN2x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(cw*ee*complex(0,1)*NN3x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((cw*ee*complex(0,1)*NN3x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN3x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(cw*ee*complex(0,1)*NN3x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((cw*ee*complex(0,1)*NN3x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN3x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(cw*ee*complex(0,1)*NN4x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((cw*ee*complex(0,1)*NN4x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN4x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*G*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(cw*ee*complex(0,1)*NN4x1)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((cw*ee*complex(0,1)*NN4x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN4x2)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(cw*ee*complex(0,1)*Rtau1x1**2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*Rtau1x1**2*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rtau1x2**2*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((cw*ee**2*complex(0,1)*Rtau1x1**2)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*Rtau1x1**2*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*Rtau1x2**2*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '(cw*ee*complex(0,1)*Rtau1x1*Rtau2x1)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*Rtau1x1*Rtau2x1*sw)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rtau1x2*Rtau2x2*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(cw*ee*complex(0,1)*Rtau1x1*Rtau2x1)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*Rtau1x1*Rtau2x1*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rtau1x2*Rtau2x2*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-((cw*ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*Rtau1x1*Rtau2x1*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*Rtau1x2*Rtau2x2*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(cw*ee*complex(0,1)*Rtau2x1**2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*Rtau2x1**2*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rtau2x2**2*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((cw*ee**2*complex(0,1)*Rtau2x1**2)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*Rtau2x1**2*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*Rtau2x2**2*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '(2*ee**2*complex(0,1))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '(-2*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(4*ee**2*complex(0,1))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '(2*ee**2*complex(0,1))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '(complex(0,1)*G**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((complex(0,1)*G**2)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '(2*ee**2*complex(0,1)*Rtau1x1**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau1x1**2*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau1x2**2*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '(2*ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau1x1*Rtau2x1*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau1x2*Rtau2x2*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '(2*ee**2*complex(0,1)*Rtau2x1**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau2x1**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau2x1**2*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau2x2**2*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((ee*complex(0,1)*UU1x1)/sw)',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((ee*complex(0,1)*NN1x2*UU1x1)/sw) - (ee*complex(0,1)*NN1x3*UU1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((ee*complex(0,1)*NN2x2*UU1x1)/sw) - (ee*complex(0,1)*NN2x3*UU1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(4*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((ee*complex(0,1)*NN3x2*UU1x1)/sw) - (ee*complex(0,1)*NN3x3*UU1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((ee*complex(0,1)*NN4x2*UU1x1)/sw) - (ee*complex(0,1)*NN4x3*UU1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = 'ee*complex(0,1)*UU1x1**2 + ee*complex(0,1)*UU1x2**2',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-((cw*ee*complex(0,1)*UU1x1**2)/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU1x1**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU1x2**2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU1x2**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((ee*complex(0,1)*UU2x1)/sw)',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((ee*complex(0,1)*NN1x2*UU2x1)/sw) - (ee*complex(0,1)*NN1x3*UU2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((ee*complex(0,1)*NN2x2*UU2x1)/sw) - (ee*complex(0,1)*NN2x3*UU2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((ee*complex(0,1)*NN3x2*UU2x1)/sw) - (ee*complex(0,1)*NN3x3*UU2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((ee*complex(0,1)*NN4x2*UU2x1)/sw) - (ee*complex(0,1)*NN4x3*UU2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = 'ee*complex(0,1)*UU1x1*UU2x1 + ee*complex(0,1)*UU1x2*UU2x2',
                  order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((cw*ee*complex(0,1)*UU1x1*UU2x1)/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU1x1*UU2x1)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU1x2*UU2x2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU1x2*UU2x2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = 'ee*complex(0,1)*UU2x1**2 + ee*complex(0,1)*UU2x2**2',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((cw*ee*complex(0,1)*UU2x1**2)/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU2x1**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU2x2**2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU2x2**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((ee*complex(0,1)*VV1x1)/sw)',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((ee*complex(0,1)*NN1x2*VV1x1)/sw) + (ee*complex(0,1)*NN1x4*VV1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((ee*complex(0,1)*NN2x2*VV1x1)/sw) + (ee*complex(0,1)*NN2x4*VV1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-((ee*complex(0,1)*NN3x2*VV1x1)/sw) + (ee*complex(0,1)*NN3x4*VV1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((ee*complex(0,1)*NN4x2*VV1x1)/sw) + (ee*complex(0,1)*NN4x4*VV1x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = 'ee*complex(0,1)*VV1x1**2 + ee*complex(0,1)*VV1x2**2',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((cw*ee*complex(0,1)*VV1x1**2)/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV1x1**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV1x2**2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV1x2**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'ee*complex(0,1)*Rtau1x1**2 + ee*complex(0,1)*Rtau1x2**2',
                 order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-((ee*complex(0,1)*VV2x1)/sw)',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((ee*complex(0,1)*NN1x2*VV2x1)/sw) + (ee*complex(0,1)*NN1x4*VV2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-((ee*complex(0,1)*NN2x2*VV2x1)/sw) + (ee*complex(0,1)*NN2x4*VV2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-((ee*complex(0,1)*NN3x2*VV2x1)/sw) + (ee*complex(0,1)*NN3x4*VV2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-((ee*complex(0,1)*NN4x2*VV2x1)/sw) + (ee*complex(0,1)*NN4x4*VV2x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = 'ee*complex(0,1)*VV1x1*VV2x1 + ee*complex(0,1)*VV1x2*VV2x2',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-((cw*ee*complex(0,1)*VV1x1*VV2x1)/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV1x1*VV2x1)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV1x2*VV2x2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV1x2*VV2x2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = 'ee*complex(0,1)*VV2x1**2 + ee*complex(0,1)*VV2x2**2',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-((cw*ee*complex(0,1)*VV2x1**2)/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV2x1**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV2x2**2)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV2x2**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = 'complex(0,1)*UU1x2*ye3x3',
                  order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '2*ee**2*complex(0,1)*Rtau1x1**2 + 2*ee**2*complex(0,1)*Rtau1x2**2',
                 order = {'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = 'complex(0,1)*UU2x2*ye3x3',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(complex(0,1)*NN1x3*Rtau1x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*Rtau1x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*Rtau1x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '(complex(0,1)*NN2x3*Rtau1x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*Rtau1x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*Rtau1x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(complex(0,1)*NN3x3*Rtau1x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*Rtau1x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*Rtau1x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(complex(0,1)*NN4x3*Rtau1x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*Rtau1x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*Rtau1x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(complex(0,1)*NN1x3*Rtau1x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*Rtau1x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*Rtau1x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*Rtau1x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*Rtau1x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(complex(0,1)*NN2x3*Rtau1x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*Rtau1x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*Rtau1x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*Rtau1x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*Rtau1x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(complex(0,1)*NN3x3*Rtau1x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*Rtau1x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*Rtau1x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*Rtau1x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*Rtau1x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '(complex(0,1)*NN4x3*Rtau1x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*Rtau1x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*Rtau1x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*Rtau1x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*Rtau1x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '(complex(0,1)*NN1x3*Rtau2x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*Rtau2x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*Rtau2x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(ee*complex(0,1)*Rtau1x1*Rtau2x1) - ee*complex(0,1)*Rtau1x2*Rtau2x2',
                 order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '(complex(0,1)*NN2x3*Rtau2x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*Rtau2x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*Rtau2x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '(complex(0,1)*NN3x3*Rtau2x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*Rtau2x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*Rtau2x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(complex(0,1)*NN4x3*Rtau2x1*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*Rtau2x1*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*Rtau2x2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(complex(0,1)*NN1x3*Rtau2x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*Rtau2x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*Rtau2x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*Rtau2x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*Rtau2x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(complex(0,1)*NN2x3*Rtau2x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*Rtau2x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*Rtau2x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*Rtau2x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*Rtau2x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(complex(0,1)*NN3x3*Rtau2x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*Rtau2x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*Rtau2x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*Rtau2x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*Rtau2x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '(complex(0,1)*NN4x3*Rtau2x2*ye3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*Rtau2x2*sw**2*ye3x3)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*Rtau2x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*Rtau2x1)/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*Rtau2x1*sw)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((ee*complex(0,1)*Rtau1x1*UU1x1)/sw) + complex(0,1)*Rtau1x2*UU1x2*ye3x3',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((ee*complex(0,1)*Rtau2x1*UU1x1)/sw) + complex(0,1)*Rtau2x2*UU1x2*ye3x3',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((ee*complex(0,1)*Rtau1x1*UU2x1)/sw) + complex(0,1)*Rtau1x2*UU2x2*ye3x3',
                  order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'ee*complex(0,1)*Rtau1x1*Rtau2x1 + ee*complex(0,1)*Rtau1x2*Rtau2x2',
                 order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((ee*complex(0,1)*Rtau2x1*UU2x1)/sw) + complex(0,1)*Rtau2x2*UU2x2*ye3x3',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-(ee**2*complex(0,1)*Rtau1x2**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*Rtau1x2**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*Rtau1x2**2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_232 = Coupling(name = 'GC_232',
                  value = '(-2*ee**2*complex(0,1)*Rtau1x1**2*Rtau1x2**2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*Rtau1x2**4)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1**4)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (4*complex(0,1)*Rtau1x1**2*Rtau1x2**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (4*complex(0,1)*Rtau1x1**2*Rtau1x2**2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_233 = Coupling(name = 'GC_233',
                  value = '-(ee**2*complex(0,1)*Rtau1x2*Rtau2x2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*Rtau1x2*Rtau2x2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*Rtau1x2*Rtau2x2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_234 = Coupling(name = 'GC_234',
                  value = '-((ee**2*complex(0,1)*Rtau1x1*Rtau1x2**2*Rtau2x1)/((-1 + sw)*(1 + sw))) - (ee**2*complex(0,1)*Rtau1x1**2*Rtau1x2*Rtau2x2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*Rtau1x2**3*Rtau2x2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1**3*Rtau2x1)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (2*complex(0,1)*Rtau1x1*Rtau1x2**2*Rtau2x1*ye3x3**2)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*Rtau1x1**2*Rtau1x2*Rtau2x2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*Rtau1x1*Rtau1x2**2*Rtau2x1*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*Rtau1x1**2*Rtau1x2*Rtau2x2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_235 = Coupling(name = 'GC_235',
                  value = '(-2*ee**2*complex(0,1)*Rtau1x1*Rtau1x2*Rtau2x1*Rtau2x2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*Rtau1x2**2*Rtau2x2**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1**2*Rtau2x1**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (4*complex(0,1)*Rtau1x1*Rtau1x2*Rtau2x1*Rtau2x2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (4*complex(0,1)*Rtau1x1*Rtau1x2*Rtau2x1*Rtau2x2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '-(ee**2*complex(0,1)*Rtau2x2**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x1**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*Rtau2x2**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*Rtau2x2**2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_237 = Coupling(name = 'GC_237',
                  value = '-(ee**2*complex(0,1)*Rtau1x2**2*Rtau2x1**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1*Rtau1x2*Rtau2x1*Rtau2x2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*Rtau1x1**2*Rtau2x2**2)/(2.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*Rtau1x2**2*Rtau2x2**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1**2*Rtau2x1**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*Rtau1x2**2*Rtau2x1**2*ye3x3**2)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*Rtau1x1*Rtau1x2*Rtau2x1*Rtau2x2*ye3x3**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*Rtau1x1**2*Rtau2x2**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*Rtau1x2**2*Rtau2x1**2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*Rtau1x1*Rtau1x2*Rtau2x1*Rtau2x2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*Rtau1x1**2*Rtau2x2**2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_238 = Coupling(name = 'GC_238',
                  value = '-((ee**2*complex(0,1)*Rtau1x2*Rtau2x1**2*Rtau2x2)/((-1 + sw)*(1 + sw))) - (ee**2*complex(0,1)*Rtau1x1*Rtau2x1*Rtau2x2**2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*Rtau1x2*Rtau2x2**3)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x1*Rtau2x1**3)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (2*complex(0,1)*Rtau1x2*Rtau2x1**2*Rtau2x2*ye3x3**2)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*Rtau1x1*Rtau2x1*Rtau2x2**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*Rtau1x2*Rtau2x1**2*Rtau2x2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*Rtau1x1*Rtau2x1*Rtau2x2**2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_239 = Coupling(name = 'GC_239',
                  value = '(-2*ee**2*complex(0,1)*Rtau2x1**2*Rtau2x2**2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*Rtau2x2**4)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau2x1**4)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (4*complex(0,1)*Rtau2x1**2*Rtau2x2**2*ye3x3**2)/((-1 + sw)*(1 + sw)) - (4*complex(0,1)*Rtau2x1**2*Rtau2x2**2*sw**2*ye3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '2*ee**2*complex(0,1)*Rtau1x1*Rtau2x1 + 2*ee**2*complex(0,1)*Rtau1x2*Rtau2x2',
                 order = {'QED':2})

GC_240 = Coupling(name = 'GC_240',
                  value = 'complex(0,1)*VV1x2*yu3x3',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = 'complex(0,1)*VV2x2*yu3x3',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '(complex(0,1)*NN1x4*yu3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x4*sw**2*yu3x3)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(complex(0,1)*NN2x4*yu3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x4*sw**2*yu3x3)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '(complex(0,1)*NN3x4*yu3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x4*sw**2*yu3x3)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '(complex(0,1)*NN4x4*yu3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x4*sw**2*yu3x3)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(complex(0,1)*yu3x3**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*sw**2*yu3x3**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = 'ee*complex(0,1)*Rtau2x1**2 + ee*complex(0,1)*Rtau2x2**2',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '2*ee**2*complex(0,1)*Rtau2x1**2 + 2*ee**2*complex(0,1)*Rtau2x2**2',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(ee**2*complex(0,1)) + (ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '2*ee**2*complex(0,1) - (2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = '(-2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(ee**2*complex(0,1)*Rtau1x1)/(2.*sw**2)',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ee**2*complex(0,1)*Rtau1x1**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(ee**2*complex(0,1)*Rtau2x1)/(2.*sw**2)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(ee**2*complex(0,1)*Rtau1x1*Rtau2x1)/(2.*sw**2)',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ee**2*complex(0,1)*Rtau2x1**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-((ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee**2*complex(0,1))/(3.*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-((ee**2*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(ee*complex(0,1)*G*cmath.sqrt(2))/sw',
                 order = {'QCD':1,'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((ee*complex(0,1)*Rtau1x1)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1)*Rtau1x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-((ee**2*complex(0,1)*Rtau1x1)/(sw*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((ee*complex(0,1)*Rtau2x1)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(ee*complex(0,1)*Rtau2x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-((ee**2*complex(0,1)*Rtau2x1)/(sw*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(ee**2*complex(0,1))/(18.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(ee**2*complex(0,1))/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(ee**2*complex(0,1))/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(ee**2*complex(0,1))/(6.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee**2*complex(0,1))/(6.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(-2*ee**2*complex(0,1))/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee**2*complex(0,1))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(4*ee**2*complex(0,1))/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(ee**2*complex(0,1))/(2.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(-2*ee**2*complex(0,1))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(ee**2*complex(0,1))/((-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(2*ee**2*complex(0,1))/((-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cw*ee**2*complex(0,1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((cw*ee**2*complex(0,1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(cw*ee*complex(0,1)*NN1x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(-2*cw*ee*complex(0,1)*NN1x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(cw*ee*complex(0,1)*NN1x1*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cw*ee*complex(0,1)*NN2x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(-2*cw*ee*complex(0,1)*NN2x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '(2*ee**2*complex(0,1))/9.',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cw*ee*complex(0,1)*NN2x1*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(cw*ee*complex(0,1)*NN3x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(-2*cw*ee*complex(0,1)*NN3x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(cw*ee*complex(0,1)*NN3x1*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(cw*ee*complex(0,1)*NN4x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(-2*cw*ee*complex(0,1)*NN4x1*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cw*ee*complex(0,1)*NN4x1*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((cw*ee**2*complex(0,1)*Rtau1x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((cw*ee**2*complex(0,1)*Rtau2x1)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                 order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(8*ee**2*complex(0,1))/9.',
                order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(-2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw)))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw))',
                 order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(2*cw*ee**2*complex(0,1)*sw)/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(8*cw*ee**2*complex(0,1)*sw)/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '(2*cw*ee**2*complex(0,1)*sw)/((-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(-2*cw*ee*complex(0,1)*G*sw)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QCD':1,'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(4*cw*ee*complex(0,1)*G*sw)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QCD':1,'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(-2*ee**2*complex(0,1)*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(-8*ee**2*complex(0,1)*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '(-2*ee**2*complex(0,1)*sw**2)/((-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(ee**2*complex(0,1)*Rtau1x1**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*Rtau1x2**2)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '(ee**2*complex(0,1)*Rtau1x1**2)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*Rtau1x2**2)/(3.*(-1 + sw)*(1 + sw))',
                 order = {'QED':2})

