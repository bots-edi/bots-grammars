from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'G05', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'TD1', MIN: 0, MAX: 5},
            {ID: 'TD3', MIN: 0, MAX: 5},
            {ID: 'TD4', MIN: 0, MAX: 5},
            {ID: 'TD5', MIN: 0, MAX: 10},
            {ID: 'FOB', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'N9', MIN: 0, MAX: 20},
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'TDS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'PRF', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'ITD', MIN: 0, MAX: 5},
            {ID: 'TXI', MIN: 0, MAX: 10},
            {ID: 'SN1', MIN: 0, MAX: 1},
            {ID: 'ISS', MIN: 0, MAX: 1},
            {ID: 'SAC', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'TXI', MIN: 0, MAX: 10},
            ]},
            {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'PAL', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'MAN', MIN: 0, MAX: 10},
        ]},
        {ID: 'LX', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 15},
            {ID: 'PO4', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'PKG', MIN: 0, MAX: 10},
            {ID: 'MAN', MIN: 0, MAX: 10},
        ]},
        {ID: 'IT1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'IT3', MIN: 0, MAX: 1},
            {ID: 'PO4', MIN: 0, MAX: 1},
            {ID: 'TD4', MIN: 0, MAX: 99999},
            {ID: 'TC2', MIN: 0, MAX: 5},
            {ID: 'TXI', MIN: 0, MAX: 10},
            {ID: 'CTP', MIN: 0, MAX: 10},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'PID', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 10},
            ]},
            {ID: 'SLN', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'PID', MIN: 0, MAX: 25},
            ]},
            {ID: 'SAC', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'TXI', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
