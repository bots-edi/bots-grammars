from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'OW',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'W05', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'NTE', MIN: 0, MAX: 99999},
    {ID: 'W09', MIN: 0, MAX: 1},
    {ID: 'W66', MIN: 0, MAX: 1},
    {ID: 'W6', MIN: 0, MAX: 1},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'W01', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'G69', MIN: 0, MAX: 5},
        {ID: 'N9', MIN: 0, MAX: 200},
        {ID: 'W20', MIN: 0, MAX: 3},
        {ID: 'AT', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 10},
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'G66', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 3},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'G62', MIN: 0, MAX: 10},
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
        ]},
    ]},
    {ID: 'W76', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
