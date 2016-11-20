from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RQ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCO', MIN: 1, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 5},
    {ID: 'CTB', MIN: 0, MAX: 5},
    {ID: 'CTP', MIN: 0, MAX: 25},
    {ID: 'FOB', MIN: 0, MAX: 1},
    {ID: 'AMT', MIN: 0, MAX: 99999},
    {ID: 'QTY', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'LDT', MIN: 0, MAX: 99999},
    {ID: 'PWK', MIN: 0, MAX: 99999},
    {ID: 'MTX', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'FOB', MIN: 0, MAX: 1},
    ]},
    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 99999},
    ]},
    {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PO3', MIN: 0, MAX: 99999},
        {ID: 'CTP', MIN: 0, MAX: 99999},
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'SI', MIN: 0, MAX: 99999},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'PWK', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'ITD', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'CTB', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'FOB', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'LDT', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
