from bots.botsconfig import *
from records004040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'EX',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2},
    {ID: 'REF', MIN: 0, MAX: 1},
    {ID: 'EXI', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 4},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'NX2', MIN: 0, MAX: 99999},
        {ID: 'PPA', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'MSG', MIN: 0, MAX: 2},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'LIE', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PPA', MIN: 1, MAX: 99999},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
