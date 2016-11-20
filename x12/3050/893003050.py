from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'G39', MIN: 1, MAX: 9999},
    {ID: 'G69', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 2},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
