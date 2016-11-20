from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTI', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
    ]},
    {ID: 'TFS', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'TIA', MIN: 0, MAX: 99999},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
