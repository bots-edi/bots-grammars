from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSW', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'CI', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 2},
            {ID: 'SWC', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'ED', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 5},
                    {ID: 'SWD', MIN: 0, MAX: 1},
                    {ID: 'SWR', MIN: 0, MAX: 2},
                    {ID: 'NM1', MIN: 0, MAX: 1},
                    {ID: 'F9', MIN: 0, MAX: 1},
                    {ID: 'D9', MIN: 0, MAX: 1},
                    {ID: 'NTE', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
