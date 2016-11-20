from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ZC1', MIN: 0, MAX: 1},
    {ID: 'Q5', MIN: 1, MAX: 1},
    {ID: 'N7', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'V4', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'W09', MIN: 0, MAX: 1},
        {ID: 'W2', MIN: 0, MAX: 1},
        {ID: 'NA', MIN: 0, MAX: 30},
        {ID: 'GR5', MIN: 0, MAX: 10},
        {ID: 'Y7', MIN: 0, MAX: 1},
        {ID: 'V1', MIN: 0, MAX: 1},
        {ID: 'R4', MIN: 1, MAX: 20, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 15},
        ]},
        {ID: 'H3', MIN: 0, MAX: 6},
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'K1', MIN: 0, MAX: 2},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'L0', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'L5', MIN: 0, MAX: 1},
            {ID: 'H1', MIN: 0, MAX: 3},
            {ID: 'LH1', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'LH2', MIN: 0, MAX: 4},
                {ID: 'LH3', MIN: 0, MAX: 10},
                {ID: 'LFH', MIN: 0, MAX: 25},
                {ID: 'LEP', MIN: 0, MAX: 3},
                {ID: 'LH4', MIN: 0, MAX: 1},
                {ID: 'LHT', MIN: 0, MAX: 3},
                {ID: 'LHR', MIN: 0, MAX: 5},
                {ID: 'PER', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'L3', MIN: 0, MAX: 2},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
