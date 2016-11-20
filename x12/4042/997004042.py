from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'AK1', MIN: 1, MAX: 1},
    {ID: 'AK2', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'AK3', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'AK4', MIN: 0, MAX: 99},
        ]},
        {ID: 'AK5', MIN: 1, MAX: 1},
    ]},
    {ID: 'AK9', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
