from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 10},
        {ID: 'THE', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 20},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'LUI', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 1},
            {ID: 'LQ', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'LQ', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'PCT', MIN: 0, MAX: 1},
                    {ID: 'AMT', MIN: 0, MAX: 1},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'G63', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 2},
                {ID: 'REF', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'PCT', MIN: 0, MAX: 1},
                    {ID: 'AMT', MIN: 0, MAX: 1},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
