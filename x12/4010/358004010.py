from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 500, LEVEL: [
            {ID: 'VID', MIN: 0, MAX: 1},
            {ID: 'MBL', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'M13', MIN: 0, MAX: 1},
                {ID: 'VID', MIN: 0, MAX: 500},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
