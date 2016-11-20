from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'G47', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 8},
    {ID: 'G23', MIN: 0, MAX: 20},
    {ID: 'G48', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'G72', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'G73', MIN: 0, MAX: 10},
        ]},
        {ID: 'G23', MIN: 0, MAX: 20},
        {ID: 'G25', MIN: 0, MAX: 1},
        {ID: 'G31', MIN: 0, MAX: 1},
        {ID: 'G33', MIN: 1, MAX: 1},
    ]},
    {ID: 'G49', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
