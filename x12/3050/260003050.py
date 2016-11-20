from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 7, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'CSI', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'NM1', MIN: 1, MAX: 2},
        {ID: 'REF', MIN: 1, MAX: 6},
        {ID: 'N3', MIN: 1, MAX: 1},
        {ID: 'N4', MIN: 1, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 2},
        {ID: 'INT', MIN: 0, MAX: 10},
        {ID: 'MIR', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
        {ID: 'PCT', MIN: 0, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 30},
        {ID: 'DFI', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'DTP', MIN: 1, MAX: 19},
            {ID: 'AMT', MIN: 1, MAX: 4},
        ]},
        {ID: 'REC', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 2},
            {ID: 'DTP', MIN: 0, MAX: 4},
            {ID: 'FCL', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'FIS', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'MSG', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
