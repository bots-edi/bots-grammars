from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 3},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'ENT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'G28', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'G69', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
