from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 9},
    ]},
    {ID: 'G62', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 1, MAX: 9},
    {ID: 'TD5', MIN: 1, MAX: 1},
    {ID: 'L0', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'L5', MIN: 0, MAX: 999},
        {ID: 'H1', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
