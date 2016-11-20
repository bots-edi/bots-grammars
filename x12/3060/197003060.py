from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'PID', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 12},
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'BIN', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 0, MAX: 99999},
            {ID: 'PDS', MIN: 0, MAX: 20},
            {ID: 'PDE', MIN: 0, MAX: 99999},
        ]},
        {ID: 'FGS', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 2},
            {ID: 'FPT', MIN: 0, MAX: 1},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'IN2', MIN: 0, MAX: 30},
                {ID: 'AMT', MIN: 0, MAX: 2},
                {ID: 'M1', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 10},
            ]},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 3},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'IN2', MIN: 0, MAX: 30},
                    {ID: 'M1', MIN: 0, MAX: 20},
                    {ID: 'MSG', MIN: 0, MAX: 4},
                ]},
            ]},
        ]},
        {ID: 'LX', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'G86', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
