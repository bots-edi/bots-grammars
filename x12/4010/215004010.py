from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'UP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'BLR', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'L11', MIN: 1, MAX: 10},
    {ID: 'G62', MIN: 0, MAX: 6},
    {ID: 'N1', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 2},
        {ID: 'L11', MIN: 1, MAX: 10},
        {ID: 'PER', MIN: 0, MAX: 10},
        {ID: 'X1', MIN: 0, MAX: 10},
        {ID: 'X2', MIN: 0, MAX: 10},
    ]},
    {ID: 'SMD', MIN: 1, MAX: 999999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 20},
        {ID: 'L5', MIN: 0, MAX: 10},
        {ID: 'MS6', MIN: 0, MAX: 1},
        {ID: 'MS5', MIN: 0, MAX: 5},
        {ID: 'MS4', MIN: 0, MAX: 1},
        {ID: 'ACS', MIN: 0, MAX: 10},
        {ID: 'NTE', MIN: 0, MAX: 10},
        {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'L11', MIN: 0, MAX: 10},
            {ID: 'G61', MIN: 0, MAX: 10},
            {ID: 'X1', MIN: 0, MAX: 10},
            {ID: 'X2', MIN: 0, MAX: 10},
            {ID: 'R4', MIN: 0, MAX: 10},
        ]},
        {ID: 'CD3', MIN: 1, MAX: 999999, LEVEL: [
            {ID: 'MAN', MIN: 0, MAX: 100},
            {ID: 'MS4', MIN: 0, MAX: 1},
            {ID: 'L11', MIN: 0, MAX: 10},
            {ID: 'L5', MIN: 0, MAX: 10},
            {ID: 'ACS', MIN: 0, MAX: 10},
            {ID: 'NTE', MIN: 0, MAX: 10},
        ]},
        {ID: 'AT6', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'MS5', MIN: 0, MAX: 1},
            {ID: 'IT1', MIN: 0, MAX: 1},
            {ID: 'CGS', MIN: 0, MAX: 10},
            {ID: 'L11', MIN: 0, MAX: 1},
            {ID: 'PID', MIN: 0, MAX: 1000},
            {ID: 'TXI', MIN: 0, MAX: 10},
            {ID: 'MS4', MIN: 0, MAX: 1},
            {ID: 'L5', MIN: 0, MAX: 1},
            {ID: 'SLN', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'L11', MIN: 0, MAX: 10},
                {ID: 'PID', MIN: 0, MAX: 10},
                {ID: 'TC2', MIN: 0, MAX: 10},
                {ID: 'TXI', MIN: 0, MAX: 10},
                {ID: 'NTE', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
