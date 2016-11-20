from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BA1', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'YNQ', MIN: 1, MAX: 10},
        {ID: 'V5', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 1, MAX: 1},
        {ID: 'P5', MIN: 1, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'M12', MIN: 0, MAX: 1},
        {ID: 'VID', MIN: 0, MAX: 999},
        {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'L13', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'MAN', MIN: 0, MAX: 999},
            {ID: 'X1', MIN: 0, MAX: 1},
            {ID: 'VEH', MIN: 0, MAX: 9999},
            {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
