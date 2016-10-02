# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Sun 2 Oct 2016 21:08:28



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
vR = Parameter(name = 'vR',
               nature = 'external',
               type = 'real',
               value = 1000,
               texname = 'v_{\\text{R}}',
               lhablock = 'FRVevs',
               lhacode = [ 1 ])

vL = Parameter(name = 'vL',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'v_{\\text{L}}',
               lhablock = 'FRVevs',
               lhacode = [ 2 ])

v1 = Parameter(name = 'v1',
               nature = 'external',
               type = 'real',
               value = 248,
               texname = 'v_1',
               lhablock = 'FRVevs',
               lhacode = [ 3 ])

v1p = Parameter(name = 'v1p',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{Subsuperscript}[v,1,\']',
                lhablock = 'FRVevs',
                lhacode = [ 4 ])

gY = Parameter(name = 'gY',
               nature = 'external',
               type = 'real',
               value = 0.360966847,
               texname = 'g_Y',
               lhablock = 'Gauge',
               lhacode = [ 1 ])

gL = Parameter(name = 'gL',
               nature = 'external',
               type = 'real',
               value = 0.64648221,
               texname = 'g_L',
               lhablock = 'Gauge',
               lhacode = [ 2 ])

gR = Parameter(name = 'gR',
               nature = 'external',
               type = 'real',
               value = 0.64648221,
               texname = 'g_R',
               lhablock = 'Gauge',
               lhacode = [ 4 ])

RAL1 = Parameter(name = 'RAL1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{RAL1}',
                 lhablock = 'HAL',
                 lhacode = [ 1 ])

RAL2 = Parameter(name = 'RAL2',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{RAL2}',
                 lhablock = 'HAL',
                 lhacode = [ 2 ])

RAL3 = Parameter(name = 'RAL3',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{RAL3}',
                 lhablock = 'HAL',
                 lhacode = [ 3 ])

RLAM1 = Parameter(name = 'RLAM1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RLAM1}',
                  lhablock = 'HLAM',
                  lhacode = [ 1 ])

RLAM2 = Parameter(name = 'RLAM2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RLAM2}',
                  lhablock = 'HLAM',
                  lhacode = [ 2 ])

RLAM3 = Parameter(name = 'RLAM3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RLAM3}',
                  lhablock = 'HLAM',
                  lhacode = [ 3 ])

RLAM4 = Parameter(name = 'RLAM4',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RLAM4}',
                  lhablock = 'HLAM',
                  lhacode = [ 4 ])

RLAM5 = Parameter(name = 'RLAM5',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RLAM5}',
                  lhablock = 'HLAM',
                  lhacode = [ 5 ])

RLAM6 = Parameter(name = 'RLAM6',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RLAM6}',
                  lhablock = 'HLAM',
                  lhacode = [ 6 ])

RRHO1 = Parameter(name = 'RRHO1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRHO1}',
                  lhablock = 'HRHO',
                  lhacode = [ 1 ])

RRHO2 = Parameter(name = 'RRHO2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRHO2}',
                  lhablock = 'HRHO',
                  lhacode = [ 2 ])

RRHO3 = Parameter(name = 'RRHO3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRHO3}',
                  lhablock = 'HRHO',
                  lhacode = [ 3 ])

IAL1 = Parameter(name = 'IAL1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{IAL1}',
                 lhablock = 'IMAL',
                 lhacode = [ 1 ])

IAL2 = Parameter(name = 'IAL2',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{IAL2}',
                 lhablock = 'IMAL',
                 lhacode = [ 2 ])

IAL3 = Parameter(name = 'IAL3',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{IAL3}',
                 lhablock = 'IMAL',
                 lhacode = [ 3 ])

ILAM1 = Parameter(name = 'ILAM1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{ILAM1}',
                  lhablock = 'IMHLAM',
                  lhacode = [ 1 ])

ILAM2 = Parameter(name = 'ILAM2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{ILAM2}',
                  lhablock = 'IMHLAM',
                  lhacode = [ 2 ])

ILAM3 = Parameter(name = 'ILAM3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{ILAM3}',
                  lhablock = 'IMHLAM',
                  lhacode = [ 3 ])

ILAM4 = Parameter(name = 'ILAM4',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{ILAM4}',
                  lhablock = 'IMHLAM',
                  lhacode = [ 4 ])

ILAM5 = Parameter(name = 'ILAM5',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{ILAM5}',
                  lhablock = 'IMHLAM',
                  lhacode = [ 5 ])

ILAM6 = Parameter(name = 'ILAM6',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{ILAM6}',
                  lhablock = 'IMHLAM',
                  lhacode = [ 6 ])

IRHO1 = Parameter(name = 'IRHO1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{IRHO1}',
                  lhablock = 'IMRHO',
                  lhacode = [ 1 ])

IRHO2 = Parameter(name = 'IRHO2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{IRHO2}',
                  lhablock = 'IMRHO',
                  lhacode = [ 2 ])

IRHO3 = Parameter(name = 'IRHO3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{IRHO3}',
                  lhablock = 'IMRHO',
                  lhacode = [ 3 ])

Iyl11x1 = Parameter(name = 'Iyl11x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl11x1}',
                    lhablock = 'IMYL1',
                    lhacode = [ 1, 1 ])

Iyl11x2 = Parameter(name = 'Iyl11x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl11x2}',
                    lhablock = 'IMYL1',
                    lhacode = [ 1, 2 ])

Iyl11x3 = Parameter(name = 'Iyl11x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl11x3}',
                    lhablock = 'IMYL1',
                    lhacode = [ 1, 3 ])

Iyl12x1 = Parameter(name = 'Iyl12x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl12x1}',
                    lhablock = 'IMYL1',
                    lhacode = [ 2, 1 ])

Iyl12x2 = Parameter(name = 'Iyl12x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl12x2}',
                    lhablock = 'IMYL1',
                    lhacode = [ 2, 2 ])

Iyl12x3 = Parameter(name = 'Iyl12x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl12x3}',
                    lhablock = 'IMYL1',
                    lhacode = [ 2, 3 ])

Iyl13x1 = Parameter(name = 'Iyl13x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl13x1}',
                    lhablock = 'IMYL1',
                    lhacode = [ 3, 1 ])

Iyl13x2 = Parameter(name = 'Iyl13x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl13x2}',
                    lhablock = 'IMYL1',
                    lhacode = [ 3, 2 ])

Iyl13x3 = Parameter(name = 'Iyl13x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl13x3}',
                    lhablock = 'IMYL1',
                    lhacode = [ 3, 3 ])

Iyl21x1 = Parameter(name = 'Iyl21x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl21x1}',
                    lhablock = 'IMYL2',
                    lhacode = [ 1, 1 ])

Iyl21x2 = Parameter(name = 'Iyl21x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl21x2}',
                    lhablock = 'IMYL2',
                    lhacode = [ 1, 2 ])

Iyl21x3 = Parameter(name = 'Iyl21x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl21x3}',
                    lhablock = 'IMYL2',
                    lhacode = [ 1, 3 ])

Iyl22x1 = Parameter(name = 'Iyl22x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl22x1}',
                    lhablock = 'IMYL2',
                    lhacode = [ 2, 1 ])

Iyl22x2 = Parameter(name = 'Iyl22x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl22x2}',
                    lhablock = 'IMYL2',
                    lhacode = [ 2, 2 ])

Iyl22x3 = Parameter(name = 'Iyl22x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl22x3}',
                    lhablock = 'IMYL2',
                    lhacode = [ 2, 3 ])

Iyl23x1 = Parameter(name = 'Iyl23x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl23x1}',
                    lhablock = 'IMYL2',
                    lhacode = [ 3, 1 ])

Iyl23x2 = Parameter(name = 'Iyl23x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl23x2}',
                    lhablock = 'IMYL2',
                    lhacode = [ 3, 2 ])

Iyl23x3 = Parameter(name = 'Iyl23x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl23x3}',
                    lhablock = 'IMYL2',
                    lhacode = [ 3, 3 ])

Iyl31x1 = Parameter(name = 'Iyl31x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl31x1}',
                    lhablock = 'IMYL3',
                    lhacode = [ 1, 1 ])

Iyl31x2 = Parameter(name = 'Iyl31x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl31x2}',
                    lhablock = 'IMYL3',
                    lhacode = [ 1, 2 ])

Iyl31x3 = Parameter(name = 'Iyl31x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl31x3}',
                    lhablock = 'IMYL3',
                    lhacode = [ 1, 3 ])

Iyl32x1 = Parameter(name = 'Iyl32x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl32x1}',
                    lhablock = 'IMYL3',
                    lhacode = [ 2, 1 ])

Iyl32x2 = Parameter(name = 'Iyl32x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl32x2}',
                    lhablock = 'IMYL3',
                    lhacode = [ 2, 2 ])

Iyl32x3 = Parameter(name = 'Iyl32x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl32x3}',
                    lhablock = 'IMYL3',
                    lhacode = [ 2, 3 ])

Iyl33x1 = Parameter(name = 'Iyl33x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl33x1}',
                    lhablock = 'IMYL3',
                    lhacode = [ 3, 1 ])

Iyl33x2 = Parameter(name = 'Iyl33x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl33x2}',
                    lhablock = 'IMYL3',
                    lhacode = [ 3, 2 ])

Iyl33x3 = Parameter(name = 'Iyl33x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl33x3}',
                    lhablock = 'IMYL3',
                    lhacode = [ 3, 3 ])

Iyl41x1 = Parameter(name = 'Iyl41x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl41x1}',
                    lhablock = 'IMYL4',
                    lhacode = [ 1, 1 ])

Iyl41x2 = Parameter(name = 'Iyl41x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl41x2}',
                    lhablock = 'IMYL4',
                    lhacode = [ 1, 2 ])

Iyl41x3 = Parameter(name = 'Iyl41x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl41x3}',
                    lhablock = 'IMYL4',
                    lhacode = [ 1, 3 ])

Iyl42x1 = Parameter(name = 'Iyl42x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl42x1}',
                    lhablock = 'IMYL4',
                    lhacode = [ 2, 1 ])

Iyl42x2 = Parameter(name = 'Iyl42x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl42x2}',
                    lhablock = 'IMYL4',
                    lhacode = [ 2, 2 ])

Iyl42x3 = Parameter(name = 'Iyl42x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl42x3}',
                    lhablock = 'IMYL4',
                    lhacode = [ 2, 3 ])

Iyl43x1 = Parameter(name = 'Iyl43x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl43x1}',
                    lhablock = 'IMYL4',
                    lhacode = [ 3, 1 ])

Iyl43x2 = Parameter(name = 'Iyl43x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl43x2}',
                    lhablock = 'IMYL4',
                    lhacode = [ 3, 2 ])

Iyl43x3 = Parameter(name = 'Iyl43x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyl43x3}',
                    lhablock = 'IMYL4',
                    lhacode = [ 3, 3 ])

