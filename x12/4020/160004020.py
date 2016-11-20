from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BAX', MIN: 1, MAX: 1},
    {ID: 'AES', MIN: 1, MAX: 1},
    {ID: 'YNQ', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'QTY', MIN: 0, MAX: 5},
    {ID: 'MEA', MIN: 0, MAX: 10},
    {ID: 'AEI', MIN: 0, MAX: 16},
    {ID: 'EI', MIN: 1, MAX: 500, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 20},
        {ID: 'MEA', MIN: 0, MAX: 20},
        {ID: 'DTM', MIN: 0, MAX: 20},
        {ID: 'TSI', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'YNQ', MIN: 0, MAX: 25},
            {ID: 'LQ', MIN: 0, MAX: 25},
            {ID: 'QTY', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 2},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
