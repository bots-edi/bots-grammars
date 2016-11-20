from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'AK1', MIN: 1, MAX: 1},
    {ID: 'AK2', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'IK3', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CTX', MIN: 0, MAX: 10},
            {ID: 'IK4', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'CTX', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'IK5', MIN: 1, MAX: 1},
    ]},
    {ID: 'AK9', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
