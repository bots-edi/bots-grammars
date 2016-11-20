from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'CMA', MIN: 1, MAX: 1},
    {ID: 'DOS', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 1, MAX: 250, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'ASM', MIN: 0, MAX: 1},
    ]},
    {ID: 'MI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DOS', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CRC', MIN: 0, MAX: 1},
            {ID: 'PAI', MIN: 0, MAX: 60},
        ]},
    ]},
    {ID: 'QTY', MIN: 0, MAX: 1},
    {ID: 'AMT', MIN: 0, MAX: 2},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
