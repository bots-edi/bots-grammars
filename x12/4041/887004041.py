from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 4},
    {ID: 'AMT', MIN: 0, MAX: 7},
    {ID: 'G43', MIN: 0, MAX: 500},
    {ID: 'N9', MIN: 0, MAX: 5},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'DTM', MIN: 0, MAX: 2},
    {ID: 'G11', MIN: 0, MAX: 10},
    {ID: 'G12', MIN: 0, MAX: 1},
    {ID: 'G14', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'G15', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 20},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'PCT', MIN: 0, MAX: 1},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'G28', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'PCT', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 3},
            {ID: 'G51', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
