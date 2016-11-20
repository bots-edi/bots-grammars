from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RW',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ZR', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 30},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 2},
    {ID: 'PER', MIN: 0, MAX: 20},
    {ID: 'BX', MIN: 0, MAX: 1},
    {ID: 'BNX', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 30},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'N7', MIN: 1, MAX: 500, LEVEL: [
            {ID: 'VC', MIN: 0, MAX: 21},
            {ID: 'IC', MIN: 0, MAX: 1},
            {ID: 'M12', MIN: 0, MAX: 1},
            {ID: 'G4', MIN: 0, MAX: 1},
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'N5', MIN: 0, MAX: 1},
        ]},
        {ID: 'N8', MIN: 1, MAX: 499},
        {ID: 'N8A', MIN: 0, MAX: 499},
        {ID: 'V9', MIN: 0, MAX: 1},
        {ID: 'F9', MIN: 1, MAX: 1},
        {ID: 'D9', MIN: 1, MAX: 1},
        {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'BL', MIN: 0, MAX: 1},
        ]},
        {ID: 'S1', MIN: 0, MAX: 6, LEVEL: [
            {ID: 'S9', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'PI', MIN: 0, MAX: 0, LEVEL: [
        {ID: 'R2', MIN: 1, MAX: 13, LEVEL: [
            {ID: 'R2B', MIN: 0, MAX: 4, LEVEL: [
                {ID: 'R2C', MIN: 0, MAX: 20},
                {ID: 'R2D', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'RE', MIN: 0, MAX: 12},
        {ID: 'R9', MIN: 0, MAX: 1},
        {ID: 'H3', MIN: 0, MAX: 6},
        {ID: 'PS', MIN: 0, MAX: 5},
        {ID: 'LX', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'L5', MIN: 0, MAX: 15},
            {ID: 'L0', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 3},
                {ID: 'L1', MIN: 0, MAX: 10},
                {ID: 'PI', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'T1', MIN: 0, MAX: 64, LEVEL: [
            {ID: 'T2', MIN: 0, MAX: 30},
            {ID: 'T3', MIN: 0, MAX: 12},
            {ID: 'T6', MIN: 0, MAX: 1},
            {ID: 'T8', MIN: 0, MAX: 99},
        ]},
        {ID: 'L3', MIN: 0, MAX: 1},
        {ID: 'L1A', MIN: 0, MAX: 13},
        {ID: 'X7', MIN: 0, MAX: 10},
        {ID: 'GA', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
