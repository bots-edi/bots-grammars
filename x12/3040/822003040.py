from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 3},
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N2', MIN: 0, MAX: 2},
    {ID: 'N3', MIN: 0, MAX: 2},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'RTE', MIN: 0, MAX: 13, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 500, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'ACT', MIN: 0, MAX: 5000, LEVEL: [
            {ID: 'ADJ', MIN: 0, MAX: 1000},
            {ID: 'RTE', MIN: 0, MAX: 13, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'BAL', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 25},
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'SER', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'CTP', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
