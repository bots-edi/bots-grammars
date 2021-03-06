from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'SMB', MIN: 1, MAX: 1},
    {ID: 'N4', MIN: 1, MAX: 10},
    {ID: 'CD', MIN: 0, MAX: 10},
    {ID: 'SMS', MIN: 0, MAX: 1},
    {ID: 'SMA', MIN: 0, MAX: 10},
    {ID: 'SMR', MIN: 0, MAX: 10},
    {ID: 'SMO', MIN: 0, MAX: 10},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
