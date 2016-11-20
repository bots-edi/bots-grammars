from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'F01', MIN: 1, MAX: 1},
    {ID: 'L11', MIN: 0, MAX: 5},
    {ID: 'CUR', MIN: 0, MAX: 5},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 20},
    ]},
    {ID: 'F02', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 99},
        {ID: 'MAN', MIN: 0, MAX: 9999},
        {ID: 'F05', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 30},
        {ID: 'Q7', MIN: 0, MAX: 10},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'F09', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'F04', MIN: 0, MAX: 1},
            {ID: 'F05', MIN: 0, MAX: 10},
            {ID: 'NTE', MIN: 0, MAX: 9999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
