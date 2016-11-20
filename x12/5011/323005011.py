from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'V1', MIN: 1, MAX: 1},
    {ID: 'K1', MIN: 0, MAX: 2},
    {ID: 'R4', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 15},
        {ID: 'V9', MIN: 1, MAX: 5},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
