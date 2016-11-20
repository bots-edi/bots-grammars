from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'CDS', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 99999},
        {ID: 'SPI', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'BCU', MIN: 0, MAX: 1},
        {ID: 'CED', MIN: 0, MAX: 1},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 0, MAX: 99999},
        ]},
        {ID: 'BBC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 1},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 99999},
            {ID: 'N3', MIN: 0, MAX: 99999},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
        {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'BIN', MIN: 1, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
