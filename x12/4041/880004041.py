from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'G01', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 5},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'G27', MIN: 0, MAX: 5},
    {ID: 'G23', MIN: 0, MAX: 20},
    {ID: 'G25', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'G72', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'G73', MIN: 0, MAX: 10},
    ]},
    {ID: 'G17', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'G69', MIN: 0, MAX: 5},
        {ID: 'G19', MIN: 0, MAX: 10},
        {ID: 'G20', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 5},
        {ID: 'G23', MIN: 0, MAX: 20},
        {ID: 'G25', MIN: 0, MAX: 1},
        {ID: 'G72', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'G73', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'ENT', MIN: 0, MAX: 500, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 5},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 2},
            {ID: 'G72', MIN: 0, MAX: 1},
            {ID: 'G17', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'G19', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'G31', MIN: 1, MAX: 1},
    {ID: 'G33', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
