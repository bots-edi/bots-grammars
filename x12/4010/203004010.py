from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 4},
        {ID: 'MPP', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 10},
        {ID: 'INT', MIN: 0, MAX: 2},
        {ID: 'QTY', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'RLT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 1, MAX: 3},
            {ID: 'AMT', MIN: 1, MAX: 8},
            {ID: 'IRA', MIN: 0, MAX: 1},
            {ID: 'INT', MIN: 0, MAX: 2},
            {ID: 'PRC', MIN: 0, MAX: 3},
            {ID: 'NX2', MIN: 0, MAX: 10},
            {ID: 'LQ', MIN: 0, MAX: 5},
            {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 2},
                {ID: 'YNQ', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