Iyq11x1 = Parameter(name = 'Iyq11x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq11x1}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 1, 1 ])

Iyq11x2 = Parameter(name = 'Iyq11x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq11x2}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 1, 2 ])

Iyq11x3 = Parameter(name = 'Iyq11x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq11x3}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 1, 3 ])

Iyq12x1 = Parameter(name = 'Iyq12x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq12x1}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 2, 1 ])

Iyq12x2 = Parameter(name = 'Iyq12x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq12x2}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 2, 2 ])

Iyq12x3 = Parameter(name = 'Iyq12x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq12x3}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 2, 3 ])

Iyq13x1 = Parameter(name = 'Iyq13x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq13x1}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 3, 1 ])

Iyq13x2 = Parameter(name = 'Iyq13x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq13x2}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 3, 2 ])

Iyq13x3 = Parameter(name = 'Iyq13x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq13x3}',
                    lhablock = 'IMYQ1',
                    lhacode = [ 3, 3 ])

Iyq21x1 = Parameter(name = 'Iyq21x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq21x1}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 1, 1 ])

Iyq21x2 = Parameter(name = 'Iyq21x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq21x2}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 1, 2 ])

Iyq21x3 = Parameter(name = 'Iyq21x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq21x3}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 1, 3 ])

Iyq22x1 = Parameter(name = 'Iyq22x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq22x1}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 2, 1 ])

Iyq22x2 = Parameter(name = 'Iyq22x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq22x2}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 2, 2 ])

Iyq22x3 = Parameter(name = 'Iyq22x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq22x3}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 2, 3 ])

Iyq23x1 = Parameter(name = 'Iyq23x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq23x1}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 3, 1 ])

Iyq23x2 = Parameter(name = 'Iyq23x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq23x2}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 3, 2 ])

Iyq23x3 = Parameter(name = 'Iyq23x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Iyq23x3}',
                    lhablock = 'IMYQ2',
                    lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{Subsuperscript}[\\alpha ,w,-1]',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 5 ])

Ryl11x1 = Parameter(name = 'Ryl11x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl11x1}',
                    lhablock = 'YL1',
                    lhacode = [ 1, 1 ])

Ryl11x2 = Parameter(name = 'Ryl11x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl11x2}',
                    lhablock = 'YL1',
                    lhacode = [ 1, 2 ])

Ryl11x3 = Parameter(name = 'Ryl11x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl11x3}',
                    lhablock = 'YL1',
                    lhacode = [ 1, 3 ])

Ryl12x1 = Parameter(name = 'Ryl12x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl12x1}',
                    lhablock = 'YL1',
                    lhacode = [ 2, 1 ])

Ryl12x2 = Parameter(name = 'Ryl12x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl12x2}',
                    lhablock = 'YL1',
                    lhacode = [ 2, 2 ])

Ryl12x3 = Parameter(name = 'Ryl12x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl12x3}',
                    lhablock = 'YL1',
                    lhacode = [ 2, 3 ])

Ryl13x1 = Parameter(name = 'Ryl13x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl13x1}',
                    lhablock = 'YL1',
                    lhacode = [ 3, 1 ])

Ryl13x2 = Parameter(name = 'Ryl13x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl13x2}',
                    lhablock = 'YL1',
                    lhacode = [ 3, 2 ])

Ryl13x3 = Parameter(name = 'Ryl13x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl13x3}',
                    lhablock = 'YL1',
                    lhacode = [ 3, 3 ])

Ryl21x1 = Parameter(name = 'Ryl21x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl21x1}',
                    lhablock = 'YL2',
                    lhacode = [ 1, 1 ])

Ryl21x2 = Parameter(name = 'Ryl21x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl21x2}',
                    lhablock = 'YL2',
                    lhacode = [ 1, 2 ])

Ryl21x3 = Parameter(name = 'Ryl21x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl21x3}',
                    lhablock = 'YL2',
                    lhacode = [ 1, 3 ])

Ryl22x1 = Parameter(name = 'Ryl22x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl22x1}',
                    lhablock = 'YL2',
                    lhacode = [ 2, 1 ])

Ryl22x2 = Parameter(name = 'Ryl22x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl22x2}',
                    lhablock = 'YL2',
                    lhacode = [ 2, 2 ])

Ryl22x3 = Parameter(name = 'Ryl22x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl22x3}',
                    lhablock = 'YL2',
                    lhacode = [ 2, 3 ])

Ryl23x1 = Parameter(name = 'Ryl23x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl23x1}',
                    lhablock = 'YL2',
                    lhacode = [ 3, 1 ])

Ryl23x2 = Parameter(name = 'Ryl23x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl23x2}',
                    lhablock = 'YL2',
                    lhacode = [ 3, 2 ])

Ryl23x3 = Parameter(name = 'Ryl23x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl23x3}',
                    lhablock = 'YL2',
                    lhacode = [ 3, 3 ])

Ryl31x1 = Parameter(name = 'Ryl31x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl31x1}',
                    lhablock = 'YL3',
                    lhacode = [ 1, 1 ])

Ryl31x2 = Parameter(name = 'Ryl31x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl31x2}',
                    lhablock = 'YL3',
                    lhacode = [ 1, 2 ])

Ryl31x3 = Parameter(name = 'Ryl31x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl31x3}',
                    lhablock = 'YL3',
                    lhacode = [ 1, 3 ])

Ryl32x1 = Parameter(name = 'Ryl32x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl32x1}',
                    lhablock = 'YL3',
                    lhacode = [ 2, 1 ])

Ryl32x2 = Parameter(name = 'Ryl32x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl32x2}',
                    lhablock = 'YL3',
                    lhacode = [ 2, 2 ])

Ryl32x3 = Parameter(name = 'Ryl32x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl32x3}',
                    lhablock = 'YL3',
                    lhacode = [ 2, 3 ])

Ryl33x1 = Parameter(name = 'Ryl33x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl33x1}',
                    lhablock = 'YL3',
                    lhacode = [ 3, 1 ])

Ryl33x2 = Parameter(name = 'Ryl33x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl33x2}',
                    lhablock = 'YL3',
                    lhacode = [ 3, 2 ])

Ryl33x3 = Parameter(name = 'Ryl33x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl33x3}',
                    lhablock = 'YL3',
                    lhacode = [ 3, 3 ])

Ryl41x1 = Parameter(name = 'Ryl41x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl41x1}',
                    lhablock = 'YL4',
                    lhacode = [ 1, 1 ])

Ryl41x2 = Parameter(name = 'Ryl41x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl41x2}',
                    lhablock = 'YL4',
                    lhacode = [ 1, 2 ])

Ryl41x3 = Parameter(name = 'Ryl41x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl41x3}',
                    lhablock = 'YL4',
                    lhacode = [ 1, 3 ])

Ryl42x1 = Parameter(name = 'Ryl42x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl42x1}',
                    lhablock = 'YL4',
                    lhacode = [ 2, 1 ])

Ryl42x2 = Parameter(name = 'Ryl42x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl42x2}',
                    lhablock = 'YL4',
                    lhacode = [ 2, 2 ])

Ryl42x3 = Parameter(name = 'Ryl42x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl42x3}',
                    lhablock = 'YL4',
                    lhacode = [ 2, 3 ])

Ryl43x1 = Parameter(name = 'Ryl43x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl43x1}',
                    lhablock = 'YL4',
                    lhacode = [ 3, 1 ])

Ryl43x2 = Parameter(name = 'Ryl43x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl43x2}',
                    lhablock = 'YL4',
                    lhacode = [ 3, 2 ])

Ryl43x3 = Parameter(name = 'Ryl43x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryl43x3}',
                    lhablock = 'YL4',
                    lhacode = [ 3, 3 ])

Ryq11x1 = Parameter(name = 'Ryq11x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq11x1}',
                    lhablock = 'YQ1',
                    lhacode = [ 1, 1 ])

Ryq11x2 = Parameter(name = 'Ryq11x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq11x2}',
                    lhablock = 'YQ1',
                    lhacode = [ 1, 2 ])

Ryq11x3 = Parameter(name = 'Ryq11x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq11x3}',
                    lhablock = 'YQ1',
                    lhacode = [ 1, 3 ])

Ryq12x1 = Parameter(name = 'Ryq12x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq12x1}',
                    lhablock = 'YQ1',
                    lhacode = [ 2, 1 ])

Ryq12x2 = Parameter(name = 'Ryq12x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq12x2}',
                    lhablock = 'YQ1',
                    lhacode = [ 2, 2 ])

Ryq12x3 = Parameter(name = 'Ryq12x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq12x3}',
                    lhablock = 'YQ1',
                    lhacode = [ 2, 3 ])

Ryq13x1 = Parameter(name = 'Ryq13x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq13x1}',
                    lhablock = 'YQ1',
                    lhacode = [ 3, 1 ])

Ryq13x2 = Parameter(name = 'Ryq13x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq13x2}',
                    lhablock = 'YQ1',
                    lhacode = [ 3, 2 ])

Ryq13x3 = Parameter(name = 'Ryq13x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq13x3}',
                    lhablock = 'YQ1',
                    lhacode = [ 3, 3 ])

Ryq21x1 = Parameter(name = 'Ryq21x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq21x1}',
                    lhablock = 'YQ2',
                    lhacode = [ 1, 1 ])

Ryq21x2 = Parameter(name = 'Ryq21x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq21x2}',
                    lhablock = 'YQ2',
                    lhacode = [ 1, 2 ])

Ryq21x3 = Parameter(name = 'Ryq21x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq21x3}',
                    lhablock = 'YQ2',
                    lhacode = [ 1, 3 ])

Ryq22x1 = Parameter(name = 'Ryq22x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq22x1}',
                    lhablock = 'YQ2',
                    lhacode = [ 2, 1 ])

Ryq22x2 = Parameter(name = 'Ryq22x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq22x2}',
                    lhablock = 'YQ2',
                    lhacode = [ 2, 2 ])

Ryq22x3 = Parameter(name = 'Ryq22x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq22x3}',
                    lhablock = 'YQ2',
                    lhacode = [ 2, 3 ])

Ryq23x1 = Parameter(name = 'Ryq23x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq23x1}',
                    lhablock = 'YQ2',
                    lhacode = [ 3, 1 ])

Ryq23x2 = Parameter(name = 'Ryq23x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq23x2}',
                    lhablock = 'YQ2',
                    lhacode = [ 3, 2 ])

Ryq23x3 = Parameter(name = 'Ryq23x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{Ryq23x3}',
                    lhablock = 'YQ2',
                    lhacode = [ 3, 3 ])

RUVN1x1 = Parameter(name = 'RUVN1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.4875099,
                    texname = '\\text{RUVN1x1}',
                    lhablock = 'VNMix',
                    lhacode = [ 1, 1 ])

RUVN1x2 = Parameter(name = 'RUVN1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.4875099,
                    texname = '\\text{RUVN1x2}',
                    lhablock = 'VNMix',
                    lhacode = [ 1, 2 ])

RUVN1x3 = Parameter(name = 'RUVN1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.7243399,
                    texname = '\\text{RUVN1x3}',
                    lhablock = 'VNMix',
                    lhacode = [ 1, 3 ])

RUVN2x1 = Parameter(name = 'RUVN2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.8730728,
                    texname = '\\text{RUVN2x1}',
                    lhablock = 'VNMix',
                    lhacode = [ 2, 1 ])

RUVN2x2 = Parameter(name = 'RUVN2x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.2637941,
                    texname = '\\text{RUVN2x2}',
                    lhablock = 'VNMix',
                    lhacode = [ 2, 2 ])

RUVN2x3 = Parameter(name = 'RUVN2x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.410069,
                    texname = '\\text{RUVN2x3}',
                    lhablock = 'VNMix',
                    lhacode = [ 2, 3 ])

RUVN3x1 = Parameter(name = 'RUVN3x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.008836105,
                    texname = '\\text{RUVN3x1}',
                    lhablock = 'VNMix',
                    lhacode = [ 3, 1 ])

RUVN3x2 = Parameter(name = 'RUVN3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.8323141,
                    texname = '\\text{RUVN3x2}',
                    lhablock = 'VNMix',
                    lhacode = [ 3, 2 ])

RUVN3x3 = Parameter(name = 'RUVN3x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.5542338,
                    texname = '\\text{RUVN3x3}',
                    lhablock = 'VNMix',
                    lhacode = [ 3, 3 ])

IUVN1x1 = Parameter(name = 'IUVN1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN1x1}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 1, 1 ])

IUVN1x2 = Parameter(name = 'IUVN1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN1x2}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 1, 2 ])

IUVN1x3 = Parameter(name = 'IUVN1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN1x3}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 1, 3 ])

IUVN2x1 = Parameter(name = 'IUVN2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN2x1}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 2, 1 ])

IUVN2x2 = Parameter(name = 'IUVN2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN2x2}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 2, 2 ])

IUVN2x3 = Parameter(name = 'IUVN2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN2x3}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 2, 3 ])

IUVN3x1 = Parameter(name = 'IUVN3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN3x1}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 3, 1 ])

IUVN3x2 = Parameter(name = 'IUVN3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN3x2}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 3, 2 ])

IUVN3x3 = Parameter(name = 'IUVN3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVN3x3}',
                    lhablock = 'IMVNMix',
                    lhacode = [ 3, 3 ])

RUVC1x1 = Parameter(name = 'RUVC1x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUVC1x1}',
                    lhablock = 'VCMix',
                    lhacode = [ 1, 1 ])

RUVC1x2 = Parameter(name = 'RUVC1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUVC1x2}',
                    lhablock = 'VCMix',
                    lhacode = [ 1, 2 ])

RUVC2x1 = Parameter(name = 'RUVC2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUVC2x1}',
                    lhablock = 'VCMix',
                    lhacode = [ 2, 1 ])

RUVC2x2 = Parameter(name = 'RUVC2x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUVC2x2}',
                    lhablock = 'VCMix',
                    lhacode = [ 2, 2 ])

IUVC1x1 = Parameter(name = 'IUVC1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVC1x1}',
                    lhablock = 'IMVCMix',
                    lhacode = [ 1, 1 ])

IUVC1x2 = Parameter(name = 'IUVC1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVC1x2}',
                    lhablock = 'IMVCMix',
                    lhacode = [ 1, 2 ])

IUVC2x1 = Parameter(name = 'IUVC2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVC2x1}',
                    lhablock = 'IMVCMix',
                    lhacode = [ 2, 1 ])

IUVC2x2 = Parameter(name = 'IUVC2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUVC2x2}',
                    lhablock = 'IMVCMix',
                    lhacode = [ 2, 2 ])

RUHD1x1 = Parameter(name = 'RUHD1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHD1x1}',
                    lhablock = 'HDMix',
                    lhacode = [ 1, 1 ])

RUHD1x2 = Parameter(name = 'RUHD1x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHD1x2}',
                    lhablock = 'HDMix',
                    lhacode = [ 1, 2 ])

RUHD2x1 = Parameter(name = 'RUHD2x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHD2x1}',
                    lhablock = 'HDMix',
                    lhacode = [ 2, 1 ])

RUHD2x2 = Parameter(name = 'RUHD2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHD2x2}',
                    lhablock = 'HDMix',
                    lhacode = [ 2, 2 ])

IUHD1x1 = Parameter(name = 'IUHD1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHD1x1}',
                    lhablock = 'IMHDMix',
                    lhacode = [ 1, 1 ])

IUHD1x2 = Parameter(name = 'IUHD1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHD1x2}',
                    lhablock = 'IMHDMix',
                    lhacode = [ 1, 2 ])

IUHD2x1 = Parameter(name = 'IUHD2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHD2x1}',
                    lhablock = 'IMHDMix',
                    lhacode = [ 2, 1 ])

IUHD2x2 = Parameter(name = 'IUHD2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHD2x2}',
                    lhablock = 'IMHDMix',
                    lhacode = [ 2, 2 ])

RUHC1x1 = Parameter(name = 'RUHC1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC1x1}',
                    lhablock = 'HCMix',
                    lhacode = [ 1, 1 ])

RUHC1x2 = Parameter(name = 'RUHC1x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHC1x2}',
                    lhablock = 'HCMix',
                    lhacode = [ 1, 2 ])

RUHC1x3 = Parameter(name = 'RUHC1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC1x3}',
                    lhablock = 'HCMix',
                    lhacode = [ 1, 3 ])

RUHC1x4 = Parameter(name = 'RUHC1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC1x4}',
                    lhablock = 'HCMix',
                    lhacode = [ 1, 4 ])

RUHC2x1 = Parameter(name = 'RUHC2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC2x1}',
                    lhablock = 'HCMix',
                    lhacode = [ 2, 1 ])

RUHC2x2 = Parameter(name = 'RUHC2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC2x2}',
                    lhablock = 'HCMix',
                    lhacode = [ 2, 2 ])

RUHC2x3 = Parameter(name = 'RUHC2x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHC2x3}',
                    lhablock = 'HCMix',
                    lhacode = [ 2, 3 ])

RUHC2x4 = Parameter(name = 'RUHC2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC2x4}',
                    lhablock = 'HCMix',
                    lhacode = [ 2, 4 ])

RUHC3x1 = Parameter(name = 'RUHC3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC3x1}',
                    lhablock = 'HCMix',
                    lhacode = [ 3, 1 ])

RUHC3x2 = Parameter(name = 'RUHC3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC3x2}',
                    lhablock = 'HCMix',
                    lhacode = [ 3, 2 ])

RUHC3x3 = Parameter(name = 'RUHC3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC3x3}',
                    lhablock = 'HCMix',
                    lhacode = [ 3, 3 ])

RUHC3x4 = Parameter(name = 'RUHC3x4',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHC3x4}',
                    lhablock = 'HCMix',
                    lhacode = [ 3, 4 ])

RUHC4x1 = Parameter(name = 'RUHC4x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHC4x1}',
                    lhablock = 'HCMix',
                    lhacode = [ 4, 1 ])

RUHC4x2 = Parameter(name = 'RUHC4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC4x2}',
                    lhablock = 'HCMix',
                    lhacode = [ 4, 2 ])

RUHC4x3 = Parameter(name = 'RUHC4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC4x3}',
                    lhablock = 'HCMix',
                    lhacode = [ 4, 3 ])

RUHC4x4 = Parameter(name = 'RUHC4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHC4x4}',
                    lhablock = 'HCMix',
                    lhacode = [ 4, 4 ])

IUHC1x1 = Parameter(name = 'IUHC1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC1x1}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 1, 1 ])

IUHC1x2 = Parameter(name = 'IUHC1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC1x2}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 1, 2 ])

IUHC1x3 = Parameter(name = 'IUHC1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC1x3}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 1, 3 ])

IUHC1x4 = Parameter(name = 'IUHC1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC1x4}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 1, 4 ])

IUHC2x1 = Parameter(name = 'IUHC2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC2x1}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 2, 1 ])

IUHC2x2 = Parameter(name = 'IUHC2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC2x2}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 2, 2 ])

IUHC2x3 = Parameter(name = 'IUHC2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC2x3}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 2, 3 ])

IUHC2x4 = Parameter(name = 'IUHC2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC2x4}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 2, 4 ])

IUHC3x1 = Parameter(name = 'IUHC3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC3x1}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 3, 1 ])

IUHC3x2 = Parameter(name = 'IUHC3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC3x2}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 3, 2 ])

IUHC3x3 = Parameter(name = 'IUHC3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC3x3}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 3, 3 ])

IUHC3x4 = Parameter(name = 'IUHC3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC3x4}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 3, 4 ])

IUHC4x1 = Parameter(name = 'IUHC4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC4x1}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 4, 1 ])

IUHC4x2 = Parameter(name = 'IUHC4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC4x2}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 4, 2 ])

IUHC4x3 = Parameter(name = 'IUHC4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC4x3}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 4, 3 ])

IUHC4x4 = Parameter(name = 'IUHC4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHC4x4}',
                    lhablock = 'IMHCMix',
                    lhacode = [ 4, 4 ])

RUHN1x1 = Parameter(name = 'RUHN1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN1x1}',
                    lhablock = 'HMix',
                    lhacode = [ 1, 1 ])

RUHN1x2 = Parameter(name = 'RUHN1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.177868,
                    texname = '\\text{RUHN1x2}',
                    lhablock = 'HMix',
                    lhacode = [ 1, 2 ])

RUHN1x3 = Parameter(name = 'RUHN1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.6958315,
                    texname = '\\text{RUHN1x3}',
                    lhablock = 'HMix',
                    lhacode = [ 1, 3 ])

RUHN1x4 = Parameter(name = 'RUHN1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN1x4}',
                    lhablock = 'HMix',
                    lhacode = [ 1, 4 ])

RUHN2x1 = Parameter(name = 'RUHN2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN2x1}',
                    lhablock = 'HMix',
                    lhacode = [ 2, 1 ])

RUHN2x2 = Parameter(name = 'RUHN2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN2x2}',
                    lhablock = 'HMix',
                    lhacode = [ 2, 2 ])

RUHN2x3 = Parameter(name = 'RUHN2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN2x3}',
                    lhablock = 'HMix',
                    lhacode = [ 2, 3 ])

RUHN2x4 = Parameter(name = 'RUHN2x4',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHN2x4}',
                    lhablock = 'HMix',
                    lhacode = [ 2, 4 ])

RUHN3x1 = Parameter(name = 'RUHN3x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUHN3x1}',
                    lhablock = 'HMix',
                    lhacode = [ 3, 1 ])

RUHN3x2 = Parameter(name = 'RUHN3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN3x2}',
                    lhablock = 'HMix',
                    lhacode = [ 3, 2 ])

RUHN3x3 = Parameter(name = 'RUHN3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN3x3}',
                    lhablock = 'HMix',
                    lhacode = [ 3, 3 ])

RUHN3x4 = Parameter(name = 'RUHN3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN3x4}',
                    lhablock = 'HMix',
                    lhacode = [ 3, 4 ])

RUHN4x1 = Parameter(name = 'RUHN4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN4x1}',
                    lhablock = 'HMix',
                    lhacode = [ 4, 1 ])

RUHN4x2 = Parameter(name = 'RUHN4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.9840544,
                    texname = '\\text{RUHN4x2}',
                    lhablock = 'HMix',
                    lhacode = [ 4, 2 ])

RUHN4x3 = Parameter(name = 'RUHN4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.1257716,
                    texname = '\\text{RUHN4x3}',
                    lhablock = 'HMix',
                    lhacode = [ 4, 3 ])

RUHN4x4 = Parameter(name = 'RUHN4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUHN4x4}',
                    lhablock = 'HMix',
                    lhacode = [ 4, 4 ])

IUHN1x1 = Parameter(name = 'IUHN1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN1x1}',
                    lhablock = 'IMHMix',
                    lhacode = [ 1, 1 ])

IUHN1x2 = Parameter(name = 'IUHN1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN1x2}',
                    lhablock = 'IMHMix',
                    lhacode = [ 1, 2 ])

IUHN1x3 = Parameter(name = 'IUHN1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.6958315,
                    texname = '\\text{IUHN1x3}',
                    lhablock = 'IMHMix',
                    lhacode = [ 1, 3 ])

IUHN1x4 = Parameter(name = 'IUHN1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN1x4}',
                    lhablock = 'IMHMix',
                    lhacode = [ 1, 4 ])

IUHN2x1 = Parameter(name = 'IUHN2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN2x1}',
                    lhablock = 'IMHMix',
                    lhacode = [ 2, 1 ])

IUHN2x2 = Parameter(name = 'IUHN2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN2x2}',
                    lhablock = 'IMHMix',
                    lhacode = [ 2, 2 ])

IUHN2x3 = Parameter(name = 'IUHN2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN2x3}',
                    lhablock = 'IMHMix',
                    lhacode = [ 2, 3 ])

IUHN2x4 = Parameter(name = 'IUHN2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN2x4}',
                    lhablock = 'IMHMix',
                    lhacode = [ 2, 4 ])

IUHN3x1 = Parameter(name = 'IUHN3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN3x1}',
                    lhablock = 'IMHMix',
                    lhacode = [ 3, 1 ])

IUHN3x2 = Parameter(name = 'IUHN3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN3x2}',
                    lhablock = 'IMHMix',
                    lhacode = [ 3, 2 ])

IUHN3x3 = Parameter(name = 'IUHN3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN3x3}',
                    lhablock = 'IMHMix',
                    lhacode = [ 3, 3 ])

IUHN3x4 = Parameter(name = 'IUHN3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN3x4}',
                    lhablock = 'IMHMix',
                    lhacode = [ 3, 4 ])

IUHN4x1 = Parameter(name = 'IUHN4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN4x1}',
                    lhablock = 'IMHMix',
                    lhacode = [ 4, 1 ])

IUHN4x2 = Parameter(name = 'IUHN4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN4x2}',
                    lhablock = 'IMHMix',
                    lhacode = [ 4, 2 ])

IUHN4x3 = Parameter(name = 'IUHN4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.1257716,
                    texname = '\\text{IUHN4x3}',
                    lhablock = 'IMHMix',
                    lhacode = [ 4, 3 ])

IUHN4x4 = Parameter(name = 'IUHN4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUHN4x4}',
                    lhablock = 'IMHMix',
                    lhacode = [ 4, 4 ])

RUAN1x1 = Parameter(name = 'RUAN1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN1x1}',
                    lhablock = 'AMix',
                    lhacode = [ 1, 1 ])

RUAN1x2 = Parameter(name = 'RUAN1x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUAN1x2}',
                    lhablock = 'AMix',
                    lhacode = [ 1, 2 ])

RUAN1x3 = Parameter(name = 'RUAN1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN1x3}',
                    lhablock = 'AMix',
                    lhacode = [ 1, 3 ])

RUAN1x4 = Parameter(name = 'RUAN1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN1x4}',
                    lhablock = 'AMix',
                    lhacode = [ 1, 4 ])

RUAN2x1 = Parameter(name = 'RUAN2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN2x1}',
                    lhablock = 'AMix',
                    lhacode = [ 2, 1 ])

RUAN2x2 = Parameter(name = 'RUAN2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN2x2}',
                    lhablock = 'AMix',
                    lhacode = [ 2, 2 ])

RUAN2x3 = Parameter(name = 'RUAN2x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUAN2x3}',
                    lhablock = 'AMix',
                    lhacode = [ 2, 3 ])

RUAN2x4 = Parameter(name = 'RUAN2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN2x4}',
                    lhablock = 'AMix',
                    lhacode = [ 2, 4 ])

RUAN3x1 = Parameter(name = 'RUAN3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN3x1}',
                    lhablock = 'AMix',
                    lhacode = [ 3, 1 ])

RUAN3x2 = Parameter(name = 'RUAN3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN3x2}',
                    lhablock = 'AMix',
                    lhacode = [ 3, 2 ])

RUAN3x3 = Parameter(name = 'RUAN3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN3x3}',
                    lhablock = 'AMix',
                    lhacode = [ 3, 3 ])

RUAN3x4 = Parameter(name = 'RUAN3x4',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUAN3x4}',
                    lhablock = 'AMix',
                    lhacode = [ 3, 4 ])

RUAN4x1 = Parameter(name = 'RUAN4x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RUAN4x1}',
                    lhablock = 'AMix',
                    lhacode = [ 4, 1 ])

RUAN4x2 = Parameter(name = 'RUAN4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN4x2}',
                    lhablock = 'AMix',
                    lhacode = [ 4, 2 ])

RUAN4x3 = Parameter(name = 'RUAN4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN4x3}',
                    lhablock = 'AMix',
                    lhacode = [ 4, 3 ])

RUAN4x4 = Parameter(name = 'RUAN4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUAN4x4}',
                    lhablock = 'AMix',
                    lhacode = [ 4, 4 ])

IUAN1x1 = Parameter(name = 'IUAN1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN1x1}',
                    lhablock = 'IMAMix',
                    lhacode = [ 1, 1 ])

IUAN1x2 = Parameter(name = 'IUAN1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN1x2}',
                    lhablock = 'IMAMix',
                    lhacode = [ 1, 2 ])

IUAN1x3 = Parameter(name = 'IUAN1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN1x3}',
                    lhablock = 'IMAMix',
                    lhacode = [ 1, 3 ])

IUAN1x4 = Parameter(name = 'IUAN1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN1x4}',
                    lhablock = 'IMAMix',
                    lhacode = [ 1, 4 ])

IUAN2x1 = Parameter(name = 'IUAN2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN2x1}',
                    lhablock = 'IMAMix',
                    lhacode = [ 2, 1 ])

IUAN2x2 = Parameter(name = 'IUAN2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN2x2}',
                    lhablock = 'IMAMix',
                    lhacode = [ 2, 2 ])

IUAN2x3 = Parameter(name = 'IUAN2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN2x3}',
                    lhablock = 'IMAMix',
                    lhacode = [ 2, 3 ])

IUAN2x4 = Parameter(name = 'IUAN2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN2x4}',
                    lhablock = 'IMAMix',
                    lhacode = [ 2, 4 ])

IUAN3x1 = Parameter(name = 'IUAN3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN3x1}',
                    lhablock = 'IMAMix',
                    lhacode = [ 3, 1 ])

IUAN3x2 = Parameter(name = 'IUAN3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN3x2}',
                    lhablock = 'IMAMix',
                    lhacode = [ 3, 2 ])

IUAN3x3 = Parameter(name = 'IUAN3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN3x3}',
                    lhablock = 'IMAMix',
                    lhacode = [ 3, 3 ])

IUAN3x4 = Parameter(name = 'IUAN3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN3x4}',
                    lhablock = 'IMAMix',
                    lhacode = [ 3, 4 ])

IUAN4x1 = Parameter(name = 'IUAN4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN4x1}',
                    lhablock = 'IMAMix',
                    lhacode = [ 4, 1 ])

IUAN4x2 = Parameter(name = 'IUAN4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN4x2}',
                    lhablock = 'IMAMix',
                    lhacode = [ 4, 2 ])

IUAN4x3 = Parameter(name = 'IUAN4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN4x3}',
                    lhablock = 'IMAMix',
                    lhacode = [ 4, 3 ])

IUAN4x4 = Parameter(name = 'IUAN4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUAN4x4}',
                    lhablock = 'IMAMix',
                    lhacode = [ 4, 4 ])

RCKML1x1 = Parameter(name = 'RCKML1x1',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{RCKML1x1}',
                     lhablock = 'VCKML',
                     lhacode = [ 1, 1 ])

RCKML1x2 = Parameter(name = 'RCKML1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKML1x2}',
                     lhablock = 'VCKML',
                     lhacode = [ 1, 2 ])

RCKML1x3 = Parameter(name = 'RCKML1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKML1x3}',
                     lhablock = 'VCKML',
                     lhacode = [ 1, 3 ])

RCKML2x1 = Parameter(name = 'RCKML2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKML2x1}',
                     lhablock = 'VCKML',
                     lhacode = [ 2, 1 ])

RCKML2x2 = Parameter(name = 'RCKML2x2',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{RCKML2x2}',
                     lhablock = 'VCKML',
                     lhacode = [ 2, 2 ])

RCKML2x3 = Parameter(name = 'RCKML2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKML2x3}',
                     lhablock = 'VCKML',
                     lhacode = [ 2, 3 ])

RCKML3x1 = Parameter(name = 'RCKML3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKML3x1}',
                     lhablock = 'VCKML',
                     lhacode = [ 3, 1 ])

RCKML3x2 = Parameter(name = 'RCKML3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKML3x2}',
                     lhablock = 'VCKML',
                     lhacode = [ 3, 2 ])

RCKML3x3 = Parameter(name = 'RCKML3x3',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{RCKML3x3}',
                     lhablock = 'VCKML',
                     lhacode = [ 3, 3 ])

ICKML1x1 = Parameter(name = 'ICKML1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML1x1}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 1, 1 ])

ICKML1x2 = Parameter(name = 'ICKML1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML1x2}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 1, 2 ])

ICKML1x3 = Parameter(name = 'ICKML1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML1x3}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 1, 3 ])

ICKML2x1 = Parameter(name = 'ICKML2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML2x1}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 2, 1 ])

ICKML2x2 = Parameter(name = 'ICKML2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML2x2}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 2, 2 ])

ICKML2x3 = Parameter(name = 'ICKML2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML2x3}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 2, 3 ])

ICKML3x1 = Parameter(name = 'ICKML3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML3x1}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 3, 1 ])

ICKML3x2 = Parameter(name = 'ICKML3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML3x2}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 3, 2 ])

ICKML3x3 = Parameter(name = 'ICKML3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKML3x3}',
                     lhablock = 'IMVCKML',
                     lhacode = [ 3, 3 ])

RCKMR1x1 = Parameter(name = 'RCKMR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{RCKMR1x1}',
                     lhablock = 'VCKMR',
                     lhacode = [ 1, 1 ])

RCKMR1x2 = Parameter(name = 'RCKMR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKMR1x2}',
                     lhablock = 'VCKMR',
                     lhacode = [ 1, 2 ])

RCKMR1x3 = Parameter(name = 'RCKMR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKMR1x3}',
                     lhablock = 'VCKMR',
                     lhacode = [ 1, 3 ])

RCKMR2x1 = Parameter(name = 'RCKMR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKMR2x1}',
                     lhablock = 'VCKMR',
                     lhacode = [ 2, 1 ])

RCKMR2x2 = Parameter(name = 'RCKMR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{RCKMR2x2}',
                     lhablock = 'VCKMR',
                     lhacode = [ 2, 2 ])

RCKMR2x3 = Parameter(name = 'RCKMR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKMR2x3}',
                     lhablock = 'VCKMR',
                     lhacode = [ 2, 3 ])

RCKMR3x1 = Parameter(name = 'RCKMR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKMR3x1}',
                     lhablock = 'VCKMR',
                     lhacode = [ 3, 1 ])

RCKMR3x2 = Parameter(name = 'RCKMR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{RCKMR3x2}',
                     lhablock = 'VCKMR',
                     lhacode = [ 3, 2 ])

RCKMR3x3 = Parameter(name = 'RCKMR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{RCKMR3x3}',
                     lhablock = 'VCKMR',
                     lhacode = [ 3, 3 ])

ICKMR1x1 = Parameter(name = 'ICKMR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR1x1}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 1, 1 ])

ICKMR1x2 = Parameter(name = 'ICKMR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR1x2}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 1, 2 ])

ICKMR1x3 = Parameter(name = 'ICKMR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR1x3}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 1, 3 ])

ICKMR2x1 = Parameter(name = 'ICKMR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR2x1}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 2, 1 ])

ICKMR2x2 = Parameter(name = 'ICKMR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR2x2}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 2, 2 ])

ICKMR2x3 = Parameter(name = 'ICKMR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR2x3}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 2, 3 ])

ICKMR3x1 = Parameter(name = 'ICKMR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR3x1}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 3, 1 ])

ICKMR3x2 = Parameter(name = 'ICKMR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR3x2}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 3, 2 ])

ICKMR3x3 = Parameter(name = 'ICKMR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{ICKMR3x3}',
                     lhablock = 'IMVCKMR',
                     lhacode = [ 3, 3 ])

RPMNSL1x1 = Parameter(name = 'RPMNSL1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL1x1}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 1, 1 ])

RPMNSL1x2 = Parameter(name = 'RPMNSL1x2',
                      nature = 'external',
                      type = 'real',
                      value = 9.495194e-17,
                      texname = '\\text{RPMNSL1x2}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 1, 2 ])

RPMNSL1x3 = Parameter(name = 'RPMNSL1x3',
                      nature = 'external',
                      type = 'real',
                      value = 5.139946e-17,
                      texname = '\\text{RPMNSL1x3}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 1, 3 ])

RPMNSL1x4 = Parameter(name = 'RPMNSL1x4',
                      nature = 'external',
                      type = 'real',
                      value = -1.821179e-18,
                      texname = '\\text{RPMNSL1x4}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 1, 4 ])

RPMNSL1x5 = Parameter(name = 'RPMNSL1x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.6777363,
                      texname = '\\text{RPMNSL1x5}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 1, 5 ])

RPMNSL1x6 = Parameter(name = 'RPMNSL1x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.6777363,
                      texname = '\\text{RPMNSL1x6}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 1, 6 ])

RPMNSL2x1 = Parameter(name = 'RPMNSL2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL2x1}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 2, 1 ])

RPMNSL2x2 = Parameter(name = 'RPMNSL2x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.002988977,
                      texname = '\\text{RPMNSL2x2}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 2, 2 ])

RPMNSL2x3 = Parameter(name = 'RPMNSL2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.9852307,
                      texname = '\\text{RPMNSL2x3}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 2, 3 ])

RPMNSL2x4 = Parameter(name = 'RPMNSL2x4',
                      nature = 'external',
                      type = 'real',
                      value = 1.899878e-17,
                      texname = '\\text{RPMNSL2x4}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 2, 4 ])

RPMNSL2x5 = Parameter(name = 'RPMNSL2x5',
                      nature = 'external',
                      type = 'real',
                      value = -4.18951e-17,
                      texname = '\\text{RPMNSL2x5}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 2, 5 ])

RPMNSL2x6 = Parameter(name = 'RPMNSL2x6',
                      nature = 'external',
                      type = 'real',
                      value = 1.223279e-17,
                      texname = '\\text{RPMNSL2x6}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 2, 6 ])

RPMNSL3x1 = Parameter(name = 'RPMNSL3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.9902962,
                      texname = '\\text{RPMNSL3x1}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 3, 1 ])

RPMNSL3x2 = Parameter(name = 'RPMNSL3x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.01950273,
                      texname = '\\text{RPMNSL3x2}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 3, 2 ])

RPMNSL3x3 = Parameter(name = 'RPMNSL3x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.01950273,
                      texname = '\\text{RPMNSL3x3}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 3, 3 ])

RPMNSL3x4 = Parameter(name = 'RPMNSL3x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL3x4}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 3, 4 ])

RPMNSL3x5 = Parameter(name = 'RPMNSL3x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL3x5}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 3, 5 ])

RPMNSL3x6 = Parameter(name = 'RPMNSL3x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL3x6}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 3, 6 ])

RPMNSL4x1 = Parameter(name = 'RPMNSL4x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL4x1}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 4, 1 ])

RPMNSL4x2 = Parameter(name = 'RPMNSL4x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.5658658,
                      texname = '\\text{RPMNSL4x2}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 4, 2 ])

RPMNSL4x3 = Parameter(name = 'RPMNSL4x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.06963799,
                      texname = '\\text{RPMNSL4x3}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 4, 3 ])

RPMNSL4x4 = Parameter(name = 'RPMNSL4x4',
                      nature = 'external',
                      type = 'real',
                      value = 1.622284e-18,
                      texname = '\\text{RPMNSL4x4}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 4, 4 ])

RPMNSL4x5 = Parameter(name = 'RPMNSL4x5',
                      nature = 'external',
                      type = 'real',
                      value = -3.577375e-18,
                      texname = '\\text{RPMNSL4x5}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 4, 5 ])

RPMNSL4x6 = Parameter(name = 'RPMNSL4x6',
                      nature = 'external',
                      type = 'real',
                      value = 1.044544e-18,
                      texname = '\\text{RPMNSL4x6}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 4, 6 ])

RPMNSL5x1 = Parameter(name = 'RPMNSL5x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL5x1}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 5, 1 ])

RPMNSL5x2 = Parameter(name = 'RPMNSL5x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.8124612,
                      texname = '\\text{RPMNSL5x2}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 5, 2 ])

RPMNSL5x3 = Parameter(name = 'RPMNSL5x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.06911685,
                      texname = '\\text{RPMNSL5x3}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 5, 3 ])

RPMNSL5x4 = Parameter(name = 'RPMNSL5x4',
                      nature = 'external',
                      type = 'real',
                      value = -3.39848e-17,
                      texname = '\\text{RPMNSL5x4}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 5, 4 ])

RPMNSL5x5 = Parameter(name = 'RPMNSL5x5',
                      nature = 'external',
                      type = 'real',
                      value = 7.494147e-17,
                      texname = '\\text{RPMNSL5x5}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 5, 5 ])

RPMNSL5x6 = Parameter(name = 'RPMNSL5x6',
                      nature = 'external',
                      type = 'real',
                      value = -2.188188e-17,
                      texname = '\\text{RPMNSL5x6}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 5, 6 ])

RPMNSL6x1 = Parameter(name = 'RPMNSL6x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.1389729,
                      texname = '\\text{RPMNSL6x1}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 6, 1 ])

RPMNSL6x2 = Parameter(name = 'RPMNSL6x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.1389729,
                      texname = '\\text{RPMNSL6x2}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 6, 2 ])

RPMNSL6x3 = Parameter(name = 'RPMNSL6x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.1389729,
                      texname = '\\text{RPMNSL6x3}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 6, 3 ])

RPMNSL6x4 = Parameter(name = 'RPMNSL6x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL6x4}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 6, 4 ])

RPMNSL6x5 = Parameter(name = 'RPMNSL6x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL6x5}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 6, 5 ])

RPMNSL6x6 = Parameter(name = 'RPMNSL6x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSL6x6}',
                      lhablock = 'PMNSMIX',
                      lhacode = [ 6, 6 ])

IPMNSL1x1 = Parameter(name = 'IPMNSL1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL1x1}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 1, 1 ])

IPMNSL1x2 = Parameter(name = 'IPMNSL1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL1x2}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 1, 2 ])

IPMNSL1x3 = Parameter(name = 'IPMNSL1x3',
                      nature = 'external',
                      type = 'real',
                      value = -1.456943e-17,
                      texname = '\\text{IPMNSL1x3}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 1, 3 ])

IPMNSL1x4 = Parameter(name = 'IPMNSL1x4',
                      nature = 'external',
                      type = 'real',
                      value = 4.215351e-17,
                      texname = '\\text{IPMNSL1x4}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 1, 4 ])

IPMNSL1x5 = Parameter(name = 'IPMNSL1x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.2016766,
                      texname = '\\text{IPMNSL1x5}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 1, 5 ])

IPMNSL1x6 = Parameter(name = 'IPMNSL1x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.2016766,
                      texname = '\\text{IPMNSL1x6}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 1, 6 ])

IPMNSL2x1 = Parameter(name = 'IPMNSL2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL2x1}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 2, 1 ])

IPMNSL2x2 = Parameter(name = 'IPMNSL2x2',
                      nature = 'external',
                      type = 'real',
                      value = -3.82864e-17,
                      texname = '\\text{IPMNSL2x2}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 2, 2 ])

IPMNSL2x3 = Parameter(name = 'IPMNSL2x3',
                      nature = 'external',
                      type = 'real',
                      value = -4.711697e-18,
                      texname = '\\text{IPMNSL2x3}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 2, 3 ])

IPMNSL2x4 = Parameter(name = 'IPMNSL2x4',
                      nature = 'external',
                      type = 'real',
                      value = -0.001483214,
                      texname = '\\text{IPMNSL2x4}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 2, 4 ])

IPMNSL2x5 = Parameter(name = 'IPMNSL2x5',
                      nature = 'external',
                      type = 'real',
                      value = -0.1210564,
                      texname = '\\text{IPMNSL2x5}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 2, 5 ])

IPMNSL2x6 = Parameter(name = 'IPMNSL2x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.1210564,
                      texname = '\\text{IPMNSL2x6}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 2, 6 ])

IPMNSL3x1 = Parameter(name = 'IPMNSL3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL3x1}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 3, 1 ])

IPMNSL3x2 = Parameter(name = 'IPMNSL3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL3x2}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 3, 2 ])

IPMNSL3x3 = Parameter(name = 'IPMNSL3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL3x3}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 3, 3 ])

IPMNSL3x4 = Parameter(name = 'IPMNSL3x4',
                      nature = 'external',
                      type = 'real',
                      value = -0.07864003,
                      texname = '\\text{IPMNSL3x4}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 3, 4 ])

IPMNSL3x5 = Parameter(name = 'IPMNSL3x5',
                      nature = 'external',
                      type = 'real',
                      value = -0.07864003,
                      texname = '\\text{IPMNSL3x5}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 3, 5 ])

IPMNSL3x6 = Parameter(name = 'IPMNSL3x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.07864003,
                      texname = '\\text{IPMNSL3x6}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 3, 6 ])

IPMNSL4x1 = Parameter(name = 'IPMNSL4x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL4x1}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 4, 1 ])

IPMNSL4x2 = Parameter(name = 'IPMNSL4x2',
                      nature = 'external',
                      type = 'real',
                      value = -3.269232e-18,
                      texname = '\\text{IPMNSL4x2}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 4, 2 ])

IPMNSL4x3 = Parameter(name = 'IPMNSL4x3',
                      nature = 'external',
                      type = 'real',
                      value = -4.023264e-19,
                      texname = '\\text{IPMNSL4x3}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 4, 3 ])

IPMNSL4x4 = Parameter(name = 'IPMNSL4x4',
                      nature = 'external',
                      type = 'real',
                      value = -0.7192016,
                      texname = '\\text{IPMNSL4x4}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 4, 4 ])

IPMNSL4x5 = Parameter(name = 'IPMNSL4x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.2807984,
                      texname = '\\text{IPMNSL4x5}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 4, 5 ])

IPMNSL4x6 = Parameter(name = 'IPMNSL4x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.2807984,
                      texname = '\\text{IPMNSL4x6}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 4, 6 ])

IPMNSL5x1 = Parameter(name = 'IPMNSL5x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL5x1}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 5, 1 ])

IPMNSL5x2 = Parameter(name = 'IPMNSL5x2',
                      nature = 'external',
                      type = 'real',
                      value = 6.848628e-17,
                      texname = '\\text{IPMNSL5x2}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 5, 2 ])

IPMNSL5x3 = Parameter(name = 'IPMNSL5x3',
                      nature = 'external',
                      type = 'real',
                      value = 8.428229e-18,
                      texname = '\\text{IPMNSL5x3}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 5, 3 ])

IPMNSL5x4 = Parameter(name = 'IPMNSL5x4',
                      nature = 'external',
                      type = 'real',
                      value = -0.4031658,
                      texname = '\\text{IPMNSL5x4}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 5, 4 ])

IPMNSL5x5 = Parameter(name = 'IPMNSL5x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.2937576,
                      texname = '\\text{IPMNSL5x5}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 5, 5 ])

IPMNSL5x6 = Parameter(name = 'IPMNSL5x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.2937576,
                      texname = '\\text{IPMNSL5x6}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 5, 6 ])

IPMNSL6x1 = Parameter(name = 'IPMNSL6x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL6x1}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 6, 1 ])

IPMNSL6x2 = Parameter(name = 'IPMNSL6x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL6x2}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 6, 2 ])

IPMNSL6x3 = Parameter(name = 'IPMNSL6x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSL6x3}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 6, 3 ])

IPMNSL6x4 = Parameter(name = 'IPMNSL6x4',
                      nature = 'external',
                      type = 'real',
                      value = -0.5603747,
                      texname = '\\text{IPMNSL6x4}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 6, 4 ])

IPMNSL6x5 = Parameter(name = 'IPMNSL6x5',
                      nature = 'external',
                      type = 'real',
                      value = -0.5603747,
                      texname = '\\text{IPMNSL6x5}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 6, 5 ])

IPMNSL6x6 = Parameter(name = 'IPMNSL6x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.5603747,
                      texname = '\\text{IPMNSL6x6}',
                      lhablock = 'IMPMNSMIX',
                      lhacode = [ 6, 6 ])

RPMNSR1x1 = Parameter(name = 'RPMNSR1x1',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = '\\text{RPMNSR1x1}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 1, 1 ])

RPMNSR1x2 = Parameter(name = 'RPMNSR1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR1x2}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 1, 2 ])

RPMNSR1x3 = Parameter(name = 'RPMNSR1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR1x3}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 1, 3 ])

RPMNSR1x4 = Parameter(name = 'RPMNSR1x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR1x4}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 1, 4 ])

RPMNSR1x5 = Parameter(name = 'RPMNSR1x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR1x5}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 1, 5 ])

RPMNSR1x6 = Parameter(name = 'RPMNSR1x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR1x6}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 1, 6 ])

RPMNSR2x1 = Parameter(name = 'RPMNSR2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR2x1}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 2, 1 ])

RPMNSR2x2 = Parameter(name = 'RPMNSR2x2',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = '\\text{RPMNSR2x2}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 2, 2 ])

RPMNSR2x3 = Parameter(name = 'RPMNSR2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR2x3}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 2, 3 ])

RPMNSR2x4 = Parameter(name = 'RPMNSR2x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR2x4}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 2, 4 ])

RPMNSR2x5 = Parameter(name = 'RPMNSR2x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR2x5}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 2, 5 ])

RPMNSR2x6 = Parameter(name = 'RPMNSR2x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR2x6}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 2, 6 ])

RPMNSR3x1 = Parameter(name = 'RPMNSR3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR3x1}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 3, 1 ])

RPMNSR3x2 = Parameter(name = 'RPMNSR3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR3x2}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 3, 2 ])

RPMNSR3x3 = Parameter(name = 'RPMNSR3x3',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = '\\text{RPMNSR3x3}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 3, 3 ])

RPMNSR3x4 = Parameter(name = 'RPMNSR3x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR3x4}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 3, 4 ])

RPMNSR3x5 = Parameter(name = 'RPMNSR3x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR3x5}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 3, 5 ])

RPMNSR3x6 = Parameter(name = 'RPMNSR3x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR3x6}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 3, 6 ])

RPMNSR4x1 = Parameter(name = 'RPMNSR4x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR4x1}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 4, 1 ])

RPMNSR4x2 = Parameter(name = 'RPMNSR4x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR4x2}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 4, 2 ])

RPMNSR4x3 = Parameter(name = 'RPMNSR4x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR4x3}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 4, 3 ])

RPMNSR4x4 = Parameter(name = 'RPMNSR4x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.8164966,
                      texname = '\\text{RPMNSR4x4}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 4, 4 ])

RPMNSR4x5 = Parameter(name = 'RPMNSR4x5',
                      nature = 'external',
                      type = 'real',
                      value = -0.4082483,
                      texname = '\\text{RPMNSR4x5}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 4, 5 ])

RPMNSR4x6 = Parameter(name = 'RPMNSR4x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.4082483,
                      texname = '\\text{RPMNSR4x6}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 4, 6 ])

RPMNSR5x1 = Parameter(name = 'RPMNSR5x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR5x1}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 5, 1 ])

RPMNSR5x2 = Parameter(name = 'RPMNSR5x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR5x2}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 5, 2 ])

RPMNSR5x3 = Parameter(name = 'RPMNSR5x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR5x3}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 5, 3 ])

RPMNSR5x4 = Parameter(name = 'RPMNSR5x4',
                      nature = 'external',
                      type = 'real',
                      value = -0.5773503,
                      texname = '\\text{RPMNSR5x4}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 5, 4 ])

RPMNSR5x5 = Parameter(name = 'RPMNSR5x5',
                      nature = 'external',
                      type = 'real',
                      value = -0.5773503,
                      texname = '\\text{RPMNSR5x5}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 5, 5 ])

RPMNSR5x6 = Parameter(name = 'RPMNSR5x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.5773503,
                      texname = '\\text{RPMNSR5x6}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 5, 6 ])

RPMNSR6x1 = Parameter(name = 'RPMNSR6x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR6x1}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 6, 1 ])

RPMNSR6x2 = Parameter(name = 'RPMNSR6x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR6x2}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 6, 2 ])

RPMNSR6x3 = Parameter(name = 'RPMNSR6x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR6x3}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 6, 3 ])

RPMNSR6x4 = Parameter(name = 'RPMNSR6x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{RPMNSR6x4}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 6, 4 ])

RPMNSR6x5 = Parameter(name = 'RPMNSR6x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.7071068,
                      texname = '\\text{RPMNSR6x5}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 6, 5 ])

RPMNSR6x6 = Parameter(name = 'RPMNSR6x6',
                      nature = 'external',
                      type = 'real',
                      value = -0.7071068,
                      texname = '\\text{RPMNSR6x6}',
                      lhablock = 'PMNSRMIX',
                      lhacode = [ 6, 6 ])

IPMNSR1x1 = Parameter(name = 'IPMNSR1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR1x1}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 1, 1 ])

IPMNSR1x2 = Parameter(name = 'IPMNSR1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR1x2}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 1, 2 ])

IPMNSR1x3 = Parameter(name = 'IPMNSR1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR1x3}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 1, 3 ])

IPMNSR1x4 = Parameter(name = 'IPMNSR1x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR1x4}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 1, 4 ])

IPMNSR1x5 = Parameter(name = 'IPMNSR1x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR1x5}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 1, 5 ])

IPMNSR1x6 = Parameter(name = 'IPMNSR1x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR1x6}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 1, 6 ])

IPMNSR2x1 = Parameter(name = 'IPMNSR2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR2x1}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 2, 1 ])

IPMNSR2x2 = Parameter(name = 'IPMNSR2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR2x2}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 2, 2 ])

IPMNSR2x3 = Parameter(name = 'IPMNSR2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR2x3}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 2, 3 ])

IPMNSR2x4 = Parameter(name = 'IPMNSR2x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR2x4}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 2, 4 ])

IPMNSR2x5 = Parameter(name = 'IPMNSR2x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR2x5}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 2, 5 ])

IPMNSR2x6 = Parameter(name = 'IPMNSR2x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR2x6}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 2, 6 ])

IPMNSR3x1 = Parameter(name = 'IPMNSR3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR3x1}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 3, 1 ])

IPMNSR3x2 = Parameter(name = 'IPMNSR3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR3x2}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 3, 2 ])

IPMNSR3x3 = Parameter(name = 'IPMNSR3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR3x3}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 3, 3 ])

IPMNSR3x4 = Parameter(name = 'IPMNSR3x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR3x4}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 3, 4 ])

IPMNSR3x5 = Parameter(name = 'IPMNSR3x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR3x5}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 3, 5 ])

IPMNSR3x6 = Parameter(name = 'IPMNSR3x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR3x6}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 3, 6 ])

IPMNSR4x1 = Parameter(name = 'IPMNSR4x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR4x1}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 4, 1 ])

IPMNSR4x2 = Parameter(name = 'IPMNSR4x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR4x2}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 4, 2 ])

IPMNSR4x3 = Parameter(name = 'IPMNSR4x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR4x3}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 4, 3 ])

IPMNSR4x4 = Parameter(name = 'IPMNSR4x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR4x4}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 4, 4 ])

IPMNSR4x5 = Parameter(name = 'IPMNSR4x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR4x5}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 4, 5 ])

IPMNSR4x6 = Parameter(name = 'IPMNSR4x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR4x6}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 4, 6 ])

IPMNSR5x1 = Parameter(name = 'IPMNSR5x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR5x1}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 5, 1 ])

IPMNSR5x2 = Parameter(name = 'IPMNSR5x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR5x2}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 5, 2 ])

IPMNSR5x3 = Parameter(name = 'IPMNSR5x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR5x3}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 5, 3 ])

IPMNSR5x4 = Parameter(name = 'IPMNSR5x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR5x4}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 5, 4 ])

IPMNSR5x5 = Parameter(name = 'IPMNSR5x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR5x5}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 5, 5 ])

IPMNSR5x6 = Parameter(name = 'IPMNSR5x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR5x6}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 5, 6 ])

IPMNSR6x1 = Parameter(name = 'IPMNSR6x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR6x1}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 6, 1 ])

IPMNSR6x2 = Parameter(name = 'IPMNSR6x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR6x2}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 6, 2 ])

IPMNSR6x3 = Parameter(name = 'IPMNSR6x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR6x3}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 6, 3 ])

IPMNSR6x4 = Parameter(name = 'IPMNSR6x4',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR6x4}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 6, 4 ])

IPMNSR6x5 = Parameter(name = 'IPMNSR6x5',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR6x5}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 6, 5 ])

IPMNSR6x6 = Parameter(name = 'IPMNSR6x6',
                      nature = 'external',
                      type = 'real',
                      value = 0.,
                      texname = '\\text{IPMNSR6x6}',
                      lhablock = 'IMPMNSRMIX',
                      lhacode = [ 6, 6 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.47614,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MZp = Parameter(name = 'MZp',
                nature = 'external',
                type = 'real',
                value = 782.1402,
                texname = '\\text{MZp}',
                lhablock = 'MASS',
                lhacode = [ 32 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.16379,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

MWp = Parameter(name = 'MWp',
                nature = 'external',
                type = 'real',
                value = 464.1076,
                texname = '\\text{MWp}',
                lhablock = 'MASS',
                lhacode = [ 34 ])

Mh01 = Parameter(name = 'Mh01',
                 nature = 'external',
                 type = 'real',
                 value = 345.2953,
                 texname = '\\text{Mh01}',
                 lhablock = 'MASS',
                 lhacode = [ 25 ])

Mh02 = Parameter(name = 'Mh02',
                 nature = 'external',
                 type = 'real',
                 value = 554.5449,
                 texname = '\\text{Mh02}',
                 lhablock = 'MASS',
                 lhacode = [ 35 ])

Mh03 = Parameter(name = 'Mh03',
                 nature = 'external',
                 type = 'real',
                 value = 1224.745,
                 texname = '\\text{Mh03}',
                 lhablock = 'MASS',
                 lhacode = [ 45 ])

Mh04 = Parameter(name = 'Mh04',
                 nature = 'external',
                 type = 'real',
                 value = 2031.45,
                 texname = '\\text{Mh04}',
                 lhablock = 'MASS',
                 lhacode = [ 9000025 ])

MA0 = Parameter(name = 'MA0',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{MA0}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

MA01 = Parameter(name = 'MA01',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{MA01}',
                 lhablock = 'MASS',
                 lhacode = [ 46 ])

MH1 = Parameter(name = 'MH1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{MH1}',
                lhablock = 'MASS',
                lhacode = [ 37 ])

MH2 = Parameter(name = 'MH2',
                nature = 'external',
                type = 'real',
                value = 1224.745,
                texname = '\\text{MH2}',
                lhablock = 'MASS',
                lhacode = [ 9000037 ])

MDH1 = Parameter(name = 'MDH1',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MDH1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000055 ])

MDH2 = Parameter(name = 'MDH2',
                 nature = 'external',
                 type = 'real',
                 value = 1224.745,
                 texname = '\\text{MDH2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000056 ])

Mve = Parameter(name = 'Mve',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{Mve}',
                lhablock = 'MASS',
                lhacode = [ 12 ])

Mvm = Parameter(name = 'Mvm',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{Mvm}',
                lhablock = 'MASS',
                lhacode = [ 14 ])

Mvt = Parameter(name = 'Mvt',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{Mvt}',
                lhablock = 'MASS',
                lhacode = [ 16 ])

MNe = Parameter(name = 'MNe',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{MNe}',
                lhablock = 'MASS',
                lhacode = [ 6000012 ])

MNm = Parameter(name = 'MNm',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{MNm}',
                lhablock = 'MASS',
                lhacode = [ 6000014 ])

MNt = Parameter(name = 'MNt',
                nature = 'external',
                type = 'real',
                value = 3090.879,
                texname = '\\text{MNt}',
                lhablock = 'MASS',
                lhacode = [ 6000016 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

Mm = Parameter(name = 'Mm',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{Mm}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

Mta = Parameter(name = 'Mta',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Mta}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WZp = Parameter(name = 'WZp',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WZp}',
                lhablock = 'DECAY',
                lhacode = [ 32 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WWp = Parameter(name = 'WWp',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WWp}',
                lhablock = 'DECAY',
                lhacode = [ 34 ])

Wh02 = Parameter(name = 'Wh02',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wh02}',
                 lhablock = 'DECAY',
                 lhacode = [ 25 ])

Wh03 = Parameter(name = 'Wh03',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wh03}',
                 lhablock = 'DECAY',
                 lhacode = [ 35 ])

Wh04 = Parameter(name = 'Wh04',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wh04}',
                 lhablock = 'DECAY',
                 lhacode = [ 45 ])

Wh05 = Parameter(name = 'Wh05',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wh05}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000025 ])

WA01 = Parameter(name = 'WA01',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WA01}',
                 lhablock = 'DECAY',
                 lhacode = [ 36 ])

WA02 = Parameter(name = 'WA02',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WA02}',
                 lhablock = 'DECAY',
                 lhacode = [ 46 ])

WH1 = Parameter(name = 'WH1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WH1}',
                lhablock = 'DECAY',
                lhacode = [ 37 ])

WH2 = Parameter(name = 'WH2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WH2}',
                lhablock = 'DECAY',
                lhacode = [ 9000037 ])

WDH1 = Parameter(name = 'WDH1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WDH1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000055 ])

WDH2 = Parameter(name = 'WDH2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WDH2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000056 ])

WNe = Parameter(name = 'WNe',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WNe}',
                lhablock = 'DECAY',
                lhacode = [ 6000012 ])

WNm = Parameter(name = 'WNm',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WNm}',
                lhablock = 'DECAY',
                lhacode = [ 6000014 ])

WNt = Parameter(name = 'WNt',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WNt}',
                lhablock = 'DECAY',
                lhacode = [ 6000016 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

gBL = Parameter(name = 'gBL',
                nature = 'internal',
                type = 'real',
                value = '(gR*gY)/cmath.sqrt(gR**2 - gY**2)',
                texname = 'g_{B-L}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

yq11x1 = Parameter(name = 'yq11x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq11x1 + Ryq11x1',
                   texname = '\\text{yq11x1}')

yq11x2 = Parameter(name = 'yq11x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq11x2 + Ryq11x2',
                   texname = '\\text{yq11x2}')

yq11x3 = Parameter(name = 'yq11x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq11x3 + Ryq11x3',
                   texname = '\\text{yq11x3}')

yq12x1 = Parameter(name = 'yq12x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq12x1 + Ryq12x1',
                   texname = '\\text{yq12x1}')

yq12x2 = Parameter(name = 'yq12x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq12x2 + Ryq12x2',
                   texname = '\\text{yq12x2}')

yq12x3 = Parameter(name = 'yq12x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq12x3 + Ryq12x3',
                   texname = '\\text{yq12x3}')

yq13x1 = Parameter(name = 'yq13x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq13x1 + Ryq13x1',
                   texname = '\\text{yq13x1}')

yq13x2 = Parameter(name = 'yq13x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq13x2 + Ryq13x2',
                   texname = '\\text{yq13x2}')

yq13x3 = Parameter(name = 'yq13x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq13x3 + Ryq13x3',
                   texname = '\\text{yq13x3}')

yq21x1 = Parameter(name = 'yq21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq21x1 + Ryq21x1',
                   texname = '\\text{yq21x1}')

yq21x2 = Parameter(name = 'yq21x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq21x2 + Ryq21x2',
                   texname = '\\text{yq21x2}')

yq21x3 = Parameter(name = 'yq21x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq21x3 + Ryq21x3',
                   texname = '\\text{yq21x3}')

yq22x1 = Parameter(name = 'yq22x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq22x1 + Ryq22x1',
                   texname = '\\text{yq22x1}')

yq22x2 = Parameter(name = 'yq22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq22x2 + Ryq22x2',
                   texname = '\\text{yq22x2}')

yq22x3 = Parameter(name = 'yq22x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq22x3 + Ryq22x3',
                   texname = '\\text{yq22x3}')

yq23x1 = Parameter(name = 'yq23x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq23x1 + Ryq23x1',
                   texname = '\\text{yq23x1}')

yq23x2 = Parameter(name = 'yq23x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq23x2 + Ryq23x2',
                   texname = '\\text{yq23x2}')

yq23x3 = Parameter(name = 'yq23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyq23x3 + Ryq23x3',
                   texname = '\\text{yq23x3}')

yl11x1 = Parameter(name = 'yl11x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl11x1 + Ryl11x1',
                   texname = '\\text{yl11x1}')

yl11x2 = Parameter(name = 'yl11x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl11x2 + Ryl11x2',
                   texname = '\\text{yl11x2}')

yl11x3 = Parameter(name = 'yl11x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl11x3 + Ryl11x3',
                   texname = '\\text{yl11x3}')

yl12x1 = Parameter(name = 'yl12x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl12x1 + Ryl12x1',
                   texname = '\\text{yl12x1}')

yl12x2 = Parameter(name = 'yl12x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl12x2 + Ryl12x2',
                   texname = '\\text{yl12x2}')

yl12x3 = Parameter(name = 'yl12x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl12x3 + Ryl12x3',
                   texname = '\\text{yl12x3}')

yl13x1 = Parameter(name = 'yl13x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl13x1 + Ryl13x1',
                   texname = '\\text{yl13x1}')

yl13x2 = Parameter(name = 'yl13x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl13x2 + Ryl13x2',
                   texname = '\\text{yl13x2}')

yl13x3 = Parameter(name = 'yl13x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl13x3 + Ryl13x3',
                   texname = '\\text{yl13x3}')

yl21x1 = Parameter(name = 'yl21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl21x1 + Ryl21x1',
                   texname = '\\text{yl21x1}')

yl21x2 = Parameter(name = 'yl21x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl21x2 + Ryl21x2',
                   texname = '\\text{yl21x2}')

yl21x3 = Parameter(name = 'yl21x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl21x3 + Ryl21x3',
                   texname = '\\text{yl21x3}')

yl22x1 = Parameter(name = 'yl22x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl22x1 + Ryl22x1',
                   texname = '\\text{yl22x1}')

yl22x2 = Parameter(name = 'yl22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl22x2 + Ryl22x2',
                   texname = '\\text{yl22x2}')

yl22x3 = Parameter(name = 'yl22x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl22x3 + Ryl22x3',
                   texname = '\\text{yl22x3}')

yl23x1 = Parameter(name = 'yl23x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl23x1 + Ryl23x1',
                   texname = '\\text{yl23x1}')

yl23x2 = Parameter(name = 'yl23x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl23x2 + Ryl23x2',
                   texname = '\\text{yl23x2}')

yl23x3 = Parameter(name = 'yl23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl23x3 + Ryl23x3',
                   texname = '\\text{yl23x3}')

yl31x1 = Parameter(name = 'yl31x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl31x1 + Ryl31x1',
                   texname = '\\text{yl31x1}')

yl31x2 = Parameter(name = 'yl31x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl31x2 + Ryl31x2',
                   texname = '\\text{yl31x2}')

yl31x3 = Parameter(name = 'yl31x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl31x3 + Ryl31x3',
                   texname = '\\text{yl31x3}')

yl32x1 = Parameter(name = 'yl32x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl32x1 + Ryl32x1',
                   texname = '\\text{yl32x1}')

yl32x2 = Parameter(name = 'yl32x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl32x2 + Ryl32x2',
                   texname = '\\text{yl32x2}')

yl32x3 = Parameter(name = 'yl32x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl32x3 + Ryl32x3',
                   texname = '\\text{yl32x3}')

yl33x1 = Parameter(name = 'yl33x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl33x1 + Ryl33x1',
                   texname = '\\text{yl33x1}')

yl33x2 = Parameter(name = 'yl33x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl33x2 + Ryl33x2',
                   texname = '\\text{yl33x2}')

yl33x3 = Parameter(name = 'yl33x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl33x3 + Ryl33x3',
                   texname = '\\text{yl33x3}')

yl41x1 = Parameter(name = 'yl41x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl41x1 + Ryl41x1',
                   texname = '\\text{yl41x1}')

yl41x2 = Parameter(name = 'yl41x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl41x2 + Ryl41x2',
                   texname = '\\text{yl41x2}')

yl41x3 = Parameter(name = 'yl41x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl41x3 + Ryl41x3',
                   texname = '\\text{yl41x3}')

yl42x1 = Parameter(name = 'yl42x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl42x1 + Ryl42x1',
                   texname = '\\text{yl42x1}')

yl42x2 = Parameter(name = 'yl42x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl42x2 + Ryl42x2',
                   texname = '\\text{yl42x2}')

yl42x3 = Parameter(name = 'yl42x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl42x3 + Ryl42x3',
                   texname = '\\text{yl42x3}')

yl43x1 = Parameter(name = 'yl43x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl43x1 + Ryl43x1',
                   texname = '\\text{yl43x1}')

yl43x2 = Parameter(name = 'yl43x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl43x2 + Ryl43x2',
                   texname = '\\text{yl43x2}')

yl43x3 = Parameter(name = 'yl43x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*Iyl43x3 + Ryl43x3',
                   texname = '\\text{yl43x3}')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ILAM1 + RLAM1',
                 texname = '\\lambda _1')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ILAM2 + RLAM2',
                 texname = '\\lambda _2')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ILAM3 + RLAM3',
                 texname = '\\lambda _3')

lam4 = Parameter(name = 'lam4',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ILAM4 + RLAM4',
                 texname = '\\lambda _4')

lam5 = Parameter(name = 'lam5',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ILAM5 + RLAM5',
                 texname = '\\lambda _5')

lam6 = Parameter(name = 'lam6',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ILAM6 + RLAM6',
                 texname = '\\lambda _6')

rho1 = Parameter(name = 'rho1',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*IRHO1 + RRHO1',
                 texname = '\\rho _1')

rho2 = Parameter(name = 'rho2',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*IRHO2 + RRHO2',
                 texname = '\\rho _2')

rho3 = Parameter(name = 'rho3',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*IRHO3 + RRHO3',
                 texname = '\\rho _3')

al1 = Parameter(name = 'al1',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*IAL1 + RAL1',
                texname = '\\alpha _1')

al2 = Parameter(name = 'al2',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*IAL2 + RAL2',
                texname = '\\alpha _2')

al3 = Parameter(name = 'al3',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*IAL3 + RAL3',
                texname = '\\alpha _3')

UVN1x1 = Parameter(name = 'UVN1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN1x1 + RUVN1x1',
                   texname = '\\text{UVN1x1}')

UVN1x2 = Parameter(name = 'UVN1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN1x2 + RUVN1x2',
                   texname = '\\text{UVN1x2}')

UVN1x3 = Parameter(name = 'UVN1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN1x3 + RUVN1x3',
                   texname = '\\text{UVN1x3}')

UVN2x1 = Parameter(name = 'UVN2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN2x1 + RUVN2x1',
                   texname = '\\text{UVN2x1}')

UVN2x2 = Parameter(name = 'UVN2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN2x2 + RUVN2x2',
                   texname = '\\text{UVN2x2}')

UVN2x3 = Parameter(name = 'UVN2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN2x3 + RUVN2x3',
                   texname = '\\text{UVN2x3}')

UVN3x1 = Parameter(name = 'UVN3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN3x1 + RUVN3x1',
                   texname = '\\text{UVN3x1}')

UVN3x2 = Parameter(name = 'UVN3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN3x2 + RUVN3x2',
                   texname = '\\text{UVN3x2}')

UVN3x3 = Parameter(name = 'UVN3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVN3x3 + RUVN3x3',
                   texname = '\\text{UVN3x3}')

UVC1x1 = Parameter(name = 'UVC1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVC1x1 + RUVC1x1',
                   texname = '\\text{UVC1x1}')

UVC1x2 = Parameter(name = 'UVC1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVC1x2 + RUVC1x2',
                   texname = '\\text{UVC1x2}')

UVC2x1 = Parameter(name = 'UVC2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVC2x1 + RUVC2x1',
                   texname = '\\text{UVC2x1}')

UVC2x2 = Parameter(name = 'UVC2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUVC2x2 + RUVC2x2',
                   texname = '\\text{UVC2x2}')

UHD1x1 = Parameter(name = 'UHD1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHD1x1 + RUHD1x1',
                   texname = '\\text{UHD1x1}')

UHD1x2 = Parameter(name = 'UHD1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHD1x2 + RUHD1x2',
                   texname = '\\text{UHD1x2}')

UHD2x1 = Parameter(name = 'UHD2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHD2x1 + RUHD2x1',
                   texname = '\\text{UHD2x1}')

UHD2x2 = Parameter(name = 'UHD2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHD2x2 + RUHD2x2',
                   texname = '\\text{UHD2x2}')

UHC1x1 = Parameter(name = 'UHC1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC1x1 + RUHC1x1',
                   texname = '\\text{UHC1x1}')

UHC1x2 = Parameter(name = 'UHC1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC1x2 + RUHC1x2',
                   texname = '\\text{UHC1x2}')

UHC1x3 = Parameter(name = 'UHC1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC1x3 + RUHC1x3',
                   texname = '\\text{UHC1x3}')

UHC1x4 = Parameter(name = 'UHC1x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC1x4 + RUHC1x4',
                   texname = '\\text{UHC1x4}')

UHC2x1 = Parameter(name = 'UHC2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC2x1 + RUHC2x1',
                   texname = '\\text{UHC2x1}')

UHC2x2 = Parameter(name = 'UHC2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC2x2 + RUHC2x2',
                   texname = '\\text{UHC2x2}')

UHC2x3 = Parameter(name = 'UHC2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC2x3 + RUHC2x3',
                   texname = '\\text{UHC2x3}')

UHC2x4 = Parameter(name = 'UHC2x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC2x4 + RUHC2x4',
                   texname = '\\text{UHC2x4}')

UHC3x1 = Parameter(name = 'UHC3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC3x1 + RUHC3x1',
                   texname = '\\text{UHC3x1}')

UHC3x2 = Parameter(name = 'UHC3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC3x2 + RUHC3x2',
                   texname = '\\text{UHC3x2}')

UHC3x3 = Parameter(name = 'UHC3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC3x3 + RUHC3x3',
                   texname = '\\text{UHC3x3}')

UHC3x4 = Parameter(name = 'UHC3x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC3x4 + RUHC3x4',
                   texname = '\\text{UHC3x4}')

UHC4x1 = Parameter(name = 'UHC4x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC4x1 + RUHC4x1',
                   texname = '\\text{UHC4x1}')

UHC4x2 = Parameter(name = 'UHC4x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC4x2 + RUHC4x2',
                   texname = '\\text{UHC4x2}')

UHC4x3 = Parameter(name = 'UHC4x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC4x3 + RUHC4x3',
                   texname = '\\text{UHC4x3}')

UHC4x4 = Parameter(name = 'UHC4x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHC4x4 + RUHC4x4',
                   texname = '\\text{UHC4x4}')

UHN1x1 = Parameter(name = 'UHN1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN1x1 + RUHN1x1',
                   texname = '\\text{UHN1x1}')

UHN1x2 = Parameter(name = 'UHN1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN1x2 + RUHN1x2',
                   texname = '\\text{UHN1x2}')

UHN1x3 = Parameter(name = 'UHN1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN1x3 + RUHN1x3',
                   texname = '\\text{UHN1x3}')

UHN1x4 = Parameter(name = 'UHN1x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN1x4 + RUHN1x4',
                   texname = '\\text{UHN1x4}')

UHN2x1 = Parameter(name = 'UHN2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN2x1 + RUHN2x1',
                   texname = '\\text{UHN2x1}')

UHN2x2 = Parameter(name = 'UHN2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN2x2 + RUHN2x2',
                   texname = '\\text{UHN2x2}')

UHN2x3 = Parameter(name = 'UHN2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN2x3 + RUHN2x3',
                   texname = '\\text{UHN2x3}')

UHN2x4 = Parameter(name = 'UHN2x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN2x4 + RUHN2x4',
                   texname = '\\text{UHN2x4}')

UHN3x1 = Parameter(name = 'UHN3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN3x1 + RUHN3x1',
                   texname = '\\text{UHN3x1}')

UHN3x2 = Parameter(name = 'UHN3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN3x2 + RUHN3x2',
                   texname = '\\text{UHN3x2}')

UHN3x3 = Parameter(name = 'UHN3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN3x3 + RUHN3x3',
                   texname = '\\text{UHN3x3}')

UHN3x4 = Parameter(name = 'UHN3x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN3x4 + RUHN3x4',
                   texname = '\\text{UHN3x4}')

UHN4x1 = Parameter(name = 'UHN4x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN4x1 + RUHN4x1',
                   texname = '\\text{UHN4x1}')

UHN4x2 = Parameter(name = 'UHN4x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN4x2 + RUHN4x2',
                   texname = '\\text{UHN4x2}')

UHN4x3 = Parameter(name = 'UHN4x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN4x3 + RUHN4x3',
                   texname = '\\text{UHN4x3}')

UHN4x4 = Parameter(name = 'UHN4x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUHN4x4 + RUHN4x4',
                   texname = '\\text{UHN4x4}')

UAN1x1 = Parameter(name = 'UAN1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN1x1 + RUAN1x1',
                   texname = '\\text{UAN1x1}')

UAN1x2 = Parameter(name = 'UAN1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN1x2 + RUAN1x2',
                   texname = '\\text{UAN1x2}')

UAN1x3 = Parameter(name = 'UAN1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN1x3 + RUAN1x3',
                   texname = '\\text{UAN1x3}')

UAN1x4 = Parameter(name = 'UAN1x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN1x4 + RUAN1x4',
                   texname = '\\text{UAN1x4}')

UAN2x1 = Parameter(name = 'UAN2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN2x1 + RUAN2x1',
                   texname = '\\text{UAN2x1}')

UAN2x2 = Parameter(name = 'UAN2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN2x2 + RUAN2x2',
                   texname = '\\text{UAN2x2}')

UAN2x3 = Parameter(name = 'UAN2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN2x3 + RUAN2x3',
                   texname = '\\text{UAN2x3}')

UAN2x4 = Parameter(name = 'UAN2x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN2x4 + RUAN2x4',
                   texname = '\\text{UAN2x4}')

UAN3x1 = Parameter(name = 'UAN3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN3x1 + RUAN3x1',
                   texname = '\\text{UAN3x1}')

UAN3x2 = Parameter(name = 'UAN3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN3x2 + RUAN3x2',
                   texname = '\\text{UAN3x2}')

UAN3x3 = Parameter(name = 'UAN3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN3x3 + RUAN3x3',
                   texname = '\\text{UAN3x3}')

UAN3x4 = Parameter(name = 'UAN3x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN3x4 + RUAN3x4',
                   texname = '\\text{UAN3x4}')

UAN4x1 = Parameter(name = 'UAN4x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN4x1 + RUAN4x1',
                   texname = '\\text{UAN4x1}')

UAN4x2 = Parameter(name = 'UAN4x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN4x2 + RUAN4x2',
                   texname = '\\text{UAN4x2}')

UAN4x3 = Parameter(name = 'UAN4x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN4x3 + RUAN4x3',
                   texname = '\\text{UAN4x3}')

UAN4x4 = Parameter(name = 'UAN4x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUAN4x4 + RUAN4x4',
                   texname = '\\text{UAN4x4}')

CKML1x1 = Parameter(name = 'CKML1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML1x1 + RCKML1x1',
                    texname = '\\text{CKML1x1}')

CKML1x2 = Parameter(name = 'CKML1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML1x2 + RCKML1x2',
                    texname = '\\text{CKML1x2}')

CKML1x3 = Parameter(name = 'CKML1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML1x3 + RCKML1x3',
                    texname = '\\text{CKML1x3}')

CKML2x1 = Parameter(name = 'CKML2x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML2x1 + RCKML2x1',
                    texname = '\\text{CKML2x1}')

CKML2x2 = Parameter(name = 'CKML2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML2x2 + RCKML2x2',
                    texname = '\\text{CKML2x2}')

CKML2x3 = Parameter(name = 'CKML2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML2x3 + RCKML2x3',
                    texname = '\\text{CKML2x3}')

CKML3x1 = Parameter(name = 'CKML3x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML3x1 + RCKML3x1',
                    texname = '\\text{CKML3x1}')

CKML3x2 = Parameter(name = 'CKML3x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML3x2 + RCKML3x2',
                    texname = '\\text{CKML3x2}')

CKML3x3 = Parameter(name = 'CKML3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKML3x3 + RCKML3x3',
                    texname = '\\text{CKML3x3}')

CKMR1x1 = Parameter(name = 'CKMR1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR1x1 + RCKMR1x1',
                    texname = '\\text{CKMR1x1}')

CKMR1x2 = Parameter(name = 'CKMR1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR1x2 + RCKMR1x2',
                    texname = '\\text{CKMR1x2}')

CKMR1x3 = Parameter(name = 'CKMR1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR1x3 + RCKMR1x3',
                    texname = '\\text{CKMR1x3}')

CKMR2x1 = Parameter(name = 'CKMR2x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR2x1 + RCKMR2x1',
                    texname = '\\text{CKMR2x1}')

CKMR2x2 = Parameter(name = 'CKMR2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR2x2 + RCKMR2x2',
                    texname = '\\text{CKMR2x2}')

CKMR2x3 = Parameter(name = 'CKMR2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR2x3 + RCKMR2x3',
                    texname = '\\text{CKMR2x3}')

CKMR3x1 = Parameter(name = 'CKMR3x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR3x1 + RCKMR3x1',
                    texname = '\\text{CKMR3x1}')

CKMR3x2 = Parameter(name = 'CKMR3x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR3x2 + RCKMR3x2',
                    texname = '\\text{CKMR3x2}')

CKMR3x3 = Parameter(name = 'CKMR3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*ICKMR3x3 + RCKMR3x3',
                    texname = '\\text{CKMR3x3}')

PMNSL1x1 = Parameter(name = 'PMNSL1x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL1x1 + RPMNSL1x1',
                     texname = '\\text{PMNSL1x1}')

PMNSL1x2 = Parameter(name = 'PMNSL1x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL1x2 + RPMNSL1x2',
                     texname = '\\text{PMNSL1x2}')

PMNSL1x3 = Parameter(name = 'PMNSL1x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL1x3 + RPMNSL1x3',
                     texname = '\\text{PMNSL1x3}')

PMNSL1x4 = Parameter(name = 'PMNSL1x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL1x4 + RPMNSL1x4',
                     texname = '\\text{PMNSL1x4}')

PMNSL1x5 = Parameter(name = 'PMNSL1x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL1x5 + RPMNSL1x5',
                     texname = '\\text{PMNSL1x5}')

PMNSL1x6 = Parameter(name = 'PMNSL1x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL1x6 + RPMNSL1x6',
                     texname = '\\text{PMNSL1x6}')

PMNSL2x1 = Parameter(name = 'PMNSL2x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL2x1 + RPMNSL2x1',
                     texname = '\\text{PMNSL2x1}')

PMNSL2x2 = Parameter(name = 'PMNSL2x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL2x2 + RPMNSL2x2',
                     texname = '\\text{PMNSL2x2}')

PMNSL2x3 = Parameter(name = 'PMNSL2x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL2x3 + RPMNSL2x3',
                     texname = '\\text{PMNSL2x3}')

PMNSL2x4 = Parameter(name = 'PMNSL2x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL2x4 + RPMNSL2x4',
                     texname = '\\text{PMNSL2x4}')

PMNSL2x5 = Parameter(name = 'PMNSL2x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL2x5 + RPMNSL2x5',
                     texname = '\\text{PMNSL2x5}')

PMNSL2x6 = Parameter(name = 'PMNSL2x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL2x6 + RPMNSL2x6',
                     texname = '\\text{PMNSL2x6}')

PMNSL3x1 = Parameter(name = 'PMNSL3x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL3x1 + RPMNSL3x1',
                     texname = '\\text{PMNSL3x1}')

PMNSL3x2 = Parameter(name = 'PMNSL3x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL3x2 + RPMNSL3x2',
                     texname = '\\text{PMNSL3x2}')

PMNSL3x3 = Parameter(name = 'PMNSL3x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL3x3 + RPMNSL3x3',
                     texname = '\\text{PMNSL3x3}')

PMNSL3x4 = Parameter(name = 'PMNSL3x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL3x4 + RPMNSL3x4',
                     texname = '\\text{PMNSL3x4}')

PMNSL3x5 = Parameter(name = 'PMNSL3x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL3x5 + RPMNSL3x5',
                     texname = '\\text{PMNSL3x5}')

PMNSL3x6 = Parameter(name = 'PMNSL3x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL3x6 + RPMNSL3x6',
                     texname = '\\text{PMNSL3x6}')

PMNSL4x1 = Parameter(name = 'PMNSL4x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL4x1 + RPMNSL4x1',
                     texname = '\\text{PMNSL4x1}')

PMNSL4x2 = Parameter(name = 'PMNSL4x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL4x2 + RPMNSL4x2',
                     texname = '\\text{PMNSL4x2}')

PMNSL4x3 = Parameter(name = 'PMNSL4x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL4x3 + RPMNSL4x3',
                     texname = '\\text{PMNSL4x3}')

PMNSL4x4 = Parameter(name = 'PMNSL4x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL4x4 + RPMNSL4x4',
                     texname = '\\text{PMNSL4x4}')

PMNSL4x5 = Parameter(name = 'PMNSL4x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL4x5 + RPMNSL4x5',
                     texname = '\\text{PMNSL4x5}')

PMNSL4x6 = Parameter(name = 'PMNSL4x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL4x6 + RPMNSL4x6',
                     texname = '\\text{PMNSL4x6}')

PMNSL5x1 = Parameter(name = 'PMNSL5x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL5x1 + RPMNSL5x1',
                     texname = '\\text{PMNSL5x1}')

PMNSL5x2 = Parameter(name = 'PMNSL5x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL5x2 + RPMNSL5x2',
                     texname = '\\text{PMNSL5x2}')

PMNSL5x3 = Parameter(name = 'PMNSL5x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL5x3 + RPMNSL5x3',
                     texname = '\\text{PMNSL5x3}')

PMNSL5x4 = Parameter(name = 'PMNSL5x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL5x4 + RPMNSL5x4',
                     texname = '\\text{PMNSL5x4}')

PMNSL5x5 = Parameter(name = 'PMNSL5x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL5x5 + RPMNSL5x5',
                     texname = '\\text{PMNSL5x5}')

PMNSL5x6 = Parameter(name = 'PMNSL5x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL5x6 + RPMNSL5x6',
                     texname = '\\text{PMNSL5x6}')

PMNSL6x1 = Parameter(name = 'PMNSL6x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL6x1 + RPMNSL6x1',
                     texname = '\\text{PMNSL6x1}')

PMNSL6x2 = Parameter(name = 'PMNSL6x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL6x2 + RPMNSL6x2',
                     texname = '\\text{PMNSL6x2}')

PMNSL6x3 = Parameter(name = 'PMNSL6x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL6x3 + RPMNSL6x3',
                     texname = '\\text{PMNSL6x3}')

PMNSL6x4 = Parameter(name = 'PMNSL6x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL6x4 + RPMNSL6x4',
                     texname = '\\text{PMNSL6x4}')

PMNSL6x5 = Parameter(name = 'PMNSL6x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL6x5 + RPMNSL6x5',
                     texname = '\\text{PMNSL6x5}')

PMNSL6x6 = Parameter(name = 'PMNSL6x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSL6x6 + RPMNSL6x6',
                     texname = '\\text{PMNSL6x6}')

PMNSR1x1 = Parameter(name = 'PMNSR1x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR1x1 + RPMNSR1x1',
                     texname = '\\text{PMNSR1x1}')

PMNSR1x2 = Parameter(name = 'PMNSR1x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR1x2 + RPMNSR1x2',
                     texname = '\\text{PMNSR1x2}')

PMNSR1x3 = Parameter(name = 'PMNSR1x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR1x3 + RPMNSR1x3',
                     texname = '\\text{PMNSR1x3}')

PMNSR1x4 = Parameter(name = 'PMNSR1x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR1x4 + RPMNSR1x4',
                     texname = '\\text{PMNSR1x4}')

PMNSR1x5 = Parameter(name = 'PMNSR1x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR1x5 + RPMNSR1x5',
                     texname = '\\text{PMNSR1x5}')

PMNSR1x6 = Parameter(name = 'PMNSR1x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR1x6 + RPMNSR1x6',
                     texname = '\\text{PMNSR1x6}')

PMNSR2x1 = Parameter(name = 'PMNSR2x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR2x1 + RPMNSR2x1',
                     texname = '\\text{PMNSR2x1}')

PMNSR2x2 = Parameter(name = 'PMNSR2x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR2x2 + RPMNSR2x2',
                     texname = '\\text{PMNSR2x2}')

PMNSR2x3 = Parameter(name = 'PMNSR2x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR2x3 + RPMNSR2x3',
                     texname = '\\text{PMNSR2x3}')

PMNSR2x4 = Parameter(name = 'PMNSR2x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR2x4 + RPMNSR2x4',
                     texname = '\\text{PMNSR2x4}')

PMNSR2x5 = Parameter(name = 'PMNSR2x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR2x5 + RPMNSR2x5',
                     texname = '\\text{PMNSR2x5}')

PMNSR2x6 = Parameter(name = 'PMNSR2x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR2x6 + RPMNSR2x6',
                     texname = '\\text{PMNSR2x6}')

PMNSR3x1 = Parameter(name = 'PMNSR3x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR3x1 + RPMNSR3x1',
                     texname = '\\text{PMNSR3x1}')

PMNSR3x2 = Parameter(name = 'PMNSR3x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR3x2 + RPMNSR3x2',
                     texname = '\\text{PMNSR3x2}')

PMNSR3x3 = Parameter(name = 'PMNSR3x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR3x3 + RPMNSR3x3',
                     texname = '\\text{PMNSR3x3}')

PMNSR3x4 = Parameter(name = 'PMNSR3x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR3x4 + RPMNSR3x4',
                     texname = '\\text{PMNSR3x4}')

PMNSR3x5 = Parameter(name = 'PMNSR3x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR3x5 + RPMNSR3x5',
                     texname = '\\text{PMNSR3x5}')

PMNSR3x6 = Parameter(name = 'PMNSR3x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR3x6 + RPMNSR3x6',
                     texname = '\\text{PMNSR3x6}')

PMNSR4x1 = Parameter(name = 'PMNSR4x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR4x1 + RPMNSR4x1',
                     texname = '\\text{PMNSR4x1}')

PMNSR4x2 = Parameter(name = 'PMNSR4x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR4x2 + RPMNSR4x2',
                     texname = '\\text{PMNSR4x2}')

PMNSR4x3 = Parameter(name = 'PMNSR4x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR4x3 + RPMNSR4x3',
                     texname = '\\text{PMNSR4x3}')

PMNSR4x4 = Parameter(name = 'PMNSR4x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR4x4 + RPMNSR4x4',
                     texname = '\\text{PMNSR4x4}')

PMNSR4x5 = Parameter(name = 'PMNSR4x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR4x5 + RPMNSR4x5',
                     texname = '\\text{PMNSR4x5}')

PMNSR4x6 = Parameter(name = 'PMNSR4x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR4x6 + RPMNSR4x6',
                     texname = '\\text{PMNSR4x6}')

PMNSR5x1 = Parameter(name = 'PMNSR5x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR5x1 + RPMNSR5x1',
                     texname = '\\text{PMNSR5x1}')

PMNSR5x2 = Parameter(name = 'PMNSR5x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR5x2 + RPMNSR5x2',
                     texname = '\\text{PMNSR5x2}')

PMNSR5x3 = Parameter(name = 'PMNSR5x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR5x3 + RPMNSR5x3',
                     texname = '\\text{PMNSR5x3}')

PMNSR5x4 = Parameter(name = 'PMNSR5x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR5x4 + RPMNSR5x4',
                     texname = '\\text{PMNSR5x4}')

PMNSR5x5 = Parameter(name = 'PMNSR5x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR5x5 + RPMNSR5x5',
                     texname = '\\text{PMNSR5x5}')

PMNSR5x6 = Parameter(name = 'PMNSR5x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR5x6 + RPMNSR5x6',
                     texname = '\\text{PMNSR5x6}')

PMNSR6x1 = Parameter(name = 'PMNSR6x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR6x1 + RPMNSR6x1',
                     texname = '\\text{PMNSR6x1}')

PMNSR6x2 = Parameter(name = 'PMNSR6x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR6x2 + RPMNSR6x2',
                     texname = '\\text{PMNSR6x2}')

PMNSR6x3 = Parameter(name = 'PMNSR6x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR6x3 + RPMNSR6x3',
                     texname = '\\text{PMNSR6x3}')

PMNSR6x4 = Parameter(name = 'PMNSR6x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR6x4 + RPMNSR6x4',
                     texname = '\\text{PMNSR6x4}')

PMNSR6x5 = Parameter(name = 'PMNSR6x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR6x5 + RPMNSR6x5',
                     texname = '\\text{PMNSR6x5}')

PMNSR6x6 = Parameter(name = 'PMNSR6x6',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complex(0,1)*IPMNSR6x6 + RPMNSR6x6',
                     texname = '\\text{PMNSR6x6}')

mu12 = Parameter(name = 'mu12',
                 nature = 'internal',
                 type = 'complex',
                 value = '(2*(lam1 + lam2)*v1**2 + 2*(lam1 + 4*lam3 + lam5 + lam6)*v1p**2 + (al1 + al3)*(vL**2 + vR**2))/2.',
                 texname = '\\mu _1{}^2')

mu22 = Parameter(name = 'mu22',
                 nature = 'internal',
                 type = 'complex',
                 value = '((al1 + al3)*v1**2 + (al1 + al2)*v1p**2 + rho3*vL**2 + 2*(rho1 + rho2)*vR**2)/2.',
                 texname = '\\mu _2{}^2')

mu1 = Parameter(name = 'mu1',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.sqrt(mu12)',
                texname = '\\mu _1')

mu2 = Parameter(name = 'mu2',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.sqrt(mu22)',
                texname = '\\mu _2')

