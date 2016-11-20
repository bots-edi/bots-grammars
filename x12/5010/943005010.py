from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'W06', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 5},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'W27', MIN: 1, MAX: 1},
    {ID: 'W28', MIN: 0, MAX: 1},
    {ID: 'W10', MIN: 0, MAX: 1},
    {ID: 'W04', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'G69', MIN: 0, MAX: 5},
        {ID: 'N9', MIN: 0, MAX: 200},
        {ID: 'W20', MIN: 0, MAX: 2},
    ]},
    {ID: 'W03', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
