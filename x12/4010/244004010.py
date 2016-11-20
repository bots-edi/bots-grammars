from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 1},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 99999},
            {ID: 'BSF', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'NX2', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 99999},
                ]},
                {ID: 'PID', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'CID', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
