from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MK',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'BLR', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'CA1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LC1', MIN: 1, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
