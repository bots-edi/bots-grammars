from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B1', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 6},
    {ID: 'N7', MIN: 0, MAX: 1},
    {ID: 'L9', MIN: 0, MAX: 40},
    {ID: 'V9', MIN: 0, MAX: 10},
    {ID: 'K1', MIN: 0, MAX: 10},
    {ID: 'S5', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'K1', MIN: 0, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
