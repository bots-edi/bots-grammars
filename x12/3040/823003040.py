from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'LB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'DEP', MIN: 1, MAX: 100, LEVEL: [
        {ID: 'AMT', MIN: 1, MAX: 1},
        {ID: 'QTY', MIN: 1, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'BAT', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'AVA', MIN: 0, MAX: 10},
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'BPS', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 5},
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'AVA', MIN: 0, MAX: 1},
                {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 12},
                    {ID: 'PER', MIN: 0, MAX: 3},
                ]},
                {ID: 'RMT', MIN: 0, MAX: 10000, LEVEL: [
                    {ID: 'N1', MIN: 0, MAX: 1},
                    {ID: 'CUR', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 5},
                    {ID: 'DTM', MIN: 0, MAX: 10},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
