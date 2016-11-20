from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'OTI', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 9},
        {ID: 'TED', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NTE', MIN: 0, MAX: 100},
            {ID: 'RED', MIN: 0, MAX: 100},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100, LEVEL: [
                {ID: 'RED', MIN: 0, MAX: 100},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
