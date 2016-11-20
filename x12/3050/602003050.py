from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'PRI', MIN: 0, MAX: 12},
    {ID: 'SS', MIN: 0, MAX: 1},
    {ID: 'SA', MIN: 0, MAX: 5},
    {ID: 'NTE', MIN: 0, MAX: 5},
    {ID: 'CD', MIN: 0, MAX: 20},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 200},
    ]},
    {ID: 'PR', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'NTE', MIN: 0, MAX: 10},
        {ID: 'CD', MIN: 0, MAX: 10},
    ]},
    {ID: 'SB', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'GY', MIN: 0, MAX: 999},
        {ID: 'SC', MIN: 0, MAX: 400, LEVEL: [
            {ID: 'GY', MIN: 0, MAX: 9999},
            {ID: 'CD', MIN: 0, MAX: 100},
            {ID: 'RA', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'RB', MIN: 0, MAX: 8},
                {ID: 'FK', MIN: 0, MAX: 15},
            ]},
            {ID: 'RH', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 30},
            ]},
        ]},
        {ID: 'SRT', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'MIN', MIN: 0, MAX: 100},
            {ID: 'SRD', MIN: 0, MAX: 200},
            {ID: 'SRM', MIN: 0, MAX: 999},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'LX', MIN: 0, MAX: 200, LEVEL: [
                {ID: 'SRD', MIN: 0, MAX: 1},
                {ID: 'SRM', MIN: 0, MAX: 100, LEVEL: [
                    {ID: 'SRA', MIN: 0, MAX: 5},
                ]},
            ]},
        ]},
    ]},
    {ID: 'MS', MIN: 0, MAX: 200},
    {ID: 'DM', MIN: 0, MAX: 5},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
