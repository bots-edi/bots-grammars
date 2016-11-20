from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'CDS', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'SPI', MIN: 0, MAX: 1},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'LS', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'CED', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'SPI', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'PAM', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'CRC', MIN: 0, MAX: 99999},
                {ID: 'CDS', MIN: 0, MAX: 99999},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'SPI', MIN: 0, MAX: 2},
                    {ID: 'N2', MIN: 0, MAX: 99999},
                    {ID: 'N3', MIN: 0, MAX: 99999},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                    {ID: 'PER', MIN: 0, MAX: 99999},
                    {ID: 'DMG', MIN: 0, MAX: 1},
                    {ID: 'MEA', MIN: 0, MAX: 3},
                    {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'REF', MIN: 0, MAX: 99999},
                        {ID: 'III', MIN: 0, MAX: 1},
                        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'LQ', MIN: 1, MAX: 99999},
                        ]},
                    ]},
                ]},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
