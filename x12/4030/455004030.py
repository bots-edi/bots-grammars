from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTC', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 1},
    {ID: 'ED', MIN: 0, MAX: 500000},
    {ID: 'BLR', MIN: 0, MAX: 5},
    {ID: 'N9', MIN: 0, MAX: 1},
    {ID: 'V9', MIN: 0, MAX: 99},
    {ID: 'LX', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'PRM', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'F9', MIN: 0, MAX: 1},
        {ID: 'D9', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
