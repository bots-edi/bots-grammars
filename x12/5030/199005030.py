from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 12},
        {ID: 'LRQ', MIN: 0, MAX: 1},
        {ID: 'LN1', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'III', MIN: 0, MAX: 5},
        {ID: 'NTE', MIN: 0, MAX: 99999},
        {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 0, MAX: 30},
            {ID: 'PDS', MIN: 0, MAX: 20},
            {ID: 'PDE', MIN: 0, MAX: 99999},
        ]},
        {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 30},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 4},
        ]},
        {ID: 'FGS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'YNQ', MIN: 0, MAX: 1},
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'NTE', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 2},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'PCT', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
