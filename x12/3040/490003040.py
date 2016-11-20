from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'REN', MIN: 1, MAX: 1},
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'GH', MIN: 1, MAX: 1},
    {ID: 'PI', MIN: 0, MAX: 8},
    {ID: 'TT', MIN: 0, MAX: 500},
    {ID: 'GY', MIN: 0, MAX: 500},
    {ID: 'CD', MIN: 0, MAX: 500},
    {ID: 'PR', MIN: 0, MAX: 500},
    {ID: 'PT', MIN: 0, MAX: 500, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
