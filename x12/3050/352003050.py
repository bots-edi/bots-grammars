from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'M14', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'K1', MIN: 0, MAX: 4},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
