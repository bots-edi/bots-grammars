from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'M13', MIN: 0, MAX: 1},
            {ID: 'M21', MIN: 0, MAX: 1},
            {ID: 'M12', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
