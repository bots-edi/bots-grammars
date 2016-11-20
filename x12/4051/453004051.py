from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ST',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'SSC', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 1, MAX: 2},
    {ID: 'N1', MIN: 0, MAX: 999999},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'OD', MIN: 0, MAX: 1},
    {ID: 'PI', MIN: 0, MAX: 10},
    {ID: 'PR', MIN: 0, MAX: 99},
    {ID: 'CT', MIN: 0, MAX: 99},
    {ID: 'APR', MIN: 0, MAX: 99},
    {ID: 'SHR', MIN: 0, MAX: 99},
    {ID: 'SR', MIN: 0, MAX: 7, LEVEL: [
        {ID: 'LX', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'ISD', MIN: 0, MAX: 15},
            {ID: 'ISC', MIN: 0, MAX: 999999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
