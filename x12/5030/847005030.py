from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MX',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'AMT', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 1, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 100},
        {ID: 'PID', MIN: 0, MAX: 5},
        {ID: 'QTY', MIN: 0, MAX: 10},
        {ID: 'MEA', MIN: 0, MAX: 10},
        {ID: 'SHP', MIN: 0, MAX: 5},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'PKG', MIN: 0, MAX: 5},
        {ID: 'CTP', MIN: 0, MAX: 10},
        {ID: 'SAC', MIN: 0, MAX: 10},
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'DTM', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
