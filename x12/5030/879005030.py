from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'G91', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 99999},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'G36', MIN: 0, MAX: 1},
    {ID: 'G26', MIN: 0, MAX: 99},
    {ID: 'G43', MIN: 0, MAX: 9999},
    {ID: 'G62', MIN: 1, MAX: 10},
    {ID: 'G46', MIN: 0, MAX: 100},
    {ID: 'G93', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'G46', MIN: 0, MAX: 1},
        {ID: 'G26', MIN: 0, MAX: 99999},
    ]},
    {ID: 'G28', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'G20', MIN: 0, MAX: 1},
        {ID: 'G69', MIN: 0, MAX: 5},
        {ID: 'G26', MIN: 0, MAX: 99},
        {ID: 'G43', MIN: 0, MAX: 9999},
        {ID: 'G62', MIN: 0, MAX: 4},
        {ID: 'G46', MIN: 0, MAX: 100},
        {ID: 'G22', MIN: 0, MAX: 1},
        {ID: 'SAC', MIN: 0, MAX: 10},
        {ID: 'G40', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'G46', MIN: 0, MAX: 100},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
