from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B3', MIN: 1, MAX: 1},
    {ID: 'Y6', MIN: 0, MAX: 2},
    {ID: 'Q3', MIN: 1, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'G1', MIN: 0, MAX: 1},
    {ID: 'G2', MIN: 0, MAX: 1},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'N9', MIN: 0, MAX: 15},
    {ID: 'V1', MIN: 1, MAX: 2},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'R4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 15},
    ]},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'L5', MIN: 0, MAX: 1},
    {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N7', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'N12', MIN: 0, MAX: 1},
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'W09', MIN: 0, MAX: 1},
            {ID: 'L4', MIN: 0, MAX: 1},
            {ID: 'H1', MIN: 0, MAX: 2, LEVEL: [
                {ID: 'H2', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'L0', MIN: 0, MAX: 120, LEVEL: [
            {ID: 'L5', MIN: 0, MAX: 999},
            {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'C3', MIN: 0, MAX: 1},
            ]},
            {ID: 'L7', MIN: 0, MAX: 1},
            {ID: 'H1', MIN: 0, MAX: 2, LEVEL: [
                {ID: 'H2', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'V9', MIN: 0, MAX: 10},
    {ID: 'L3', MIN: 1, MAX: 1},
    {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'C3', MIN: 0, MAX: 1},
    ]},
    {ID: 'K1', MIN: 0, MAX: 999},
    {ID: 'L11', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
