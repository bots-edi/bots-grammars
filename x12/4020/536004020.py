from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'LR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BR', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 20},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'LM', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'N1', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 10},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'CS', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'RCD', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'CON', MIN: 0, MAX: 99999},
        {ID: 'G62', MIN: 0, MAX: 50},
        {ID: 'CTP', MIN: 0, MAX: 10},
        {ID: 'G69', MIN: 0, MAX: 30},
        {ID: 'DD', MIN: 0, MAX: 100},
        {ID: 'LDT', MIN: 0, MAX: 3},
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'PKG', MIN: 0, MAX: 5},
        {ID: 'PWK', MIN: 0, MAX: 1},
        {ID: 'MSG', MIN: 0, MAX: 10},
        {ID: 'LM', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'N1', MIN: 0, MAX: 50, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'G61', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
