from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'UW',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'LTR', MIN: 0, MAX: 99},
    {ID: 'NM1', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'ACT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NM1', MIN: 0, MAX: 9},
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 5},
            {ID: 'AM1', MIN: 0, MAX: 9},
            {ID: 'PWK', MIN: 0, MAX: 1},
            {ID: 'K3', MIN: 0, MAX: 3},
            {ID: 'SPK', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'CD2', MIN: 0, MAX: 9},
                {ID: 'K3', MIN: 0, MAX: 3},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N4', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'LTR', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'CD2', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'NM1', MIN: 0, MAX: 9},
                {ID: 'K3', MIN: 0, MAX: 3},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
