from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BMA', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 10},
    {ID: 'G62', MIN: 1, MAX: 1},
    {ID: 'G43', MIN: 0, MAX: 1000},
    {ID: 'G95', MIN: 0, MAX: 99},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'UIT', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 2},
            {ID: 'G62', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'N1', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'G95', MIN: 0, MAX: 5},
        {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'LIN', MIN: 1, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'G62', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
