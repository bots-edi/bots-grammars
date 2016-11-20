from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'JL', MIN: 1, MAX: 7, LEVEL: [
        {ID: 'K1', MIN: 1, MAX: 100},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
