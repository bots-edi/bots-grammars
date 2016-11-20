from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'SPI', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'RDT', MIN: 0, MAX: 99999},
        {ID: 'NTE', MIN: 0, MAX: 99999},
        {ID: 'X1', MIN: 0, MAX: 1},
        {ID: 'X2', MIN: 0, MAX: 1},
        {ID: 'X7', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'SPI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'RDT', MIN: 0, MAX: 99999},
            {ID: 'PRR', MIN: 0, MAX: 99999},
            {ID: 'PRT', MIN: 0, MAX: 99999},
            {ID: 'PRS', MIN: 0, MAX: 1},
            {ID: 'LIN', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 99999},
                {ID: 'N9', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PKD', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'UIT', MIN: 0, MAX: 99999},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'PWK', MIN: 0, MAX: 99999},
            {ID: 'PKG', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LIN', MIN: 0, MAX: 1},
            {ID: 'TMD', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 1, MAX: 99999},
            {ID: 'PSD', MIN: 0, MAX: 99999},
            {ID: 'SPS', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'BIN', MIN: 0, MAX: 1},
        ]},
        {ID: 'CID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'UIT', MIN: 0, MAX: 1},
            {ID: 'TMD', MIN: 0, MAX: 99999},
            {ID: 'PSD', MIN: 0, MAX: 1},
            {ID: 'CSS', MIN: 0, MAX: 1},
            {ID: 'SPS', MIN: 0, MAX: 1},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
            {ID: 'STA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
            {ID: 'CSF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'CID', MIN: 1, MAX: 99999, LEVEL: [
                        {ID: 'MEA', MIN: 0, MAX: 1},
                        {ID: 'STA', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
            ]},
            {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'BIN', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
