from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B13', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'H6', MIN: 0, MAX: 5},
    {ID: 'N7', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'N9', MIN: 0, MAX: 999},
    {ID: 'H3', MIN: 0, MAX: 10},
    {ID: 'G05', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'G61', MIN: 0, MAX: 5},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'OID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'S5', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'H6', MIN: 0, MAX: 5},
        {ID: 'G61', MIN: 0, MAX: 5},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'OID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
