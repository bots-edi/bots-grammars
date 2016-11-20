from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N2', MIN: 0, MAX: 1},
    {ID: 'N3', MIN: 0, MAX: 1},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'PER', MIN: 0, MAX: 1},
    {ID: 'P1', MIN: 0, MAX: 1},
    {ID: 'G47', MIN: 0, MAX: 1},
    {ID: 'F9', MIN: 0, MAX: 1},
    {ID: 'FOB', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'SL1', MIN: 1, MAX: 1},
        {ID: 'N9', MIN: 1, MAX: 10},
        {ID: 'TD4', MIN: 0, MAX: 10},
        {ID: 'H1', MIN: 0, MAX: 1},
        {ID: 'H2', MIN: 0, MAX: 1},
        {ID: 'H3', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'M1', MIN: 0, MAX: 1},
        {ID: 'C3', MIN: 0, MAX: 1},
        {ID: 'X1', MIN: 0, MAX: 1},
        {ID: 'X2', MIN: 0, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 10},
        {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 1},
        ]},
        {ID: 'L5', MIN: 1, MAX: 100, LEVEL: [
            {ID: 'L0', MIN: 0, MAX: 10},
            {ID: 'L1', MIN: 0, MAX: 10},
            {ID: 'L4', MIN: 0, MAX: 10},
        ]},
        {ID: 'ACS', MIN: 0, MAX: 100},
    ]},
    {ID: 'L3', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
