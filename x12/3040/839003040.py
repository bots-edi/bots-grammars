from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PK',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCS', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 100},
    {ID: 'DLV', MIN: 0, MAX: 10},
    {ID: 'AMT', MIN: 0, MAX: 30},
    {ID: 'PCT', MIN: 0, MAX: 30},
    {ID: 'DTM', MIN: 0, MAX: 30},
    {ID: 'CFT', MIN: 1, MAX: 100, LEVEL: [
        {ID: 'CAL', MIN: 0, MAX: 50},
        {ID: 'BSD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 100},
            {ID: 'DTM', MIN: 0, MAX: 50},
            {ID: 'AMT', MIN: 0, MAX: 100},
            {ID: 'QTY', MIN: 0, MAX: 100},
            {ID: 'PAM', MIN: 0, MAX: 100},
            {ID: 'PCT', MIN: 0, MAX: 100},
            {ID: 'MSG', MIN: 0, MAX: 1000},
        ]},
    ]},
    {ID: 'N1', MIN: 1, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 10},
        {ID: 'DTM', MIN: 0, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
