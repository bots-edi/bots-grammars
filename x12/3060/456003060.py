from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'EI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'EIA', MIN: 1, MAX: 1},
    {ID: 'LX', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'N7', MIN: 0, MAX: 1},
        {ID: 'H5', MIN: 0, MAX: 1},
        {ID: 'G4', MIN: 0, MAX: 1},
        {ID: 'G5', MIN: 0, MAX: 1},
        {ID: 'IC', MIN: 0, MAX: 2},
        {ID: 'N8', MIN: 0, MAX: 1},
        {ID: 'F9', MIN: 0, MAX: 1},
        {ID: 'D9', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99},
        {ID: 'N1', MIN: 0, MAX: 999999},
        {ID: 'H3', MIN: 0, MAX: 20},
        {ID: 'L5', MIN: 0, MAX: 15},
        {ID: 'R2', MIN: 0, MAX: 13},
        {ID: 'IS1', MIN: 0, MAX: 1},
        {ID: 'ISC', MIN: 0, MAX: 99},
        {ID: 'IS2', MIN: 0, MAX: 99},
        {ID: 'VC', MIN: 0, MAX: 21, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 2},
        ]},
        {ID: 'S1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'S9', MIN: 0, MAX: 3},
        ]},
        {ID: 'ER', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'NA', MIN: 0, MAX: 1},
            {ID: 'IC', MIN: 0, MAX: 3},
            {ID: 'ES', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
