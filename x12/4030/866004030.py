from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SQ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSS', MIN: 1, MAX: 1},
    {ID: 'UIT', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'FOB', MIN: 0, MAX: 1},
    ]},
    {ID: 'DTM', MIN: 1, MAX: 100, LEVEL: [
        {ID: 'UIT', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'PID', MIN: 0, MAX: 1},
            {ID: 'OQS', MIN: 0, MAX: 1},
            {ID: 'SLN', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
                {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'MEA', MIN: 0, MAX: 10},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
