# This file was automatically created by FeynRules 1.7.221
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 7 Oct 2013 12:36:37


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot


GC_Sgg_ct = Coupling(name = 'GC_Sgg_ct',
                     value = 'complex(0,1)*gY**2/(16*pi**2) * (1/eps)',
                     order = {'QCD': 2})

GC_SYY_ct = Coupling(name = 'GC_SYY_ct',
                     value = 'complex(0,1)*gY/(16*pi**2) * (1/eps)',
                     order = {'QCD': 1})
