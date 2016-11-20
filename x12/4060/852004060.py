from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'XQ', MIN: 1, MAX: 1},
    {ID: 'XPO', MIN: 0, MAX: 99999},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'TD5', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'CTP', MIN: 0, MAX: 25},
        {ID: 'SAC', MIN: 0, MAX: 99999},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 10},
        {ID: 'PAL', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'ZA', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'CTP', MIN: 0, MAX: 25},
            {ID: 'SDQ', MIN: 0, MAX: 99999},
            {ID: 'G95', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 2},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
