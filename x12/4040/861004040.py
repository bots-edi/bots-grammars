from bots.botsconfig import *
from records004040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BRA', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'PRF', MIN: 0, MAX: 25},
    {ID: 'TD1', MIN: 0, MAX: 2},
    {ID: 'TD5', MIN: 0, MAX: 12},
    {ID: 'TD3', MIN: 0, MAX: 12},
    {ID: 'TD4', MIN: 0, MAX: 5},
    {ID: 'MEA', MIN: 0, MAX: 40},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 100},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'FOB', MIN: 0, MAX: 1},
    ]},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FA2', MIN: 1, MAX: 99999},
    ]},
    {ID: 'RCD', MIN: 0, MAX: 200000, LEVEL: [
        {ID: 'SN1', MIN: 0, MAX: 1},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'LIN', MIN: 0, MAX: 100},
        {ID: 'PID', MIN: 0, MAX: 1000},
        {ID: 'PO4', MIN: 0, MAX: 100},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'PRF', MIN: 0, MAX: 25},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'TD1', MIN: 0, MAX: 20},
        {ID: 'TD5', MIN: 0, MAX: 12},
        {ID: 'TD3', MIN: 0, MAX: 12},
        {ID: 'TD4', MIN: 0, MAX: 5},
        {ID: 'SAC', MIN: 0, MAX: 10},
        {ID: 'MAN', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 1000},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 100},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'FOB', MIN: 0, MAX: 1},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
