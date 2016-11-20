from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B10', MIN: 1, MAX: 1},
    {ID: 'MS3', MIN: 0, MAX: 12},
    {ID: 'LX', MIN: 1, MAX: 999999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 999},
        {ID: 'MAN', MIN: 0, MAX: 9999},
        {ID: 'Q7', MIN: 0, MAX: 10},
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'AT5', MIN: 0, MAX: 10},
        {ID: 'AT8', MIN: 0, MAX: 10},
        {ID: 'AT7', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'MS1', MIN: 0, MAX: 1},
            {ID: 'MS2', MIN: 0, MAX: 2},
            {ID: 'K1', MIN: 0, MAX: 1},
            {ID: 'M7', MIN: 0, MAX: 1},
        ]},
        {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'G62', MIN: 0, MAX: 1},
            {ID: 'L11', MIN: 0, MAX: 10},
        ]},
        {ID: 'OID', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
