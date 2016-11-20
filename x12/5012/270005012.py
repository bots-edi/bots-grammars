from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'TRN', MIN: 0, MAX: 9},
        {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'PRV', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'INS', MIN: 0, MAX: 1},
            {ID: 'HI', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'MPI', MIN: 0, MAX: 9},
            {ID: 'EQ', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 2},
                {ID: 'VEH', MIN: 0, MAX: 1},
                {ID: 'PDR', MIN: 0, MAX: 1},
                {ID: 'PDP', MIN: 0, MAX: 1},
                {ID: 'III', MIN: 0, MAX: 10},
                {ID: 'REF', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
