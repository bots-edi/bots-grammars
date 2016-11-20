from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'GR', MIN: 1, MAX: 1},
    {ID: 'DB', MIN: 0, MAX: 10},
    {ID: 'LM', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 10},
    ]},
    {ID: 'ENT', MIN: 1, MAX: 6, LEVEL: [
        {ID: 'IN2', MIN: 0, MAX: 5},
        {ID: 'IDB', MIN: 0, MAX: 10},
        {ID: 'DTP', MIN: 0, MAX: 1},
    ]},
    {ID: 'AMT', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
