from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AQ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'M13', MIN: 0, MAX: 1},
            {ID: 'M11', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
            {ID: 'M12', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'P5', MIN: 0, MAX: 5},
            ]},
            {ID: 'VID', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'N10', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'H1', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'H2', MIN: 0, MAX: 99},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
