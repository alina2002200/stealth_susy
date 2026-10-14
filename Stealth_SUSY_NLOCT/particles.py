# This file was automatically created by FeynRules 2.4.43
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Wed 30 Nov 2016 08:56:01


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             Y = 0)

n1 = Particle(pdg_code = 1000022,
              name = 'n1',
              antiname = 'n1',
              spin = 2,
              color = 1,
              mass = Param.Mneu1,
              width = Param.Wneu1,
              texname = 'n1',
              antitexname = 'n1',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

n2 = Particle(pdg_code = 1000023,
              name = 'n2',
              antiname = 'n2',
              spin = 2,
              color = 1,
              mass = Param.Mneu2,
              width = Param.Wneu2,
              texname = 'n2',
              antitexname = 'n2',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

n3 = Particle(pdg_code = 1000025,
              name = 'n3',
              antiname = 'n3',
              spin = 2,
              color = 1,
              mass = Param.Mneu3,
              width = Param.Wneu3,
              texname = 'n3',
              antitexname = 'n3',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

n4 = Particle(pdg_code = 1000035,
              name = 'n4',
              antiname = 'n4',
              spin = 2,
              color = 1,
              mass = Param.Mneu4,
              width = Param.Wneu4,
              texname = 'n4',
              antitexname = 'n4',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

x1__plus__ = Particle(pdg_code = 1000024,
                      name = 'x1+',
                      antiname = 'x1-',
                      spin = 2,
                      color = 1,
                      mass = Param.Mch1,
                      width = Param.Wch1,
                      texname = 'x1+',
                      antitexname = 'x1-',
                      charge = 1,
                      GhostNumber = 0,
                      Y = 0)

x1__minus__ = x1__plus__.anti()

x2__plus__ = Particle(pdg_code = 1000037,
                      name = 'x2+',
                      antiname = 'x2-',
                      spin = 2,
                      color = 1,
                      mass = Param.Mch2,
                      width = Param.Wch2,
                      texname = 'x2+',
                      antitexname = 'x2-',
                      charge = 1,
                      GhostNumber = 0,
                      Y = 0)

x2__minus__ = x2__plus__.anti()

go = Particle(pdg_code = 1000021,
              name = 'go',
              antiname = 'go',
              spin = 2,
              color = 8,
              mass = Param.Mgo,
              width = Param.Wgo,
              texname = 'go',
              antitexname = 'go',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

tau__minus__ = Particle(pdg_code = 15,
                        name = 'tau-',
                        antiname = 'tau+',
                        spin = 2,
                        color = 1,
                        mass = Param.MTA,
                        width = Param.ZERO,
                        texname = 'tau-',
                        antitexname = 'tau+',
                        charge = -1,
                        GhostNumber = 0,
                        Y = 0)

tau__plus__ = tau__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

sne = Particle(pdg_code = 1000012,
               name = 'sne',
               antiname = 'sne~',
               spin = 1,
               color = 1,
               mass = Param.Msne,
               width = Param.Wsne,
               texname = 'sne',
               antitexname = 'sne~',
               charge = 0,
               GhostNumber = 0,
               Y = 0)

sne__tilde__ = sne.anti()

snm = Particle(pdg_code = 1000014,
               name = 'snm',
               antiname = 'snm~',
               spin = 1,
               color = 1,
               mass = Param.Msnm,
               width = Param.Wsnm,
               texname = 'snm',
               antitexname = 'snm~',
               charge = 0,
               GhostNumber = 0,
               Y = 0)

snm__tilde__ = snm.anti()

snt = Particle(pdg_code = 1000016,
               name = 'snt',
               antiname = 'snt~',
               spin = 1,
               color = 1,
               mass = Param.Msnt,
               width = Param.Wsnt,
               texname = 'snt',
               antitexname = 'snt~',
               charge = 0,
               GhostNumber = 0,
               Y = 0)

snt__tilde__ = snt.anti()

seL__minus__ = Particle(pdg_code = 1000011,
                        name = 'seL-',
                        antiname = 'seL+',
                        spin = 1,
                        color = 1,
                        mass = Param.MseL,
                        width = Param.WseL,
                        texname = 'seL-',
                        antitexname = 'seL+',
                        charge = -1,
                        GhostNumber = 0,
                        Y = 0)

seL__plus__ = seL__minus__.anti()

smuL__minus__ = Particle(pdg_code = 1000013,
                         name = 'smuL-',
                         antiname = 'smuL+',
                         spin = 1,
                         color = 1,
                         mass = Param.MsmuL,
                         width = Param.WsmuL,
                         texname = 'smuL-',
                         antitexname = 'smuL+',
                         charge = -1,
                         GhostNumber = 0,
                         Y = 0)

smuL__plus__ = smuL__minus__.anti()

stau1__minus__ = Particle(pdg_code = 1000015,
                          name = 'stau1-',
                          antiname = 'stau1+',
                          spin = 1,
                          color = 1,
                          mass = Param.Mstau1,
                          width = Param.Wstau1,
                          texname = 'stau1-',
                          antitexname = 'stau1+',
                          charge = -1,
                          GhostNumber = 0,
                          Y = 0)

stau1__plus__ = stau1__minus__.anti()

seR__minus__ = Particle(pdg_code = 2000011,
                        name = 'seR-',
                        antiname = 'seR+',
                        spin = 1,
                        color = 1,
                        mass = Param.MseR,
                        width = Param.WseR,
                        texname = 'seR-',
                        antitexname = 'seR+',
                        charge = -1,
                        GhostNumber = 0,
                        Y = 0)

seR__plus__ = seR__minus__.anti()

smuR__minus__ = Particle(pdg_code = 2000013,
                         name = 'smuR-',
                         antiname = 'smuR+',
                         spin = 1,
                         color = 1,
                         mass = Param.MsmuR,
                         width = Param.WsmuR,
                         texname = 'smuR-',
                         antitexname = 'smuR+',
                         charge = -1,
                         GhostNumber = 0,
                         Y = 0)

smuR__plus__ = smuR__minus__.anti()

stau2__minus__ = Particle(pdg_code = 2000015,
                          name = 'stau2-',
                          antiname = 'stau2+',
                          spin = 1,
                          color = 1,
                          mass = Param.Mstau2,
                          width = Param.Wstau2,
                          texname = 'stau2-',
                          antitexname = 'stau2+',
                          charge = -1,
                          GhostNumber = 0,
                          Y = 0)

stau2__plus__ = stau2__minus__.anti()

suL = Particle(pdg_code = 1000002,
               name = 'suL',
               antiname = 'suL~',
               spin = 1,
               color = 3,
               mass = Param.MsuL,
               width = Param.WsuL,
               texname = 'suL',
               antitexname = 'suL~',
               charge = 2/3,
               GhostNumber = 0,
               Y = 0)

suL__tilde__ = suL.anti()

scL = Particle(pdg_code = 1000004,
               name = 'scL',
               antiname = 'scL~',
               spin = 1,
               color = 3,
               mass = Param.MscL,
               width = Param.WscL,
               texname = 'scL',
               antitexname = 'scL~',
               charge = 2/3,
               GhostNumber = 0,
               Y = 0)

scL__tilde__ = scL.anti()

stL = Particle(pdg_code = 1000006,
               name = 'stL',
               antiname = 'stL~',
               spin = 1,
               color = 3,
               mass = Param.MstL,
               width = Param.WstL,
               texname = 'stL',
               antitexname = 'stL~',
               charge = 2/3,
               GhostNumber = 0,
               Y = 0)

stL__tilde__ = stL.anti()

suR = Particle(pdg_code = 2000002,
               name = 'suR',
               antiname = 'suR~',
               spin = 1,
               color = 3,
               mass = Param.MsuR,
               width = Param.WsuR,
               texname = 'suR',
               antitexname = 'suR~',
               charge = 2/3,
               GhostNumber = 0,
               Y = 0)

suR__tilde__ = suR.anti()

scR = Particle(pdg_code = 2000004,
               name = 'scR',
               antiname = 'scR~',
               spin = 1,
               color = 3,
               mass = Param.MscR,
               width = Param.WscR,
               texname = 'scR',
               antitexname = 'scR~',
               charge = 2/3,
               GhostNumber = 0,
               Y = 0)

scR__tilde__ = scR.anti()

stR = Particle(pdg_code = 2000006,
               name = 'stR',
               antiname = 'stR~',
               spin = 1,
               color = 3,
               mass = Param.MstR,
               width = Param.WstR,
               texname = 'stR',
               antitexname = 'stR~',
               charge = 2/3,
               GhostNumber = 0,
               Y = 0)

stR__tilde__ = stR.anti()

sdL = Particle(pdg_code = 1000001,
               name = 'sdL',
               antiname = 'sdL~',
               spin = 1,
               color = 3,
               mass = Param.MsdL,
               width = Param.WsdL,
               texname = 'sdL',
               antitexname = 'sdL~',
               charge = -1/3,
               GhostNumber = 0,
               Y = 0)

sdL__tilde__ = sdL.anti()

ssL = Particle(pdg_code = 1000003,
               name = 'ssL',
               antiname = 'ssL~',
               spin = 1,
               color = 3,
               mass = Param.MssL,
               width = Param.WssL,
               texname = 'ssL',
               antitexname = 'ssL~',
               charge = -1/3,
               GhostNumber = 0,
               Y = 0)

ssL__tilde__ = ssL.anti()

sbL = Particle(pdg_code = 1000005,
               name = 'sbL',
               antiname = 'sbL~',
               spin = 1,
               color = 3,
               mass = Param.MsbL,
               width = Param.WsbL,
               texname = 'sbL',
               antitexname = 'sbL~',
               charge = -1/3,
               GhostNumber = 0,
               Y = 0)

sbL__tilde__ = sbL.anti()

sdR = Particle(pdg_code = 2000001,
               name = 'sdR',
               antiname = 'sdR~',
               spin = 1,
               color = 3,
               mass = Param.MsdR,
               width = Param.WsdR,
               texname = 'sdR',
               antitexname = 'sdR~',
               charge = -1/3,
               GhostNumber = 0,
               Y = 0)

sdR__tilde__ = sdR.anti()

ssR = Particle(pdg_code = 2000003,
               name = 'ssR',
               antiname = 'ssR~',
               spin = 1,
               color = 3,
               mass = Param.MssR,
               width = Param.WssR,
               texname = 'ssR',
               antitexname = 'ssR~',
               charge = -1/3,
               GhostNumber = 0,
               Y = 0)

ssR__tilde__ = ssR.anti()

sbR = Particle(pdg_code = 2000005,
               name = 'sbR',
               antiname = 'sbR~',
               spin = 1,
               color = 3,
               mass = Param.MsbR,
               width = Param.WsbR,
               texname = 'sbR',
               antitexname = 'sbR~',
               charge = -1/3,
               GhostNumber = 0,
               Y = 0)

sbR__tilde__ = sbR.anti()

ghG = Particle(pdg_code = 9000001,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               Y = 0)

ghG__tilde__ = ghG.anti()

