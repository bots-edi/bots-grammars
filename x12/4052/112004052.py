from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PQ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'SUP', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'K2', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'TXI', MIN: 0, MAX: 1},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SLN', MIN: 1, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
        ]},
        {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'PCT', MIN: 0, MAX: 1},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'MS1', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
        {ID: 'CID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
