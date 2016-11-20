from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'UA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 3},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'ENT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'G53', MIN: 1, MAX: 1},
        {ID: 'DTM', MIN: 1, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'N1', MIN: 0, MAX: 100},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'G13', MIN: 0, MAX: 1},
        {ID: 'G18', MIN: 0, MAX: 30},
        {ID: 'G29', MIN: 0, MAX: 10},
        {ID: 'G30', MIN: 0, MAX: 10},
        {ID: 'SPR', MIN: 0, MAX: 1},
        {ID: 'RDI', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
