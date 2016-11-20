from bots.botsconfig import *
from records004040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'PRI', MIN: 0, MAX: 1},
    {ID: 'SA', MIN: 1, MAX: 1},
    {ID: 'SC', MIN: 0, MAX: 8, LEVEL: [
        {ID: 'RA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'FK', MIN: 0, MAX: 5},
            {ID: 'MC', MIN: 0, MAX: 64, LEVEL: [
                {ID: 'FK', MIN: 0, MAX: 5},
            ]},
            {ID: 'SW', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
