from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B3B', MIN: 1, MAX: 1},
    {ID: 'C4', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 30},
    {ID: 'CM', MIN: 0, MAX: 2},
    {ID: 'NTE', MIN: 0, MAX: 2},
    {ID: 'N7', MIN: 1, MAX: 500, LEVEL: [
        {ID: 'VC', MIN: 0, MAX: 36},
        {ID: 'G4', MIN: 0, MAX: 1},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'N5', MIN: 0, MAX: 1},
        {ID: 'IC', MIN: 0, MAX: 1},
        {ID: 'IM', MIN: 0, MAX: 1},
        {ID: 'M12', MIN: 0, MAX: 1},
        {ID: 'GA', MIN: 0, MAX: 15},
    ]},
    {ID: 'N8', MIN: 1, MAX: 499},
    {ID: 'F9', MIN: 1, MAX: 1},
    {ID: 'D9', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 15, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'BL', MIN: 0, MAX: 12},
    ]},
    {ID: 'S1', MIN: 0, MAX: 12, LEVEL: [
        {ID: 'S2', MIN: 0, MAX: 1},
        {ID: 'S9', MIN: 0, MAX: 1},
    ]},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'R9', MIN: 0, MAX: 1},
    {ID: 'PS', MIN: 0, MAX: 5},
    {ID: 'LX', MIN: 1, MAX: 25, LEVEL: [
        {ID: 'L5', MIN: 1, MAX: 15},
        {ID: 'L0', MIN: 1, MAX: 25, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 3},
            {ID: 'L1', MIN: 1, MAX: 10},
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'PI', MIN: 0, MAX: 30},
        ]},
    ]},
    {ID: 'T1', MIN: 0, MAX: 64, LEVEL: [
        {ID: 'T2', MIN: 0, MAX: 30},
        {ID: 'T3', MIN: 0, MAX: 12},
        {ID: 'T6', MIN: 0, MAX: 1},
        {ID: 'T8', MIN: 0, MAX: 99},
    ]},
    {ID: 'L3', MIN: 1, MAX: 1},
    {ID: 'X7', MIN: 0, MAX: 2},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
