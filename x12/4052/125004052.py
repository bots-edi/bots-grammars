from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BMM', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 1, MAX: 1},
    {ID: 'N7', MIN: 1, MAX: 1},
    {ID: 'VC', MIN: 0, MAX: 21},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
