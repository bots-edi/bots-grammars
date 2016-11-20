from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 3},
    {ID: 'TRN', MIN: 0, MAX: 5},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'IN1', MIN: 0, MAX: 1},
        {ID: 'DMG', MIN: 0, MAX: 3},
        {ID: 'PRV', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'NX1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'TRN', MIN: 0, MAX: 1},
        {ID: 'STC', MIN: 0, MAX: 1},
        {ID: 'NM1', MIN: 0, MAX: 1},
        {ID: 'PRV', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'DTP', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CAT', MIN: 0, MAX: 1},
            {ID: 'PID', MIN: 0, MAX: 1},
            {ID: 'EFI', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'BIN', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
