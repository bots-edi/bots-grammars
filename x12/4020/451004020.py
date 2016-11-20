from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'EV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ER', MIN: 0, MAX: 2},
    {ID: 'ED', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'ER', MIN: 0, MAX: 2},
        {ID: 'NA', MIN: 0, MAX: 1},
        {ID: 'IC', MIN: 0, MAX: 3},
        {ID: 'CLR', MIN: 0, MAX: 10},
        {ID: 'ES', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
