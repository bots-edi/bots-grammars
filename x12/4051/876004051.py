from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'OG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'G92', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 50},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'G66', MIN: 0, MAX: 1},
    {ID: 'G23', MIN: 0, MAX: 20},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'G72', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'G73', MIN: 0, MAX: 10},
    ]},
    {ID: 'G68', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'G69', MIN: 0, MAX: 5},
        {ID: 'G70', MIN: 0, MAX: 2},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'G23', MIN: 0, MAX: 20},
        {ID: 'G72', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'G73', MIN: 0, MAX: 10},
        ]},
        {ID: 'N1', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 10},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'G72', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'G76', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
