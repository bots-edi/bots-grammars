from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TU',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BLR', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 3},
        {ID: 'NTE', MIN: 0, MAX: 3},
        {ID: 'N7', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'M7', MIN: 0, MAX: 2},
            {ID: 'G62', MIN: 0, MAX: 1},
            {ID: 'TRL', MIN: 0, MAX: 1},
            {ID: 'L11', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
