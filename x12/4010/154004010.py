from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'UC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DAD', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'NM1', MIN: 0, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'LS1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'PO3', MIN: 0, MAX: 25},
        {ID: 'PID', MIN: 0, MAX: 1000},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'PAM', MIN: 0, MAX: 25},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'AMT', MIN: 0, MAX: 5},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
