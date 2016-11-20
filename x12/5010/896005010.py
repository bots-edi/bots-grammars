from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'G43', MIN: 0, MAX: 200},
    {ID: 'ID1', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'ID2', MIN: 0, MAX: 1},
        {ID: 'ID3', MIN: 0, MAX: 50},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
