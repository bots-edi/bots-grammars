from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'ENR', MIN: 0, MAX: 1},
    {ID: 'ERP', MIN: 0, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 2},
    {ID: 'SST', MIN: 0, MAX: 1},
    {ID: 'SUM', MIN: 0, MAX: 6},
    {ID: 'N1', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'ENT', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'IN2', MIN: 0, MAX: 5},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'SES', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'SUM', MIN: 0, MAX: 6},
        {ID: 'ENR', MIN: 0, MAX: 1},
        {ID: 'FOS', MIN: 0, MAX: 5},
        {ID: 'NTE', MIN: 0, MAX: 100},
    ]},
    {ID: 'DEG', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'FOS', MIN: 0, MAX: 2},
        {ID: 'NTE', MIN: 0, MAX: 100},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
