from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B11', MIN: 1, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'L10', MIN: 0, MAX: 5},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 10},
    ]},
    {ID: 'K2', MIN: 0, MAX: 2},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
