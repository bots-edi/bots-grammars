from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BMP', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 5},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'QTY', MIN: 0, MAX: 1},
    {ID: 'BAL', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
