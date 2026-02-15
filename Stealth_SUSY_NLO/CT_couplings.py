# This file was automatically created by FeynRules 1.7.221
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 7 Oct 2013 12:36:37


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

import cmath

pi2 = 9.869604401089358

GC_Sgg_r2 = Coupling(name = 'GC_Sgg_r2',
                     value = 'complex(0,1)*(-0.5)*gY*gY/(16*{})'.format(pi2),
                     order = {'QCD': 2})

GC_SYY_r2 = Coupling(name = 'GC_SYY_r2',
                     value = 'complex(0,1)*(-3)*gY/(16*{})'.format(pi2),
                     order = {'QCD': 1})

GC_Sgg_ct = Coupling(name = 'GC_Sgg_ct',
                     value = 'complex(0,1)*gY*gY/(16*{})'.format(pi2),
                     order = {'QCD': 2})

GC_SYY_ct = Coupling(name = 'GC_SYY_ct',
                     value = 'complex(0,1)*gY/(16*{})'.format(pi2),
                     order = {'QCD': 1})

GC_YYg_ct = Coupling(name = 'GC_YYg_ct',
                     value = 'complex(0,1)*gS/(16*{})'.format(pi2),
                     order = {'QCD': 2})
