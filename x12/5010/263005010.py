from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 1, MAX: 1},
        {ID: 'REF', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N1', MIN: 1, MAX: 1},
            {ID: 'MIR', MIN: 1, MAX: 1},
            {ID: 'TXI', MIN: 0, MAX: 5},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'MIC', MIN: 0, MAX: 1},
            {ID: 'G63', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PCT', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
