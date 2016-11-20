from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCT', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'CTP', MIN: 0, MAX: 100},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'CTB', MIN: 0, MAX: 25},
    {ID: 'CUR', MIN: 0, MAX: 5},
    {ID: 'ITD', MIN: 0, MAX: 2},
    {ID: 'LDT', MIN: 0, MAX: 99999},
    {ID: 'SAC', MIN: 0, MAX: 25},
    {ID: 'FOB', MIN: 0, MAX: 1},
    {ID: 'G93', MIN: 0, MAX: 50},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 10},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 700000, LEVEL: [
        {ID: 'G53', MIN: 0, MAX: 1},
        {ID: 'SLN', MIN: 0, MAX: 100},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'CTB', MIN: 0, MAX: 25},
        {ID: 'PID', MIN: 0, MAX: 200},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'TD4', MIN: 0, MAX: 10},
        {ID: 'ITD', MIN: 0, MAX: 2},
        {ID: 'LDT', MIN: 0, MAX: 1},
        {ID: 'SAC', MIN: 0, MAX: 25},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'TC2', MIN: 0, MAX: 2},
        {ID: 'TXI', MIN: 0, MAX: 1},
        {ID: 'G39', MIN: 0, MAX: 1},
        {ID: 'G55', MIN: 0, MAX: 1},
        {ID: 'G54', MIN: 0, MAX: 1},
        {ID: 'CTP', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'G40', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'G36', MIN: 0, MAX: 1},
            {ID: 'LDT', MIN: 0, MAX: 1},
            {ID: 'CUR', MIN: 0, MAX: 5},
            {ID: 'PO4', MIN: 0, MAX: 1},
            {ID: 'CTB', MIN: 0, MAX: 5},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'G43', MIN: 0, MAX: 9999},
            {ID: 'SAC', MIN: 0, MAX: 5},
            {ID: 'G26', MIN: 0, MAX: 99},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'DTM', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'PKL', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'CTP', MIN: 0, MAX: 1},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
