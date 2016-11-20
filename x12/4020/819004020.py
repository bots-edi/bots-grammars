from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'JB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BOS', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 5},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'MSG', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'JIL', MIN: 1, MAX: 10000, LEVEL: [
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'MSG', MIN: 0, MAX: 12},
        {ID: 'MEA', MIN: 0, MAX: 10},
        {ID: 'ITA', MIN: 0, MAX: 10},
        {ID: 'PSA', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'JID', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'MSG', MIN: 0, MAX: 12},
            {ID: 'MEA', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'AMT', MIN: 1, MAX: 1},
    {ID: 'QTY', MIN: 0, MAX: 5},
    {ID: 'TDS', MIN: 0, MAX: 1},
    {ID: 'PSA', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
