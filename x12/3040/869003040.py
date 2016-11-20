from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSI', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'HL', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'PRF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'PID', MIN: 0, MAX: 1000},
        {ID: 'MEA', MIN: 0, MAX: 40},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
