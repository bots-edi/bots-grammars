from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 1, MAX: 10},
    {ID: 'F9', MIN: 1, MAX: 1},
    {ID: 'D9', MIN: 1, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'H3', MIN: 0, MAX: 20},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'LET', MIN: 0, MAX: 150, LEVEL: [
        {ID: 'MEA', MIN: 1, MAX: 4},
        {ID: 'L4', MIN: 1, MAX: 75},
        {ID: 'N7', MIN: 0, MAX: 1},
        {ID: 'L10', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'LX', MIN: 1, MAX: 5, LEVEL: [
            {ID: 'NTE', MIN: 0, MAX: 10},
            {ID: 'L5', MIN: 0, MAX: 15},
        ]},
    ]},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
