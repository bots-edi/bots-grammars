from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'PAM', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'GRI', MIN: 1, MAX: 100000, LEVEL: [
        {ID: 'PAM', MIN: 0, MAX: 99999},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'ICH', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
