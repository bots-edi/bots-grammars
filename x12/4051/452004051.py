from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGP', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 5},
    {ID: 'DTP', MIN: 0, MAX: 2},
    {ID: 'NTE', MIN: 0, MAX: 999999},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
