from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BLR', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 1},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'N1', MIN: 1, MAX: 999999, LEVEL: [
            {ID: 'GY', MIN: 0, MAX: 9999},
            {ID: 'N4', MIN: 0, MAX: 9999},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LX', MIN: 1, MAX: 999999, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 3},
                {ID: 'GY', MIN: 0, MAX: 9999},
                {ID: 'N4', MIN: 0, MAX: 9999},
                {ID: 'SV', MIN: 1, MAX: 1},
                {ID: 'RST', MIN: 0, MAX: 10},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
    ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 2},
        {ID: 'GY', MIN: 0, MAX: 9999},
        {ID: 'N4', MIN: 0, MAX: 9999},
        {ID: 'SV', MIN: 0, MAX: 1},
        {ID: 'RST', MIN: 0, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
