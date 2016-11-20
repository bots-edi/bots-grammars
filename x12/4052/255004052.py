from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'UI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'ACT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'AM1', MIN: 0, MAX: 9},
        {ID: 'PWK', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MSG', MIN: 0, MAX: 9},
        {ID: 'YNQ', MIN: 0, MAX: 15},
        {ID: 'NTE', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 3},
            {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'ASI', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 3},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'IND', MIN: 0, MAX: 1},
                {ID: 'CD2', MIN: 0, MAX: 9},
                {ID: 'MSG', MIN: 0, MAX: 9},
            ]},
            {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'BIN', MIN: 0, MAX: 1},
            ]},
            {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'ASI', MIN: 0, MAX: 1},
                {ID: 'DMA', MIN: 0, MAX: 9},
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'MSG', MIN: 0, MAX: 9},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                        {ID: 'NM1', MIN: 1, MAX: 1},
                        {ID: 'N2', MIN: 0, MAX: 3},
                        {ID: 'NX2', MIN: 0, MAX: 99999},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'REC', MIN: 0, MAX: 1},
                        {ID: 'IND', MIN: 0, MAX: 1},
                        {ID: 'EMS', MIN: 0, MAX: 1},
                        {ID: 'PER', MIN: 0, MAX: 3},
                        {ID: 'CN1', MIN: 0, MAX: 1},
                        {ID: 'DTP', MIN: 0, MAX: 9},
                        {ID: 'CD2', MIN: 0, MAX: 9},
                        {ID: 'REF', MIN: 0, MAX: 9},
                        {ID: 'PWK', MIN: 0, MAX: 1},
                        {ID: 'MSG', MIN: 0, MAX: 9},
                        {ID: 'AM1', MIN: 0, MAX: 99999},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
