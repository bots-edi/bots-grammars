from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CV',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 99999},
    {ID: 'NX1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 1, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'DMA', MIN: 0, MAX: 1},
            {ID: 'DVI', MIN: 0, MAX: 99999},
            {ID: 'VC1', MIN: 0, MAX: 1},
            {ID: 'VEH', MIN: 0, MAX: 1},
            {ID: 'N12', MIN: 0, MAX: 1},
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 99999},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'MEA', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'LM', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 1},
                    {ID: 'YNQ', MIN: 0, MAX: 99999},
                    {ID: 'REF', MIN: 0, MAX: 1},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'PCT', MIN: 0, MAX: 1},
                    {ID: 'AMT', MIN: 0, MAX: 1},
                    {ID: 'SPR', MIN: 0, MAX: 1},
                    {ID: 'SRE', MIN: 0, MAX: 1},
                    {ID: 'STA', MIN: 0, MAX: 99999},
                    {ID: 'MEA', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 1},
                    {ID: 'NTE', MIN: 0, MAX: 99999},
                    {ID: 'TC2', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'H1', MIN: 0, MAX: 1},
                        {ID: 'PER', MIN: 0, MAX: 1},
                        {ID: 'N4', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'REF', MIN: 0, MAX: 99999},
                        ]},
                    ]},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
