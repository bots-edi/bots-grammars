from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BIG', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'YNQ', MIN: 0, MAX: 10},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'ITD', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'FOB', MIN: 0, MAX: 1},
    {ID: 'PID', MIN: 0, MAX: 200},
    {ID: 'MEA', MIN: 0, MAX: 40},
    {ID: 'PWK', MIN: 0, MAX: 25},
    {ID: 'PKG', MIN: 0, MAX: 25},
    {ID: 'L7', MIN: 0, MAX: 1},
    {ID: 'AT', MIN: 0, MAX: 99999},
    {ID: 'BAL', MIN: 0, MAX: 2},
    {ID: 'INC', MIN: 0, MAX: 1},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'N9', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'MSG', MIN: 1, MAX: 10},
    ]},
    {ID: 'V1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'R4', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'IT1', MIN: 0, MAX: 200000, LEVEL: [
        {ID: 'CRC', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 5},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'IT3', MIN: 0, MAX: 5},
        {ID: 'TXI', MIN: 0, MAX: 10},
        {ID: 'CTP', MIN: 0, MAX: 25},
        {ID: 'PAM', MIN: 0, MAX: 10},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'PID', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 10},
        ]},
        {ID: 'PWK', MIN: 0, MAX: 25},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'ITD', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'YNQ', MIN: 0, MAX: 10},
        {ID: 'PER', MIN: 0, MAX: 5},
        {ID: 'SDQ', MIN: 0, MAX: 500},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'CAD', MIN: 0, MAX: 99999},
        {ID: 'L7', MIN: 0, MAX: 99999},
        {ID: 'SR', MIN: 0, MAX: 1},
        {ID: 'AT', MIN: 0, MAX: 99999},
        {ID: 'SAC', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'TXI', MIN: 0, MAX: 10},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PID', MIN: 0, MAX: 1000},
            {ID: 'SAC', MIN: 0, MAX: 25},
            {ID: 'TC2', MIN: 0, MAX: 2},
            {ID: 'TXI', MIN: 0, MAX: 10},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'V1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'R4', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'TDS', MIN: 1, MAX: 1},
    {ID: 'TXI', MIN: 0, MAX: 10},
    {ID: 'CAD', MIN: 0, MAX: 1},
    {ID: 'SAC', MIN: 0, MAX: 25, LEVEL: [
        {ID: 'TXI', MIN: 0, MAX: 10},
    ]},
    {ID: 'ISS', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PID', MIN: 0, MAX: 1},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
