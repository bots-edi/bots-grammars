from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B3', MIN: 1, MAX: 1},
    {ID: 'B3A', MIN: 0, MAX: 1},
    {ID: 'C2', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'LX', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 1},
        ]},
        {ID: 'P1', MIN: 0, MAX: 1},
        {ID: 'R1', MIN: 0, MAX: 1},
        {ID: 'POD', MIN: 0, MAX: 1},
        {ID: 'V9', MIN: 0, MAX: 1},
        {ID: 'RMT', MIN: 0, MAX: 10},
        {ID: 'G47', MIN: 0, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 10},
        {ID: 'L5', MIN: 1, MAX: 4, LEVEL: [
            {ID: 'L0', MIN: 0, MAX: 1},
            {ID: 'L4', MIN: 0, MAX: 4},
            {ID: 'L10', MIN: 0, MAX: 4},
            {ID: 'SL1', MIN: 0, MAX: 1},
            {ID: 'L1', MIN: 0, MAX: 30, LEVEL: [
                {ID: 'C3', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'L3', MIN: 1, MAX: 1},
    {ID: 'ACS', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 5},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
