from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PK',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCM', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 99999},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'CRT', MIN: 0, MAX: 1},
        {ID: 'BSD', MIN: 0, MAX: 1},
        {ID: 'CLI', MIN: 0, MAX: 1},
        {ID: 'CAL', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'RPA', MIN: 0, MAX: 99999},
        {ID: 'PCT', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'PD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PDD', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
