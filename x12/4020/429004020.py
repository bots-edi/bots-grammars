from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RU',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'RU1', MIN: 0, MAX: 999},
    {ID: 'RU2', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'RU3', MIN: 0, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 2},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
