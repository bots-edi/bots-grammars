from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'ENT', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'IN2', MIN: 0, MAX: 5},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'DMA', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 3},
        {ID: 'YNQ', MIN: 0, MAX: 5},
        {ID: 'ENR', MIN: 0, MAX: 1},
        {ID: 'IN1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 5},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'YNQ', MIN: 0, MAX: 5},
        ]},
        {ID: 'REF', MIN: 1, MAX: 100, LEVEL: [
            {ID: 'SLI', MIN: 0, MAX: 1},
            {ID: 'GR', MIN: 0, MAX: 1},
            {ID: 'DEF', MIN: 0, MAX: 100},
            {ID: 'YNQ', MIN: 0, MAX: 1000},
            {ID: 'DB', MIN: 0, MAX: 10},
            {ID: 'DTP', MIN: 0, MAX: 500},
            {ID: 'AMT', MIN: 0, MAX: 500},
            {ID: 'IN1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'IN2', MIN: 0, MAX: 5},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 2},
                {ID: 'YNQ', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
