from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'VC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BVP', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'VC', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'VC1', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
