from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'KM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'SPI', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'LM', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'N9', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                    {ID: 'MEA', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'PDL', MIN: 0, MAX: 1},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'YNQ', MIN: 0, MAX: 99999},
                    {ID: 'VEH', MIN: 0, MAX: 99999},
                    {ID: 'DVI', MIN: 0, MAX: 99999},
                    {ID: 'TC2', MIN: 0, MAX: 99999},
                    {ID: 'N12', MIN: 0, MAX: 99999},
                    {ID: 'H1', MIN: 0, MAX: 99999},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'N2', MIN: 0, MAX: 2},
                        {ID: 'N3', MIN: 0, MAX: 2},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'N9', MIN: 0, MAX: 99999},
                        {ID: 'PER', MIN: 0, MAX: 99999},
                        {ID: 'EMS', MIN: 0, MAX: 1},
                        {ID: 'DTM', MIN: 0, MAX: 99999},
                        {ID: 'MEA', MIN: 0, MAX: 99999},
                        {ID: 'QTY', MIN: 0, MAX: 99999},
                        {ID: 'YNQ', MIN: 0, MAX: 99999},
                        {ID: 'TD5', MIN: 0, MAX: 99999},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
