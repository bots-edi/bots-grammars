from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'F01', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 5},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'F02', MIN: 1, MAX: 100, LEVEL: [
        {ID: 'F05', MIN: 0, MAX: 1},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'F09', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'F04', MIN: 0, MAX: 1},
            {ID: 'F05', MIN: 0, MAX: 10},
            {ID: 'NTE', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
