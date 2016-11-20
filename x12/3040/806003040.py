from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BPP', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 100},
    {ID: 'CAL', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 100},
        {ID: 'DTM', MIN: 0, MAX: 10000},
    ]},
    {ID: 'TID', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 50},
        {ID: 'DTM', MIN: 0, MAX: 50},
        {ID: 'QTY', MIN: 0, MAX: 100},
        {ID: 'AMT', MIN: 0, MAX: 100},
        {ID: 'PCT', MIN: 0, MAX: 100},
        {ID: 'RES', MIN: 0, MAX: 100},
        {ID: 'MIL', MIN: 0, MAX: 1000},
        {ID: 'MSG', MIN: 0, MAX: 1000},
    ]},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'DTM', MIN: 0, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
