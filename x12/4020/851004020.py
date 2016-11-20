from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'LS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BLS', MIN: 1, MAX: 1},
    {ID: 'MSG', MIN: 0, MAX: 100},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'TXI', MIN: 0, MAX: 7},
    {ID: 'TAX', MIN: 0, MAX: 5},
    {ID: 'PAM', MIN: 0, MAX: 100},
    {ID: 'ITA', MIN: 0, MAX: 35},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 1, MAX: 100000, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'LS1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'PO3', MIN: 0, MAX: 25},
        {ID: 'PID', MIN: 0, MAX: 1000},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'CTP', MIN: 0, MAX: 5},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'TXI', MIN: 0, MAX: 7},
        {ID: 'TAX', MIN: 0, MAX: 5},
        {ID: 'PAM', MIN: 0, MAX: 25},
        {ID: 'ITA', MIN: 0, MAX: 35},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'AMT', MIN: 0, MAX: 5},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'TXI', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'AMT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
