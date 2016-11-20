from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FA2', MIN: 1, MAX: 99999},
    ]},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'ASI', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'PM', MIN: 0, MAX: 1},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
