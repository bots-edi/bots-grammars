from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ZC1', MIN: 0, MAX: 1},
    {ID: 'Q5', MIN: 0, MAX: 1},
    {ID: 'W2A', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'NA', MIN: 0, MAX: 10},
        {ID: 'N9', MIN: 0, MAX: 30},
        {ID: 'M7', MIN: 0, MAX: 1},
        {ID: 'Q5', MIN: 0, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 1},
        {ID: 'PRO', MIN: 0, MAX: 1},
        {ID: 'V1', MIN: 0, MAX: 1},
        {ID: 'R4', MIN: 0, MAX: 8},
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'H3', MIN: 0, MAX: 20},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
