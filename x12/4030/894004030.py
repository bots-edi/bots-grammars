from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DX',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'G82', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'G83', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'G22', MIN: 0, MAX: 1},
            {ID: 'G72', MIN: 0, MAX: 10},
            {ID: 'G23', MIN: 0, MAX: 20},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'G72', MIN: 0, MAX: 20},
    {ID: 'G23', MIN: 0, MAX: 20},
    {ID: 'G84', MIN: 1, MAX: 1},
    {ID: 'G86', MIN: 1, MAX: 1},
    {ID: 'G85', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
