from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSS', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'FOB', MIN: 0, MAX: 1},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'UIT', MIN: 1, MAX: 1},
        {ID: 'PKG', MIN: 0, MAX: 99999},
        {ID: 'PO4', MIN: 0, MAX: 99999},
        {ID: 'PRS', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'SDP', MIN: 0, MAX: 1},
        {ID: 'FST', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'SDQ', MIN: 0, MAX: 99999},
            {ID: 'JIT', MIN: 0, MAX: 96, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 500},
                {ID: 'DTM', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'SHP', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 12},
        ]},
        {ID: 'TD1', MIN: 0, MAX: 1},
        {ID: 'TD3', MIN: 0, MAX: 1},
        {ID: 'TD5', MIN: 0, MAX: 1},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
