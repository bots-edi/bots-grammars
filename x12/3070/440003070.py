from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'WR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BW', MIN: 1, MAX: 1},
    {ID: 'G4', MIN: 0, MAX: 1},
    {ID: 'G5', MIN: 1, MAX: 255},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
