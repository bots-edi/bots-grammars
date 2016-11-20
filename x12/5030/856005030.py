from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SH',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'HL', MIN: 1, MAX: 200000, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'SN1', MIN: 0, MAX: 1},
        {ID: 'SLN', MIN: 0, MAX: 1000},
        {ID: 'PRF', MIN: 0, MAX: 1},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'PID', MIN: 0, MAX: 200},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'PWK', MIN: 0, MAX: 25},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'TD1', MIN: 0, MAX: 20},
        {ID: 'TD5', MIN: 0, MAX: 12},
        {ID: 'TD3', MIN: 0, MAX: 12, LEVEL: [
            {ID: 'AT9', MIN: 0, MAX: 1},
        ]},
        {ID: 'TD4', MIN: 0, MAX: 5},
        {ID: 'TSD', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'LH1', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'LH2', MIN: 0, MAX: 4},
            {ID: 'LH3', MIN: 0, MAX: 12},
            {ID: 'LFH', MIN: 0, MAX: 20},
            {ID: 'LEP', MIN: 0, MAX: 99999},
            {ID: 'LH4', MIN: 0, MAX: 4},
            {ID: 'LHT', MIN: 0, MAX: 3},
            {ID: 'LHR', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'LHE', MIN: 0, MAX: 1},
        ]},
        {ID: 'CLD', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 200},
            {ID: 'DTP', MIN: 0, MAX: 1},
        ]},
        {ID: 'MAN', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'PAL', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'FOB', MIN: 0, MAX: 1},
        ]},
        {ID: 'SDQ', MIN: 0, MAX: 50},
        {ID: 'ETD', MIN: 0, MAX: 1},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'SAC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
        {ID: 'GF', MIN: 0, MAX: 1},
        {ID: 'YNQ', MIN: 0, MAX: 10},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'V1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'R4', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
