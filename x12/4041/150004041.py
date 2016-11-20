from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N2', MIN: 0, MAX: 2},
    {ID: 'N3', MIN: 0, MAX: 2},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 2},
    {ID: 'DTP', MIN: 0, MAX: 1},
    {ID: 'TFS', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'MTX', MIN: 0, MAX: 1},
        {ID: 'TRS', MIN: 1, MAX: 100000, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'QTY', MIN: 0, MAX: 10},
            {ID: 'N1', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'FGS', MIN: 1, MAX: 1000, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'TRS', MIN: 1, MAX: 100000, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 10},
                {ID: 'N1', MIN: 0, MAX: 1000, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
