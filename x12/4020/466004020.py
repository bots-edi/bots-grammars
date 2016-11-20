from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'REN', MIN: 1, MAX: 1},
    {ID: 'DK', MIN: 0, MAX: 1},
    {ID: 'PR1', MIN: 0, MAX: 1},
    {ID: 'PR2', MIN: 0, MAX: 1},
    {ID: 'PI', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
