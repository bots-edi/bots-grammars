from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'IS1', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 1, MAX: 5},
    {ID: 'ISC', MIN: 0, MAX: 99999},
    {ID: 'N8', MIN: 0, MAX: 1},
    {ID: 'IS2', MIN: 1, MAX: 99999},
    {ID: 'F9', MIN: 0, MAX: 1},
    {ID: 'D9', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 10},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'L5', MIN: 0, MAX: 5},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'H5', MIN: 0, MAX: 1},
    {ID: 'IC', MIN: 0, MAX: 1},
    {ID: 'IMA', MIN: 0, MAX: 1},
    {ID: 'PS', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'N8A', MIN: 0, MAX: 25},
    {ID: 'S1', MIN: 0, MAX: 12, LEVEL: [
        {ID: 'S9', MIN: 0, MAX: 1},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LH1', MIN: 1, MAX: 1000, LEVEL: [
            {ID: 'LH2', MIN: 0, MAX: 4},
            {ID: 'LH3', MIN: 0, MAX: 10},
            {ID: 'LFH', MIN: 0, MAX: 20},
            {ID: 'LEP', MIN: 0, MAX: 3},
            {ID: 'LH4', MIN: 0, MAX: 1},
            {ID: 'LHT', MIN: 0, MAX: 3},
            {ID: 'LHR', MIN: 0, MAX: 5},
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 2},
            ]},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'PER', MIN: 0, MAX: 5},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
