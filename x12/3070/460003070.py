from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'REN', MIN: 1, MAX: 1},
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'PI', MIN: 0, MAX: 8},
    {ID: 'PR', MIN: 0, MAX: 200},
    {ID: 'SS', MIN: 0, MAX: 1},
    {ID: 'SA', MIN: 0, MAX: 1},
    {ID: 'CD', MIN: 0, MAX: 150},
    {ID: 'RAB', MIN: 0, MAX: 48},
    {ID: 'PT', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'SB', MIN: 1, MAX: 50, LEVEL: [
        {ID: 'GY', MIN: 0, MAX: 150},
        {ID: 'SC', MIN: 1, MAX: 300, LEVEL: [
            {ID: 'GY', MIN: 0, MAX: 150},
            {ID: 'CD', MIN: 0, MAX: 150},
            {ID: 'RAB', MIN: 0, MAX: 48},
            {ID: 'LX', MIN: 1, MAX: 60, LEVEL: [
                {ID: 'RS', MIN: 1, MAX: 2},
                {ID: 'RD', MIN: 0, MAX: 25},
                {ID: 'R9', MIN: 0, MAX: 2, LEVEL: [
                    {ID: 'FK', MIN: 0, MAX: 13},
                    {ID: 'R2B', MIN: 0, MAX: 13, LEVEL: [
                        {ID: 'R2C', MIN: 0, MAX: 25},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
