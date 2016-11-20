from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 5},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'LX', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 5},
        {ID: 'BLR', MIN: 0, MAX: 1},
        {ID: 'OID', MIN: 0, MAX: 99999},
        {ID: 'G62', MIN: 0, MAX: 2},
        {ID: 'MSI', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'AT9', MIN: 0, MAX: 1},
        ]},
        {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
