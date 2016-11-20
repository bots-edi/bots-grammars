from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B4', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 25},
    {ID: 'N1', MIN: 0, MAX: 2},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
