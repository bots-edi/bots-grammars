from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'VB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BVB', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 1, MAX: 1},
    {ID: 'VC', MIN: 0, MAX: 99},
    {ID: 'SFC', MIN: 0, MAX: 20},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
