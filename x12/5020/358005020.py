from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'VEH', MIN: 0, MAX: 10},
    {ID: 'CII', MIN: 0, MAX: 3},
    {ID: 'NM1', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'DMA', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 10},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'VID', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'MBL', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'M13', MIN: 0, MAX: 1},
                {ID: 'X1', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
