from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'TRN', MIN: 0, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 3},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'N9', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DEX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 1, MAX: 15},
            {ID: 'CN1', MIN: 0, MAX: 1},
            {ID: 'PCT', MIN: 0, MAX: 10},
            {ID: 'INT', MIN: 0, MAX: 10},
            {ID: 'AMT', MIN: 0, MAX: 4},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'MPP', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 10},
            {ID: 'III', MIN: 0, MAX: 15},
            {ID: 'ASM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 5},
            ]},
            {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 0, MAX: 15},
                    {ID: 'AMT', MIN: 0, MAX: 20},
                    {ID: 'DTP', MIN: 0, MAX: 5},
                    {ID: 'YNQ', MIN: 0, MAX: 10},
                    {ID: 'QTY', MIN: 0, MAX: 5},
                    {ID: 'N1', MIN: 0, MAX: 6},
                    {ID: 'III', MIN: 0, MAX: 50},
                    {ID: 'LUC', MIN: 0, MAX: 1},
                    {ID: 'RLD', MIN: 0, MAX: 50},
                    {ID: 'INT', MIN: 0, MAX: 6},
                    {ID: 'PPD', MIN: 0, MAX: 1},
                    {ID: 'PWK', MIN: 0, MAX: 2},
                    {ID: 'BUY', MIN: 0, MAX: 1},
                    {ID: 'PEX', MIN: 0, MAX: 10},
                    {ID: 'BEP', MIN: 0, MAX: 2},
                    {ID: 'IGI', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'REF', MIN: 0, MAX: 1},
                        {ID: 'PCT', MIN: 0, MAX: 10},
                    ]},
                    {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'NX2', MIN: 0, MAX: 15},
                        {ID: 'REA', MIN: 0, MAX: 1},
                        {ID: 'PDS', MIN: 0, MAX: 2},
                    ]},
                    {ID: 'LN1', MIN: 0, MAX: 5, LEVEL: [
                        {ID: 'YNQ', MIN: 0, MAX: 1},
                        {ID: 'DTP', MIN: 0, MAX: 5},
                        {ID: 'REF', MIN: 0, MAX: 10},
                    ]},
                    {ID: 'CRC', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'IN1', MIN: 0, MAX: 1},
                        {ID: 'IN2', MIN: 0, MAX: 30},
                        {ID: 'DMG', MIN: 0, MAX: 1},
                        {ID: 'QTY', MIN: 0, MAX: 10},
                        {ID: 'N1', MIN: 0, MAX: 1},
                        {ID: 'YNQ', MIN: 0, MAX: 5},
                        {ID: 'AIN', MIN: 0, MAX: 10},
                        {ID: 'AMT', MIN: 0, MAX: 15},
                        {ID: 'SCM', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'SCS', MIN: 0, MAX: 5},
                        ]},
                    ]},
                    {ID: 'PAM', MIN: 0, MAX: 4, LEVEL: [
                        {ID: 'YNQ', MIN: 1, MAX: 1},
                        {ID: 'REF', MIN: 1, MAX: 1},
                    ]},
                    {ID: 'UWI', MIN: 0, MAX: 5, LEVEL: [
                        {ID: 'III', MIN: 0, MAX: 10},
                        {ID: 'REF', MIN: 0, MAX: 1},
                        {ID: 'MSG', MIN: 0, MAX: 99999},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
