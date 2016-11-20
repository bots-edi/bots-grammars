from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'IS1', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 2},
    {ID: 'IS2', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'N8', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 2},
        {ID: 'F9', MIN: 0, MAX: 1},
        {ID: 'D9', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 2},
        {ID: 'S9', MIN: 0, MAX: 5},
        {ID: 'R2', MIN: 0, MAX: 13},
        {ID: 'L5', MIN: 0, MAX: 1},
        {ID: 'H3', MIN: 0, MAX: 5},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
