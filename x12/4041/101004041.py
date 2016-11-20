from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'NL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 1, MAX: 99999},
        {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'IN2', MIN: 0, MAX: 99999},
                {ID: 'NX2', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'SPA', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
