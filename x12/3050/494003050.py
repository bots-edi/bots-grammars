from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'PRI', MIN: 1, MAX: 1},
    {ID: 'SRC', MIN: 1, MAX: 1},
    {ID: 'SRD', MIN: 1, MAX: 200},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
