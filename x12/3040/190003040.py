from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'ENR', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 1, MAX: 2},
    {ID: 'ENT', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'IN2', MIN: 0, MAX: 5},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
