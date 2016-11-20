from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BR', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'LM', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'N1', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 5},
    ]},
    {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 1, MAX: 99999},
        {ID: 'PO1', MIN: 0, MAX: 99999},
        {ID: 'PWK', MIN: 0, MAX: 1},
        {ID: 'DD', MIN: 0, MAX: 100},
        {ID: 'GF', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 20},
        {ID: 'MAN', MIN: 0, MAX: 5},
        {ID: 'LIN', MIN: 0, MAX: 99999},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'G69', MIN: 0, MAX: 99999},
        {ID: 'NTE', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 50, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LM', MIN: 0, MAX: 50, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
        ]},
        {ID: 'N1', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'G61', MIN: 0, MAX: 5},
        ]},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'G62', MIN: 0, MAX: 10},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'R4', MIN: 0, MAX: 1},
            {ID: 'LM', MIN: 0, MAX: 50, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
