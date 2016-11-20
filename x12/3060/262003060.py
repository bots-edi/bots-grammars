from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'TRN', MIN: 0, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'AM1', MIN: 0, MAX: 4},
        {ID: 'PWK', MIN: 0, MAX: 5},
        {ID: 'NX1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 1, MAX: 7},
            {ID: 'PEX', MIN: 0, MAX: 3},
            {ID: 'PDS', MIN: 0, MAX: 99999},
            {ID: 'PDE', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 25},
            {ID: 'REF', MIN: 0, MAX: 16},
            {ID: 'DTP', MIN: 0, MAX: 6},
            {ID: 'YNQ', MIN: 0, MAX: 43},
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'PCT', MIN: 0, MAX: 8},
            {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 10},
            ]},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 7},
                {ID: 'MSG', MIN: 0, MAX: 3},
                {ID: 'DTP', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'IN1', MIN: 1, MAX: 6, LEVEL: [
            {ID: 'IN2', MIN: 1, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 2},
            {ID: 'YNQ', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'REF', MIN: 1, MAX: 1},
                {ID: 'DTP', MIN: 1, MAX: 2},
                {ID: 'III', MIN: 1, MAX: 50, LEVEL: [
                    {ID: 'MSG', MIN: 0, MAX: 10},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
