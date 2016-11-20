from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PW',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 1},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'TRN', MIN: 0, MAX: 1},
        {ID: 'AAA', MIN: 0, MAX: 1},
        {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 20},
            {ID: 'API', MIN: 0, MAX: 99999},
            {ID: 'DEG', MIN: 0, MAX: 9},
            {ID: 'IND', MIN: 0, MAX: 1},
            {ID: 'LUI', MIN: 0, MAX: 9},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'AAA', MIN: 0, MAX: 1},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99},
            {ID: 'WS', MIN: 0, MAX: 99},
            {ID: 'CRC', MIN: 0, MAX: 9},
            {ID: 'HSD', MIN: 0, MAX: 99},
            {ID: 'BCI', MIN: 0, MAX: 9},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'HAD', MIN: 0, MAX: 1},
            {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
            ]},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 2},
                {ID: 'TPB', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'YNQ', MIN: 0, MAX: 99999},
                {ID: 'AAA', MIN: 0, MAX: 1},
            ]},
            {ID: 'HPL', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'AAA', MIN: 0, MAX: 1},
            ]},
            {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'AAA', MIN: 0, MAX: 1},
            ]},
            {ID: 'EMS', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
