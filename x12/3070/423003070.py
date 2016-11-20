from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N2', MIN: 0, MAX: 1},
    {ID: 'N3', MIN: 0, MAX: 1},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 1},
    {ID: 'LX', MIN: 1, MAX: 150, LEVEL: [
        {ID: 'NTE', MIN: 0, MAX: 1},
        {ID: 'XD', MIN: 1, MAX: 10},
        {ID: 'N7', MIN: 1, MAX: 150, LEVEL: [
            {ID: 'XD', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 1},
            {ID: 'L5', MIN: 0, MAX: 5},
            {ID: 'D9', MIN: 0, MAX: 1},
            {ID: 'F9', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'LH2', MIN: 0, MAX: 2},
            {ID: 'LH6', MIN: 0, MAX: 6},
            {ID: 'LH1', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'LH2', MIN: 0, MAX: 4},
                {ID: 'LH3', MIN: 0, MAX: 10},
                {ID: 'LFH', MIN: 0, MAX: 20},
                {ID: 'LEP', MIN: 0, MAX: 3},
                {ID: 'LH4', MIN: 0, MAX: 1},
                {ID: 'LHT', MIN: 0, MAX: 3},
                {ID: 'LHR', MIN: 0, MAX: 5},
                {ID: 'PER', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
