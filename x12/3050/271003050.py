from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'TRN', MIN: 0, MAX: 9},
        {ID: 'AAA', MIN: 0, MAX: 9},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'AAA', MIN: 0, MAX: 9},
            {ID: 'PRV', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'INS', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'EB', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'HSD', MIN: 0, MAX: 9},
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 20},
                {ID: 'AAA', MIN: 0, MAX: 9},
                {ID: 'MSG', MIN: 0, MAX: 10},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'NM1', MIN: 1, MAX: 1, LEVEL: [
                        {ID: 'N2', MIN: 0, MAX: 1},
                        {ID: 'N3', MIN: 0, MAX: 1},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'PER', MIN: 0, MAX: 3},
                        {ID: 'PRV', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
