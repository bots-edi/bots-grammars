from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'N9', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 99999},
        {ID: 'AMT', MIN: 1, MAX: 1},
        {ID: 'DFI', MIN: 1, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'PCT', MIN: 0, MAX: 1},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'DTM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 2},
            {ID: 'INT', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 2},
            {ID: 'III', MIN: 0, MAX: 99999},
        ]},
        {ID: 'FIS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'III', MIN: 0, MAX: 99999},
            {ID: 'AWD', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 1},
                {ID: 'III', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
