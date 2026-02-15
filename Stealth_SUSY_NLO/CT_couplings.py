# This file was automatically created by FeynRules 1.7.221
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 7 Oct 2013 12:36:37


from object_library import all_couplings, Coupling
from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
import cmath

pi2 = cmath.pi**2

R2GC_Sgg = Coupling(name = 'R2GC_Sgg',
                    value = 'complex(0,1)*(-0.5)*gY*gY/(16*pi2)',
                    order = {'QCD': 2, 'QED': 0})

R2GC_SYY = Coupling(name = 'R2GC_SYY',
                    value = 'complex(0,1)*(-3)*gY/(16*pi2)',
                    order = {'QCD': 1, 'QED': 1})

UVGC_Sgg = Coupling(name = 'UVGC_Sgg',
                    value = 'complex(0,1)*gY*gY/(16*pi2)',
                    order = {'QCD': 2, 'QED': 0})

UVGC_SYY = Coupling(name = 'UVGC_SYY',
                    value = 'complex(0,1)*gY/(16*pi2)',
                    order = {'QCD': 1, 'QED': 1})

UVGC_YYg = Coupling(name = 'UVGC_YYg',
                    value = 'complex(0,1)*gS/(16*pi2)',
                    order = {'QCD': 2, 'QED': 0})
