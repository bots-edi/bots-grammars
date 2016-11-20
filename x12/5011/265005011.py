from bots.botsconfig import *
from records005011 import recorddefs

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
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 12},
        {ID: 'PDS', MIN: 1, MAX: 20},
        {ID: 'PDE', MIN: 0, MAX: 99999},
        {ID: 'NX1', MIN: 0, MAX: 1},
        {ID: 'NX2', MIN: 0, MAX: 30},
        {ID: 'PRD', MIN: 0, MAX: 1},
        {ID: 'LRQ', MIN: 0, MAX: 1},
        {ID: 'LN1', MIN: 0, MAX: 1},
        {ID: 'MSG', MIN: 0, MAX: 100},
        {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 30},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'FPT', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'PER', MIN: 0, MAX: 4},
            ]},
        ]},
        {ID: 'MCD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 50},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'AMT', MIN: 0, MAX: 2},
        ]},
        {ID: 'TIS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 30},
        ]},
        {ID: 'PWK', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'TIS', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 30},
            {ID: 'MSG', MIN: 0, MAX: 100},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
