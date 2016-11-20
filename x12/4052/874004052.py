from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CQ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'III', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'LCD', MIN: 0, MAX: 1},
        {ID: 'CS', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'III', MIN: 0, MAX: 99999},
        {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'III', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
