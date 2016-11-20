from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCQ', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'PI', MIN: 0, MAX: 3},
    {ID: 'LQ', MIN: 0, MAX: 3},
    {ID: 'QTY', MIN: 0, MAX: 3},
    {ID: 'NTE', MIN: 0, MAX: 3},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'N9', MIN: 0, MAX: 20},
    ]},
    {ID: 'LX', MIN: 1, MAX: 31, LEVEL: [
        {ID: 'D9', MIN: 0, MAX: 1},
        {ID: 'F9', MIN: 1, MAX: 31, LEVEL: [
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'R2', MIN: 0, MAX: 13},
            {ID: 'SCR', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'GA', MIN: 0, MAX: 15},
                {ID: 'DTM', MIN: 1, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 3},
                {ID: 'YNQ', MIN: 0, MAX: 20},
                {ID: 'N9', MIN: 0, MAX: 20},
                {ID: 'PI', MIN: 0, MAX: 3},
                {ID: 'LQ', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'N9', MIN: 0, MAX: 20},
                ]},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'N7', MIN: 1, MAX: 9999, LEVEL: [
                        {ID: 'SCR', MIN: 0, MAX: 1},
                        {ID: 'PI', MIN: 0, MAX: 5},
                        {ID: 'DTM', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
