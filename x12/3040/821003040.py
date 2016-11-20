from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'ACT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'BAL', MIN: 0, MAX: 99999},
        ]},
        {ID: 'FIR', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'TRN', MIN: 0, MAX: 1},
            {ID: 'AVA', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
