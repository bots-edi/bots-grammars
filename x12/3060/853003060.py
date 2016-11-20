from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 1, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'TD5', MIN: 1, MAX: 200000, LEVEL: [
        {ID: 'TD3', MIN: 0, MAX: 12},
        {ID: 'TD4', MIN: 0, MAX: 5},
        {ID: 'NTE', MIN: 0, MAX: 100},
        {ID: 'REF', MIN: 0, MAX: 200},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'FK', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
