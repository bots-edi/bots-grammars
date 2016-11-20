from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BJF', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'JCT', MIN: 0, MAX: 1},
    {ID: 'JS', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 3},
        {ID: 'SID', MIN: 0, MAX: 20},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
