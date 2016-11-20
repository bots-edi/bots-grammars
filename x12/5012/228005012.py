from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'EN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'Q5', MIN: 1, MAX: 1},
    {ID: 'W2', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'NA', MIN: 0, MAX: 30},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'EQD', MIN: 1, MAX: 1000, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 3},
            {ID: 'NTE', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'L11', MIN: 0, MAX: 5},
            {ID: 'NM1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 3},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
