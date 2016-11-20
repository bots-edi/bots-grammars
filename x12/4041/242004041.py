from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'IRP', MIN: 0, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 10},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'MSG', MIN: 0, MAX: 1},
    {ID: 'HL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'IIS', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 10},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'STS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'QTY', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
