# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Sun 2 Oct 2016 21:08:27


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
             YBL = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.ZERO,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             YBL = 0)

Zp = Particle(pdg_code = 32,
              name = 'Zp',
              antiname = 'Zp',
              spin = 3,
              color = 1,
              mass = Param.MZp,
              width = Param.ZERO,
              texname = 'Zp',
              antitexname = 'Zp',
              charge = 0,
              YBL = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.ZERO,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     YBL = 0)

W__minus__ = W__plus__.anti()

Wp__plus__ = Particle(pdg_code = 34,
                      name = 'Wp+',
                      antiname = 'Wp-',
                      spin = 3,
                      color = 1,
                      mass = Param.MWp,
                      width = Param.ZERO,
                      texname = 'Wp+',
                      antitexname = 'Wp-',
                      charge = 1,
                      YBL = 0)

Wp__minus__ = Wp__plus__.anti()

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
             YBL = 0)

h01 = Particle(pdg_code = 25,
               name = 'h01',
               antiname = 'h01',
               spin = 1,
               color = 1,
               mass = Param.Mh01,
               width = Param.ZERO,
               texname = 'h01',
               antitexname = 'h01',
               charge = 0,
               YBL = 0)

h02 = Particle(pdg_code = 35,
               name = 'h02',
               antiname = 'h02',
               spin = 1,
               color = 1,
               mass = Param.Mh02,
               width = Param.ZERO,
               texname = 'h02',
               antitexname = 'h02',
               charge = 0,
               YBL = 0)

h03 = Particle(pdg_code = 45,
               name = 'h03',
               antiname = 'h03',
               spin = 1,
               color = 1,
               mass = Param.Mh03,
               width = Param.ZERO,
               texname = 'h03',
               antitexname = 'h03',
               charge = 0,
               YBL = 0)

h04 = Particle(pdg_code = 9000025,
               name = 'h04',
               antiname = 'h04',
               spin = 1,
               color = 1,
               mass = Param.Mh04,
               width = Param.ZERO,
               texname = 'h04',
               antitexname = 'h04',
               charge = 0,
               YBL = 0)

a01 = Particle(pdg_code = 36,
               name = 'a01',
               antiname = 'a01',
               spin = 1,
               color = 1,
               mass = Param.MA0,
               width = Param.ZERO,
               texname = 'a01',
               antitexname = 'a01',
               charge = 0,
               YBL = 0)

a02 = Particle(pdg_code = 46,
               name = 'a02',
               antiname = 'a02',
               spin = 1,
               color = 1,
               mass = Param.MA01,
               width = Param.ZERO,
               texname = 'a02',
               antitexname = 'a02',
               charge = 0,
               YBL = 0)

H1__plus__ = Particle(pdg_code = 37,
                      name = 'H1+',
                      antiname = 'H1-',
                      spin = 1,
                      color = 1,
                      mass = Param.MH1,
                      width = Param.ZERO,
                      texname = 'H1+',
                      antitexname = 'H1-',
                      charge = 1,
                      YBL = 0)

H1__minus__ = H1__plus__.anti()

H2__plus__ = Particle(pdg_code = 9000037,
                      name = 'H2+',
                      antiname = 'H2-',
                      spin = 1,
                      color = 1,
                      mass = Param.MH2,
                      width = Param.ZERO,
                      texname = 'H2+',
                      antitexname = 'H2-',
                      charge = 1,
                      YBL = 0)

H2__minus__ = H2__plus__.anti()

H1__plus____plus__ = Particle(pdg_code = 9000055,
                              name = 'H1++',
                              antiname = 'H1--',
                              spin = 1,
                              color = 1,
                              mass = Param.MDH1,
                              width = Param.ZERO,
                              texname = 'H1++',
                              antitexname = 'H1--',
                              charge = 2,
                              YBL = 0)

H1__minus____minus__ = H1__plus____plus__.anti()

H2__plus____plus__ = Particle(pdg_code = 9000056,
                              name = 'H2++',
                              antiname = 'H2--',
                              spin = 1,
                              color = 1,
                              mass = Param.MDH2,
                              width = Param.ZERO,
                              texname = 'H2++',
                              antitexname = 'H2--',
                              charge = 2,
                              YBL = 0)

H2__minus____minus__ = H2__plus____plus__.anti()

G01 = Particle(pdg_code = 250,
               name = 'G01',
               antiname = 'G01',
               spin = 1,
               color = 1,
               mass = Param.MZ,
               width = Param.ZERO,
               texname = 'G01',
               antitexname = 'G01',
               goldstone = True,
               charge = 0,
               YBL = 0)

G02 = Particle(pdg_code = 251,
               name = 'G02',
               antiname = 'G02',
               spin = 1,
               color = 1,
               mass = Param.MZp,
               width = Param.ZERO,
               texname = 'G02',
               antitexname = 'G02',
               goldstone = True,
               charge = 0,
               YBL = 0)

G1__plus__ = Particle(pdg_code = 252,
                      name = 'G1+',
                      antiname = 'G1-',
                      spin = 1,
                      color = 1,
                      mass = Param.MW,
                      width = Param.ZERO,
                      texname = 'G1+',
                      antitexname = 'G1-',
                      goldstone = True,
                      charge = 1,
                      YBL = 0)

G1__minus__ = G1__plus__.anti()

G2__plus__ = Particle(pdg_code = 253,
                      name = 'G2+',
                      antiname = 'G2-',
                      spin = 1,
                      color = 1,
                      mass = Param.MWp,
                      width = Param.ZERO,
                      texname = 'G2+',
                      antitexname = 'G2-',
                      goldstone = True,
                      charge = 1,
                      YBL = 0)

G2__minus__ = G2__plus__.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.Mve,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              YBL = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.Mvm,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              YBL = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.Mvt,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              YBL = 0)

vt__tilde__ = vt.anti()

Ne = Particle(pdg_code = 6000012,
              name = 'Ne',
              antiname = 'Ne~',
              spin = 2,
              color = 1,
              mass = Param.MNe,
              width = Param.ZERO,
              texname = 'Ne',
              antitexname = 'Ne~',
              charge = 0,
              YBL = 0)

Ne__tilde__ = Ne.anti()

Nm = Particle(pdg_code = 6000014,
              name = 'Nm',
              antiname = 'Nm~',
              spin = 2,
              color = 1,
              mass = Param.MNm,
              width = Param.ZERO,
              texname = 'Nm',
              antitexname = 'Nm~',
              charge = 0,
              YBL = 0)

Nm__tilde__ = Nm.anti()

Nt = Particle(pdg_code = 6000016,
              name = 'Nt',
              antiname = 'Nt~',
              spin = 2,
              color = 1,
              mass = Param.MNt,
              width = Param.ZERO,
              texname = 'Nt',
              antitexname = 'Nt~',
              charge = 0,
              YBL = 0)

Nt__tilde__ = Nt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      YBL = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.Mm,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       YBL = 0)

mu__plus__ = mu__minus__.anti()

tau__minus__ = Particle(pdg_code = 15,
                        name = 'tau-',
                        antiname = 'tau+',
                        spin = 2,
                        color = 1,
                        mass = Param.Mta,
                        width = Param.ZERO,
                        texname = 'tau-',
                        antitexname = 'tau+',
                        charge = -1,
                        YBL = 0)

tau__plus__ = tau__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             YBL = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             YBL = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.ZERO,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             YBL = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             YBL = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             YBL = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             YBL = 0)

b__tilde__ = b.anti()

