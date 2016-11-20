from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ATA', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'L11', MIN: 0, MAX: 300},
    {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 1},
        {ID: 'L11', MIN: 0, MAX: 10},
    ]},
    {ID: 'AT7', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'G62', MIN: 0, MAX: 5},
        {ID: 'MS1', MIN: 0, MAX: 1},
        {ID: 'MS2', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'M7', MIN: 0, MAX: 1},
            {ID: 'AT9', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 10},
        {ID: 'AT7', MIN: 0, MAX: 1},
        {ID: 'BLR', MIN: 0, MAX: 1},
        {ID: 'MAN', MIN: 0, MAX: 9999},
        {ID: 'AT8', MIN: 0, MAX: 1},
        {ID: 'Q7', MIN: 0, MAX: 10},
        {ID: 'G62', MIN: 0, MAX: 5},
        {ID: 'TSD', MIN: 0, MAX: 1},
        {ID: 'OID', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 9999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'L11', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
