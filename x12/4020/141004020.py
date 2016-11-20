from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'WA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'QTY', MIN: 0, MAX: 3},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 4},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 8},
        {ID: 'PCS', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'RC', MIN: 0, MAX: 1},
    ]},
    {ID: 'TDS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'CUR', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
