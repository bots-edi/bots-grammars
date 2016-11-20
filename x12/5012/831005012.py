from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 2},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'TRN', MIN: 0, MAX: 99999},
    {ID: 'QTY', MIN: 0, MAX: 10},
    {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
