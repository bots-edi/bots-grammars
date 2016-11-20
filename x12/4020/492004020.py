from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'PRI', MIN: 1, MAX: 1},
    {ID: 'DM', MIN: 0, MAX: 1},
    {ID: 'SC', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DM', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
