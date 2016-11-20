from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RH',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N2', MIN: 0, MAX: 2},
    {ID: 'N3', MIN: 0, MAX: 1},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'SMS', MIN: 1, MAX: 4, LEVEL: [
        {ID: 'SMR', MIN: 1, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PI', MIN: 0, MAX: 1},
        {ID: 'CD', MIN: 0, MAX: 150, LEVEL: [
            {ID: 'SID', MIN: 0, MAX: 2},
            {ID: 'BLR', MIN: 0, MAX: 20},
            {ID: 'N4', MIN: 0, MAX: 50},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
