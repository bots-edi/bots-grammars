from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2},
    {ID: 'DTP', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 1, MAX: 99999},
            {ID: 'PPA', MIN: 0, MAX: 1},
            {ID: 'TA', MIN: 0, MAX: 99999},
            {ID: 'ASI', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
