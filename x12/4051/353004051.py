from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AX',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 0, MAX: 1},
    {ID: 'P4', MIN: 0, MAX: 1},
    {ID: 'M15', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'K1', MIN: 0, MAX: 4},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
