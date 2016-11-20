from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'G42', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 99999},
    {ID: 'G62', MIN: 1, MAX: 50},
    {ID: 'NTE', MIN: 0, MAX: 300},
    {ID: 'G43', MIN: 0, MAX: 1000},
    {ID: 'G23', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 99999},
    ]},
    {ID: 'G94', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'G95', MIN: 0, MAX: 99},
    ]},
    {ID: 'LX', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'G46', MIN: 0, MAX: 20},
        {ID: 'G51', MIN: 0, MAX: 1},
        {ID: 'G94', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'G95', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'G62', MIN: 0, MAX: 2},
            ]},
        ]},
        {ID: 'G45', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'G69', MIN: 0, MAX: 5},
            {ID: 'G43', MIN: 0, MAX: 9999},
            {ID: 'G51', MIN: 0, MAX: 10},
            {ID: 'G23', MIN: 0, MAX: 1},
            {ID: 'G62', MIN: 0, MAX: 10},
            {ID: 'G22', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
