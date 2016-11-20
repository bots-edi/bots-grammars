from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CU',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'DTM', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'LQ', MIN: 0, MAX: 99999},
        {ID: 'LCD', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'CS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 99999},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 0, MAX: 99999},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LCD', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'LQ', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
