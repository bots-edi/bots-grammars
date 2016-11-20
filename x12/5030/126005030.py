from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'VA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BVA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'V1', MIN: 0, MAX: 1},
        {ID: 'L7', MIN: 0, MAX: 5},
        {ID: 'VAD', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'L7', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
