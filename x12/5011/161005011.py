from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTS', MIN: 1, MAX: 1},
    {ID: 'V9', MIN: 1, MAX: 100},
    {ID: 'N9', MIN: 0, MAX: 3},
    {ID: 'H3', MIN: 0, MAX: 5},
    {ID: 'FAC', MIN: 0, MAX: 10},
    {ID: 'PWK', MIN: 0, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 5},
    {ID: 'NM1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 3},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
