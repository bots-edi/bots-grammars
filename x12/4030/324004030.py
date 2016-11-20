from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'V1', MIN: 1, MAX: 1},
    {ID: 'R4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 15},
    ]},
    {ID: 'N7', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'ED', MIN: 0, MAX: 1},
        {ID: 'NA', MIN: 0, MAX: 2},
        {ID: 'V4', MIN: 1, MAX: 1},
        {ID: 'R4', MIN: 0, MAX: 9},
        {ID: 'W09', MIN: 0, MAX: 1},
        {ID: 'H3', MIN: 0, MAX: 6},
        {ID: 'H1', MIN: 0, MAX: 4},
        {ID: 'N9', MIN: 0, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
