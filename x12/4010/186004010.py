from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'UW',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'LTR', MIN: 0, MAX: 99},
    {ID: 'NM1', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'ACT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 5},
                {ID: 'AM1', MIN: 0, MAX: 9},
                {ID: 'PWK', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'DMA', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 99999},
            ]},
            {ID: 'BOR', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'PER', MIN: 0, MAX: 1},
                    {ID: 'N3', MIN: 0, MAX: 1},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'DMA', MIN: 0, MAX: 1},
                    {ID: 'REL', MIN: 0, MAX: 1},
                ]},
                {ID: 'SPK', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'CD2', MIN: 0, MAX: 9},
                    {ID: 'DTP', MIN: 0, MAX: 9},
                    {ID: 'REF', MIN: 0, MAX: 1},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'N4', MIN: 0, MAX: 1},
                    ]},
                ]},
                {ID: 'LTR', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'CD2', MIN: 0, MAX: 9},
                    {ID: 'DTP', MIN: 0, MAX: 9},
                    {ID: 'NM1', MIN: 0, MAX: 9},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
                {ID: 'UC', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'HL', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'UQS', MIN: 0, MAX: 1},
                        {ID: 'NM1', MIN: 0, MAX: 1},
                        {ID: 'N1', MIN: 0, MAX: 1},
                        {ID: 'N3', MIN: 0, MAX: 1},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'DTP', MIN: 0, MAX: 99999},
                        {ID: 'QTY', MIN: 0, MAX: 99999},
                        {ID: 'MSG', MIN: 0, MAX: 99999},
                        {ID: 'DMA', MIN: 0, MAX: 1},
                        {ID: 'AM1', MIN: 0, MAX: 1},
                        {ID: 'DMG', MIN: 0, MAX: 1},
                        {ID: 'AMT', MIN: 0, MAX: 1},
                        {ID: 'EC', MIN: 0, MAX: 1},
                        {ID: 'PER', MIN: 0, MAX: 1},
                        {ID: 'REF', MIN: 0, MAX: 1},
                        {ID: 'IN1', MIN: 0, MAX: 1},
                        {ID: 'EMS', MIN: 0, MAX: 1},
                        {ID: 'ASL', MIN: 0, MAX: 99999},
                        {ID: 'TOA', MIN: 0, MAX: 1},
                        {ID: 'TOV', MIN: 0, MAX: 1},
                        {ID: 'III', MIN: 0, MAX: 99999},
                        {ID: 'SIN', MIN: 0, MAX: 1},
                        {ID: 'UCS', MIN: 0, MAX: 1},
                        {ID: 'FH', MIN: 0, MAX: 1},
                        {ID: 'UD', MIN: 0, MAX: 1},
                        {ID: 'CDS', MIN: 0, MAX: 1},
                        {ID: 'CED', MIN: 0, MAX: 1},
                        {ID: 'YNQ', MIN: 0, MAX: 1},
                        {ID: 'MPI', MIN: 0, MAX: 1},
                        {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'BIN', MIN: 1, MAX: 1},
                        ]},
                    ]},
                ]},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'UD', MIN: 1, MAX: 99999, LEVEL: [
                        {ID: 'NM1', MIN: 0, MAX: 1},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'REL', MIN: 0, MAX: 1},
                        {ID: 'DTP', MIN: 0, MAX: 1},
                        {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'BIN', MIN: 1, MAX: 1},
                        ]},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
