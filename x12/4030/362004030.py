from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'OC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 1, MAX: 9},
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N2', MIN: 0, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 1},
    {ID: 'L5', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 20},
        {ID: 'DTP', MIN: 1, MAX: 9},
        {ID: 'V1', MIN: 1, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 9},
        {ID: 'R1', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'PCT', MIN: 0, MAX: 1},
        {ID: 'R4', MIN: 1, MAX: 5, LEVEL: [
            {ID: 'NX2', MIN: 0, MAX: 20},
        ]},
        {ID: 'AMT', MIN: 1, MAX: 9, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PCT', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
