from bots.botsconfig import *
from records004040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 5},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'G01', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'QTY', MIN: 1, MAX: 4},
        {ID: 'AMT', MIN: 1, MAX: 2},
        {ID: 'G72', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'G73', MIN: 0, MAX: 1},
        ]},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 2},
                {ID: 'AMT', MIN: 0, MAX: 1},
                {ID: 'G72', MIN: 0, MAX: 1},
                {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'AMT', MIN: 0, MAX: 1},
                    {ID: 'LIN', MIN: 0, MAX: 1},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'G72', MIN: 0, MAX: 1},
                    {ID: 'G73', MIN: 0, MAX: 5},
                ]},
            ]},
        ]},
    ]},
    {ID: 'LX', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'QTY', MIN: 1, MAX: 1},
        {ID: 'AMT', MIN: 1, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
