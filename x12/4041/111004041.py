from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'ASI', MIN: 0, MAX: 99999},
        {ID: 'LQ', MIN: 0, MAX: 99999},
        {ID: 'C3', MIN: 0, MAX: 1},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'LUI', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 99999},
        {ID: 'BLI', MIN: 0, MAX: 1},
        {ID: 'LIN', MIN: 0, MAX: 99999},
        {ID: 'UDA', MIN: 0, MAX: 99999},
        {ID: 'SPA', MIN: 0, MAX: 99999},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'BLN', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'RPA', MIN: 0, MAX: 99999},
        {ID: 'PDL', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 99999},
        ]},
        {ID: 'AM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'III', MIN: 0, MAX: 99999},
            {ID: 'SPA', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'RPA', MIN: 0, MAX: 99999},
            {ID: 'BLN', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 3},
            {ID: 'COM', MIN: 0, MAX: 99999},
            {ID: 'N3', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'BEN', MIN: 0, MAX: 1},
            {ID: 'III', MIN: 0, MAX: 99999},
            {ID: 'AM1', MIN: 0, MAX: 99999},
            {ID: 'IN1', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
