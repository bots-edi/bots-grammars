from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MQ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B3A', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'L11', MIN: 0, MAX: 5},
    ]},
    {ID: 'N7', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'M7', MIN: 0, MAX: 5},
    ]},
    {ID: 'LX', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'CSD', MIN: 1, MAX: 5},
        {ID: 'SPO', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
        {ID: 'N1', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'L11', MIN: 0, MAX: 10},
            {ID: 'CSD', MIN: 0, MAX: 20},
            {ID: 'SPO', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'SDQ', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
