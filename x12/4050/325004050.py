from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B12', MIN: 1, MAX: 1},
    {ID: 'M7', MIN: 0, MAX: 5},
    {ID: 'W09', MIN: 0, MAX: 1},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'V1', MIN: 1, MAX: 1},
    {ID: 'V9', MIN: 0, MAX: 2},
    {ID: 'L3', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'R4', MIN: 1, MAX: 4},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'MBL', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'L3', MIN: 0, MAX: 1},
        {ID: 'C3', MIN: 0, MAX: 1},
        {ID: 'R4', MIN: 0, MAX: 4},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'N1', MIN: 0, MAX: 6, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'LIN', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'SN1', MIN: 1, MAX: 1},
            {ID: 'PRF', MIN: 0, MAX: 1},
            {ID: 'TD1', MIN: 1, MAX: 1},
            {ID: 'H1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'H2', MIN: 0, MAX: 10},
            ]},
            {ID: 'G20', MIN: 0, MAX: 1},
            {ID: 'MAN', MIN: 0, MAX: 10},
            {ID: 'UIT', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'L8', MIN: 0, MAX: 1},
            {ID: 'C3', MIN: 0, MAX: 1},
            {ID: 'R4', MIN: 0, MAX: 4},
            {ID: 'N9', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
