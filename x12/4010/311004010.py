from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'Y6', MIN: 0, MAX: 2},
    {ID: 'N9', MIN: 1, MAX: 10},
    {ID: 'V1', MIN: 0, MAX: 1},
    {ID: 'V2', MIN: 0, MAX: 1},
    {ID: 'V3', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 2},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'R4', MIN: 1, MAX: 10},
    {ID: 'K1', MIN: 0, MAX: 5},
    {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'Y2', MIN: 0, MAX: 10},
        {ID: 'ED', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'NA', MIN: 0, MAX: 1},
            {ID: 'L4', MIN: 0, MAX: 1},
            {ID: 'G2', MIN: 0, MAX: 1},
        ]},
        {ID: 'L0', MIN: 0, MAX: 120, LEVEL: [
            {ID: 'L5', MIN: 1, MAX: 999},
            {ID: 'L4', MIN: 0, MAX: 1},
            {ID: 'X1', MIN: 0, MAX: 5},
            {ID: 'X2', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'L3', MIN: 0, MAX: 1},
    {ID: 'K1', MIN: 0, MAX: 2},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
