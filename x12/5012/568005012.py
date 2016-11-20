from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'D5',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'AMT', MIN: 1, MAX: 2},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'CS', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 1, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
                ]},
                {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'N9', MIN: 0, MAX: 2},
                ]},
            ]},
            {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'FA2', MIN: 1, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'BAL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'RTE', MIN: 0, MAX: 99999},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
