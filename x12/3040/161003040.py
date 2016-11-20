from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTS', MIN: 1, MAX: 1},
    {ID: 'FAC', MIN: 1, MAX: 10},
    {ID: 'V9', MIN: 0, MAX: 10},
    {ID: 'NM1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 3},
    ]},
    {ID: 'SE', MIN: 0, MAX: 1},
]}
]
