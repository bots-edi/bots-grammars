from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'REN', MIN: 1, MAX: 1},
    {ID: 'DK', MIN: 0, MAX: 300000, LEVEL: [
        {ID: 'LQ', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'NTE', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
