from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B1', MIN: 1, MAX: 1},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'Y6', MIN: 0, MAX: 2},
    {ID: 'Y3', MIN: 1, MAX: 1},
    {ID: 'Y4', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'W09', MIN: 0, MAX: 1},
    ]},
    {ID: 'N9', MIN: 0, MAX: 100},
    {ID: 'R2A', MIN: 0, MAX: 25},
    {ID: 'N1', MIN: 0, MAX: 4, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 3},
    ]},
    {ID: 'R4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 15},
    ]},
    {ID: 'W09', MIN: 0, MAX: 1},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'EA', MIN: 0, MAX: 5},
    {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N7', MIN: 0, MAX: 1},
        {ID: 'W09', MIN: 0, MAX: 1},
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'L0', MIN: 0, MAX: 1},
        {ID: 'L5', MIN: 0, MAX: 1},
        {ID: 'L4', MIN: 0, MAX: 1},
        {ID: 'L1', MIN: 0, MAX: 1},
        {ID: 'H1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'H2', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'V1', MIN: 0, MAX: 2},
    {ID: 'V9', MIN: 0, MAX: 10},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
