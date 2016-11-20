from bots.botsconfig import *
from records004040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'LEQ', MIN: 0, MAX: 1},
    {ID: 'CTC', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CIC', MIN: 1, MAX: 1000, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 2},
            {ID: 'LX', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CHR', MIN: 0, MAX: 3},
                {ID: 'CYC', MIN: 0, MAX: 2},
                {ID: 'PRI', MIN: 0, MAX: 1},
                {ID: 'PI', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 2},
                {ID: 'CUR', MIN: 0, MAX: 1},
                {ID: 'CV', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
