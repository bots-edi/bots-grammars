from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'GR', MIN: 1, MAX: 1},
    {ID: 'SLI', MIN: 1, MAX: 1},
    {ID: 'DEF', MIN: 0, MAX: 1},
    {ID: 'DB', MIN: 0, MAX: 10},
    {ID: 'DTP', MIN: 0, MAX: 5},
    {ID: 'AMT', MIN: 0, MAX: 5},
    {ID: 'ENT', MIN: 1, MAX: 6, LEVEL: [
        {ID: 'IN2', MIN: 0, MAX: 5},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'DMA', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 3},
        {ID: 'ENR', MIN: 0, MAX: 1},
        {ID: 'IN1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 5},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
