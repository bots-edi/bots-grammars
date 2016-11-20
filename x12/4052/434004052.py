from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BRR', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'N1', MIN: 1, MAX: 25, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
