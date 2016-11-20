from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'E6', MIN: 1, MAX: 150, LEVEL: [
        {ID: 'W3', MIN: 0, MAX: 1},
        {ID: 'W5', MIN: 0, MAX: 4},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
