from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 2},
    ]},
    {ID: 'G39', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'G69', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'RCR', MIN: 0, MAX: 99999},
        {ID: 'G43', MIN: 0, MAX: 99999},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
