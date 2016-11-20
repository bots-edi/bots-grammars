from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'IIS', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'STS', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
