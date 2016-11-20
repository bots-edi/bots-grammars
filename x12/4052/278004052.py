from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'TRN', MIN: 0, MAX: 9},
        {ID: 'AAA', MIN: 0, MAX: 9},
        {ID: 'UM', MIN: 0, MAX: 1},
        {ID: 'HCR', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'DTP', MIN: 0, MAX: 9},
        {ID: 'HI', MIN: 0, MAX: 1},
        {ID: 'SV1', MIN: 0, MAX: 1},
        {ID: 'SV2', MIN: 0, MAX: 1},
        {ID: 'SV3', MIN: 0, MAX: 1},
        {ID: 'TOO', MIN: 0, MAX: 32},
        {ID: 'HSD', MIN: 0, MAX: 1},
        {ID: 'CRC', MIN: 0, MAX: 9},
        {ID: 'CL1', MIN: 0, MAX: 1},
        {ID: 'CR1', MIN: 0, MAX: 1},
        {ID: 'CR2', MIN: 0, MAX: 1},
        {ID: 'CR4', MIN: 0, MAX: 1},
        {ID: 'CR5', MIN: 0, MAX: 1},
        {ID: 'CR6', MIN: 0, MAX: 1},
        {ID: 'CR7', MIN: 0, MAX: 1},
        {ID: 'CR8', MIN: 0, MAX: 1},
        {ID: 'PWK', MIN: 0, MAX: 99999},
        {ID: 'MSG', MIN: 0, MAX: 1},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'AAA', MIN: 0, MAX: 9},
            {ID: 'PRV', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'INS', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
