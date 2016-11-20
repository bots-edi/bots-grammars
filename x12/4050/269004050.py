from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'TRN', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'CLP', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 2},
        {ID: 'AAA', MIN: 0, MAX: 1},
        {ID: 'NM1', MIN: 0, MAX: 4, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 1},
        ]},
        {ID: 'SVC', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
