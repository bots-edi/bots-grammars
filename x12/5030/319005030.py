from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BA2', MIN: 1, MAX: 1},
    {ID: 'CD1', MIN: 1, MAX: 999},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
