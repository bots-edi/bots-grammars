from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'RIC', MIN: 1, MAX: 1},
    {ID: 'TRN', MIN: 0, MAX: 2},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'DTM', MIN: 0, MAX: 5},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
