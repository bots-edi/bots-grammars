from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCD', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'PER', MIN: 0, MAX: 99999},
    {ID: 'ITD', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'FOB', MIN: 0, MAX: 1},
    {ID: 'SHD', MIN: 0, MAX: 99999},
    {ID: 'SAC', MIN: 0, MAX: 25},
    {ID: 'N1', MIN: 1, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'AMT', MIN: 0, MAX: 10},
    ]},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FA2', MIN: 1, MAX: 99999},
    ]},
    {ID: 'CDD', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'SAC', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'N11', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'PCT', MIN: 0, MAX: 2},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 10},
                {ID: 'PCT', MIN: 0, MAX: 2},
            ]},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
