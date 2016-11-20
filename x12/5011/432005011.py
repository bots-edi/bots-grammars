from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RX',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'BLR', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'DTM', MIN: 0, MAX: 6},
    {ID: 'QTY', MIN: 0, MAX: 1},
    {ID: 'LX', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 0, MAX: 8},
        {ID: 'DRT', MIN: 0, MAX: 6},
        {ID: 'CIC', MIN: 1, MAX: 1500, LEVEL: [
            {ID: 'DRT', MIN: 0, MAX: 12},
            {ID: 'QTY', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
