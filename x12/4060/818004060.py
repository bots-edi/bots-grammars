from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSC', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N11', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'AMT', MIN: 0, MAX: 5},
        {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 5},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'SCD', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 5},
            {ID: 'SAL', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'AMT', MIN: 1, MAX: 10},
            ]},
            {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'PID', MIN: 0, MAX: 5},
                {ID: 'AMT', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
