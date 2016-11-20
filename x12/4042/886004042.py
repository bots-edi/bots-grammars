from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'UB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 2},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'ENT', MIN: 1, MAX: 5000, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'N1', MIN: 0, MAX: 150, LEVEL: [
            {ID: 'G32', MIN: 0, MAX: 25},
            {ID: 'G37', MIN: 0, MAX: 10},
            {ID: 'G28', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 10},
                {ID: 'G29', MIN: 0, MAX: 10},
                {ID: 'CTP', MIN: 0, MAX: 4},
                {ID: 'G35', MIN: 0, MAX: 10},
                {ID: 'CRC', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
