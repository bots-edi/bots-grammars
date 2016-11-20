from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSI', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'PRF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'LIN', MIN: 0, MAX: 99999},
        {ID: 'PID', MIN: 0, MAX: 1000},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'DD', MIN: 0, MAX: 99999},
        {ID: 'GF', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
