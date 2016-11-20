from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BA1', MIN: 1, MAX: 1},
    {ID: 'V5', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'P5', MIN: 1, MAX: 2},
    {ID: 'REF', MIN: 0, MAX: 9},
    {ID: 'L13', MIN: 1, MAX: 999},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
