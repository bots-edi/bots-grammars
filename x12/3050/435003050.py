from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RK',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'SID', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 30},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'LQ', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 100},
        ]},
        {ID: 'LX', MIN: 0, MAX: 4, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 50},
            {ID: 'LH3', MIN: 0, MAX: 100},
            {ID: 'LH2', MIN: 0, MAX: 8},
            {ID: 'LFH', MIN: 0, MAX: 20},
            {ID: 'LEP', MIN: 0, MAX: 3},
            {ID: 'LH4', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
