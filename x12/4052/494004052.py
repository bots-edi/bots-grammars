from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'REN', MIN: 1, MAX: 1},
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'PI', MIN: 1, MAX: 8},
    {ID: 'PR', MIN: 0, MAX: 200},
    {ID: 'SS', MIN: 0, MAX: 1},
    {ID: 'SA', MIN: 1, MAX: 1},
    {ID: 'CD', MIN: 0, MAX: 150},
    {ID: 'GY', MIN: 0, MAX: 150},
    {ID: 'RAB', MIN: 0, MAX: 12},
    {ID: 'PT', MIN: 0, MAX: 50},
    {ID: 'LX', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PI', MIN: 0, MAX: 15},
    ]},
    {ID: 'R9', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'R2B', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'R2C', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SCL', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'RD', MIN: 0, MAX: 6},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
