from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'TRN', MIN: 0, MAX: 1},
    {ID: 'NM1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 4},
    ]},
    {ID: 'MNC', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'SOM', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 20},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'INT', MIN: 0, MAX: 2},
        {ID: 'PCT', MIN: 0, MAX: 10},
        {ID: 'AMT', MIN: 0, MAX: 10},
        {ID: 'QTY', MIN: 0, MAX: 6},
        {ID: 'YNQ', MIN: 0, MAX: 12},
        {ID: 'III', MIN: 0, MAX: 12},
        {ID: 'CDI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'VDI', MIN: 0, MAX: 99999},
                {ID: 'YNQ', MIN: 0, MAX: 4},
                {ID: 'AMT', MIN: 0, MAX: 6},
                {ID: 'PCT', MIN: 0, MAX: 6},
                {ID: 'DTP', MIN: 0, MAX: 5},
                {ID: 'III', MIN: 0, MAX: 12},
            ]},
        ]},
        {ID: 'IN1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'REF', MIN: 0, MAX: 15},
            {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NX2', MIN: 0, MAX: 99999},
                {ID: 'PDS', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
