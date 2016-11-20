from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'G21', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'G69', MIN: 0, MAX: 5},
        {ID: 'CTP', MIN: 0, MAX: 1},
        {ID: 'G72', MIN: 0, MAX: 99999},
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'G62', MIN: 0, MAX: 10},
            {ID: 'G22', MIN: 0, MAX: 1},
            {ID: 'CTP', MIN: 0, MAX: 1},
            {ID: 'G72', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
