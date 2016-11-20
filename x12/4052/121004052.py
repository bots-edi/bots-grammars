from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'VS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BVS', MIN: 1, MAX: 1},
    {ID: 'N7', MIN: 0, MAX: 1},
    {ID: 'V1', MIN: 0, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 3},
    {ID: 'VC', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 3},
        {ID: 'DEL', MIN: 0, MAX: 1},
        {ID: 'CGS', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
