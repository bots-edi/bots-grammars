from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'V1', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'MBL', MIN: 0, MAX: 1},
        {ID: 'G1', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 999},
        {ID: 'VC', MIN: 0, MAX: 9999},
        {ID: 'N7', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'VC', MIN: 0, MAX: 9},
        ]},
        {ID: 'R4', MIN: 1, MAX: 4, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
