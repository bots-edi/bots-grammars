from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'F01', MIN: 1, MAX: 1},
    {ID: 'F6X', MIN: 1, MAX: 1},
    {ID: 'F02', MIN: 0, MAX: 1},
    {ID: 'F12', MIN: 0, MAX: 1},
    {ID: 'F07', MIN: 1, MAX: 99},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
