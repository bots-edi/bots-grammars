from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'GR2', MIN: 1, MAX: 1},
    {ID: 'V1', MIN: 0, MAX: 1},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'GR4', MIN: 1, MAX: 100, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'N7', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'GR5', MIN: 0, MAX: 10},
            {ID: 'V1', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'R4', MIN: 0, MAX: 10},
            {ID: 'REF', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
