from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'LT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'GR', MIN: 1, MAX: 1},
    {ID: 'LV', MIN: 0, MAX: 25},
    {ID: 'DB', MIN: 0, MAX: 10},
    {ID: 'DTP', MIN: 0, MAX: 10},
    {ID: 'IDB', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 5},
    {ID: 'ENT', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'IN2', MIN: 0, MAX: 5},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
