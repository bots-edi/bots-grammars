from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCQ', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'QTY', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 3},
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N3', MIN: 0, MAX: 1},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 2},
    {ID: 'LX', MIN: 1, MAX: 31, LEVEL: [
        {ID: 'G62', MIN: 1, MAX: 2},
        {ID: 'D9', MIN: 0, MAX: 1},
        {ID: 'F9', MIN: 1, MAX: 31, LEVEL: [
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'R2', MIN: 1, MAX: 10},
            {ID: 'SCO', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'G62', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 4},
                {ID: 'N7', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'NA', MIN: 0, MAX: 1},
                    {ID: 'N9', MIN: 0, MAX: 5},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
