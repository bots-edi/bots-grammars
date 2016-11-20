from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'STP', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 1},
    ]},
    {ID: 'GID', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'GRP', MIN: 1, MAX: 1},
        {ID: 'MSG', MIN: 1, MAX: 99999},
        {ID: 'GDP', MIN: 1, MAX: 99999},
        {ID: 'REF', MIN: 1, MAX: 99999},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'ANI', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'ARC', MIN: 1, MAX: 99999},
            {ID: 'GDP', MIN: 0, MAX: 99999},
            {ID: 'ADI', MIN: 0, MAX: 1},
            {ID: 'ATR', MIN: 0, MAX: 99999},
            {ID: 'AOL', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'AOR', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'NTE', MIN: 1, MAX: 99999},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'AST', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'ADT', MIN: 0, MAX: 1},
                {ID: 'AOC', MIN: 0, MAX: 99999},
            ]},
            {ID: 'AOI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'ATR', MIN: 0, MAX: 99999},
                {ID: 'AOL', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                    {ID: 'AOR', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'NTE', MIN: 1, MAX: 99999},
                        {ID: 'MSG', MIN: 0, MAX: 99999},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
