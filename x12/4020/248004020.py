from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SU',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'NM1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 99999},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'NM1', MIN: 1, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'AIN', MIN: 0, MAX: 99999},
        {ID: 'EMS', MIN: 0, MAX: 99999},
        {ID: 'BAL', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'STC', MIN: 0, MAX: 99999},
            {ID: 'INT', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'ACT', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
