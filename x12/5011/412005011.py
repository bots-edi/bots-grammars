from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'R11', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 5},
    {ID: 'CUR', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'R12', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'AMT', MIN: 1, MAX: 6},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'N1', MIN: 1, MAX: 4, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'R13', MIN: 1, MAX: 50, LEVEL: [
            {ID: 'IT1', MIN: 0, MAX: 10},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'AMT', MIN: 1, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
