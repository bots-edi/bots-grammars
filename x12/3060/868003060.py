from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'E01', MIN: 1, MAX: 1},
    {ID: 'DMI', MIN: 0, MAX: 100},
    {ID: 'E03', MIN: 0, MAX: 100},
    {ID: 'MSG', MIN: 0, MAX: 1000},
    {ID: 'E10', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'E13', MIN: 0, MAX: 1000},
    ]},
    {ID: 'E20', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'E22', MIN: 0, MAX: 100},
        {ID: 'E24', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'E26', MIN: 0, MAX: 100},
        ]},
    ]},
    {ID: 'E30', MIN: 0, MAX: 2000, LEVEL: [
        {ID: 'DAI', MIN: 0, MAX: 10},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'E34', MIN: 0, MAX: 100000, LEVEL: [
            {ID: 'DDI', MIN: 0, MAX: 20},
            {ID: 'DAI', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'E40', MIN: 0, MAX: 10000, LEVEL: [
        {ID: 'DMI', MIN: 0, MAX: 100},
        {ID: 'DDI', MIN: 0, MAX: 1000},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
