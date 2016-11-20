from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BAX', MIN: 1, MAX: 1},
    {ID: 'W1', MIN: 1, MAX: 30, LEVEL: [
        {ID: 'W2', MIN: 1, MAX: 400, LEVEL: [
            {ID: 'W3', MIN: 0, MAX: 7},
            {ID: 'IMA', MIN: 0, MAX: 3},
            {ID: 'W4', MIN: 0, MAX: 1},
            {ID: 'W5', MIN: 0, MAX: 4},
            {ID: 'W6', MIN: 0, MAX: 6},
            {ID: 'PS', MIN: 0, MAX: 5},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'LH1', MIN: 1, MAX: 1000, LEVEL: [
                    {ID: 'LH2', MIN: 0, MAX: 4},
                    {ID: 'LH3', MIN: 0, MAX: 10},
                    {ID: 'LFH', MIN: 0, MAX: 20},
                    {ID: 'LEP', MIN: 0, MAX: 3},
                    {ID: 'LH4', MIN: 0, MAX: 4},
                    {ID: 'LHT', MIN: 0, MAX: 3},
                    {ID: 'LHR', MIN: 0, MAX: 5},
                    {ID: 'PER', MIN: 0, MAX: 5},
                    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'N3', MIN: 0, MAX: 2},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'PER', MIN: 0, MAX: 2},
                    ]},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'LH2', MIN: 0, MAX: 1},
            {ID: 'LHR', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
