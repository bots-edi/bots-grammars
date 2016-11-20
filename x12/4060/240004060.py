from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MZ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 1},
        ]},
        {ID: 'EFI', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'BIN', MIN: 1, MAX: 1},
        ]},
        {ID: 'L11', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'MS2', MIN: 0, MAX: 99999},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'MAN', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'L11', MIN: 0, MAX: 99999},
                    {ID: 'AT7', MIN: 0, MAX: 99999},
                    {ID: 'CD3', MIN: 0, MAX: 99999},
                    {ID: 'NM1', MIN: 0, MAX: 1},
                    {ID: 'Q7', MIN: 0, MAX: 99999},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
            {ID: 'EFI', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'BIN', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
