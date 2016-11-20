from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'D3',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BC', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 2},
    {ID: 'G61', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'CS', MIN: 1, MAX: 100, LEVEL: [
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 3},
        {ID: 'G61', MIN: 0, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 5},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
