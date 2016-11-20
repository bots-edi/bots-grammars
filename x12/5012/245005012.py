from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LN', MIN: 0, MAX: 1},
        {ID: 'MLA', MIN: 0, MAX: 1},
        {ID: 'ASM', MIN: 0, MAX: 1},
        {ID: 'TA', MIN: 0, MAX: 1},
        {ID: 'PTS', MIN: 0, MAX: 1},
        {ID: 'TII', MIN: 0, MAX: 1},
        {ID: 'INC', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
        ]},
        {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 0, MAX: 99999},
            {ID: 'PDS', MIN: 0, MAX: 99999},
            {ID: 'PDE', MIN: 0, MAX: 1},
            {ID: 'TIA', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'TDT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
