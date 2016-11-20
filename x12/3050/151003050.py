from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTA', MIN: 1, MAX: 1},
    {ID: 'BTI', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'PBI', MIN: 0, MAX: 1000},
    {ID: 'TFS', MIN: 0, MAX: 100000, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 10},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'PBI', MIN: 0, MAX: 1000},
        {ID: 'FGS', MIN: 0, MAX: 100000, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'PBI', MIN: 0, MAX: 1000},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
