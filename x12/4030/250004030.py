from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'SSD', MIN: 0, MAX: 999999},
    {ID: 'PRF', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'G05', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'H3', MIN: 0, MAX: 6},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'G05', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
