from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BFR', MIN: 1, MAX: 1},
    {ID: 'XPO', MIN: 0, MAX: 99999},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'TAX', MIN: 0, MAX: 3},
    {ID: 'FOB', MIN: 0, MAX: 1},
    {ID: 'CTP', MIN: 0, MAX: 25},
    {ID: 'SAC', MIN: 0, MAX: 25},
    {ID: 'CSH', MIN: 0, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 2},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'PID', MIN: 0, MAX: 200},
    {ID: 'MEA', MIN: 0, MAX: 40},
    {ID: 'PWK', MIN: 0, MAX: 25},
    {ID: 'PKG', MIN: 0, MAX: 25},
    {ID: 'TD1', MIN: 0, MAX: 2},
    {ID: 'TD5', MIN: 0, MAX: 12},
    {ID: 'TD3', MIN: 0, MAX: 12},
    {ID: 'TD4', MIN: 0, MAX: 5},
    {ID: 'MAN', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'FOB', MIN: 0, MAX: 1},
    ]},
    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'UIT', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'PO3', MIN: 0, MAX: 25},
        {ID: 'CTP', MIN: 0, MAX: 25},
        {ID: 'PID', MIN: 0, MAX: 1000},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'PWK', MIN: 0, MAX: 25},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'PRS', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'SAC', MIN: 0, MAX: 25},
        {ID: 'ITD', MIN: 0, MAX: 2},
        {ID: 'TAX', MIN: 0, MAX: 3},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'LDT', MIN: 0, MAX: 12},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'ATH', MIN: 0, MAX: 20},
        {ID: 'TD1', MIN: 0, MAX: 1},
        {ID: 'TD5', MIN: 0, MAX: 12},
        {ID: 'TD3', MIN: 0, MAX: 12},
        {ID: 'TD4', MIN: 0, MAX: 5},
        {ID: 'MAN', MIN: 0, MAX: 10},
        {ID: 'DD', MIN: 0, MAX: 10},
        {ID: 'SLN', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 1000},
            {ID: 'NM1', MIN: 0, MAX: 10},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'FOB', MIN: 0, MAX: 1},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'FST', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'SDQ', MIN: 0, MAX: 50},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
        ]},
        {ID: 'SDP', MIN: 0, MAX: 260, LEVEL: [
            {ID: 'FST', MIN: 0, MAX: 260},
        ]},
        {ID: 'SHP', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
