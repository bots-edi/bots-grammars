from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PU',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'PUN', MIN: 1, MAX: 1},
    {ID: 'G61', MIN: 0, MAX: 1},
    {ID: 'TEM', MIN: 0, MAX: 1},
    {ID: 'K2', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
