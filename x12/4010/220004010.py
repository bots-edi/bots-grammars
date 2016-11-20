from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AH',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B9', MIN: 1, MAX: 1},
    {ID: 'B9A', MIN: 1, MAX: 7},
    {ID: 'L11', MIN: 0, MAX: 99},
    {ID: 'G62', MIN: 0, MAX: 5},
    {ID: 'MS3', MIN: 0, MAX: 99},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'LCD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'ITA', MIN: 0, MAX: 999},
        {ID: 'L8', MIN: 0, MAX: 999},
        {ID: 'L9', MIN: 0, MAX: 999},
        {ID: 'L3', MIN: 0, MAX: 999},
    ]},
    {ID: 'N7', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'N7A', MIN: 0, MAX: 1},
        {ID: 'N7B', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 1},
        {ID: 'M7', MIN: 0, MAX: 2},
    ]},
    {ID: 'S5', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'G62', MIN: 0, MAX: 2},
        {ID: 'L11', MIN: 0, MAX: 99},
        {ID: 'ITA', MIN: 0, MAX: 20},
        {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
        {ID: 'LX', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'LCT', MIN: 0, MAX: 1},
            {ID: 'MAN', MIN: 0, MAX: 10},
            {ID: 'AT5', MIN: 0, MAX: 6},
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'L11', MIN: 0, MAX: 10},
            {ID: 'LAD', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'PO4', MIN: 0, MAX: 1},
                {ID: 'G69', MIN: 0, MAX: 99},
                {ID: 'AT5', MIN: 0, MAX: 6},
                {ID: 'AMT', MIN: 0, MAX: 1},
                {ID: 'L11', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
