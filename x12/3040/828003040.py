from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BAU', MIN: 1, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'DAD', MIN: 1, MAX: 999990},
    {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'AMT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
