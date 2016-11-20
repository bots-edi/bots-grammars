from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCP', MIN: 1, MAX: 1},
    {ID: 'SPI', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 20},
    {ID: 'MSG', MIN: 0, MAX: 99999},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'G61', MIN: 0, MAX: 2},
    ]},
    {ID: 'CBS', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'JIL', MIN: 0, MAX: 1},
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'MSG', MIN: 0, MAX: 99999},
    ]},
    {ID: 'CB1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'G61', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'PL', MIN: 0, MAX: 99999},
    {ID: 'HL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 1},
    ]},
    {ID: 'PD', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'SPI', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'PDD', MIN: 0, MAX: 99999},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'G61', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 4},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
