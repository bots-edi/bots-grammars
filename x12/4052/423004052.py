from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 3},
    {ID: 'LQ', MIN: 0, MAX: 1},
    {ID: 'QTY', MIN: 0, MAX: 3},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'LX', MIN: 0, MAX: 150, LEVEL: [
        {ID: 'XD', MIN: 0, MAX: 1},
        {ID: 'N7', MIN: 0, MAX: 500, LEVEL: [
            {ID: 'YNQ', MIN: 0, MAX: 10},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'XD', MIN: 0, MAX: 1},
            {ID: 'R2', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'L5', MIN: 0, MAX: 5},
            {ID: 'D9', MIN: 0, MAX: 1},
            {ID: 'F9', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'LH2', MIN: 0, MAX: 2},
            {ID: 'LH6', MIN: 0, MAX: 6},
            {ID: 'QTY', MIN: 0, MAX: 2},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'LH1', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'LH2', MIN: 0, MAX: 4},
                {ID: 'LH3', MIN: 0, MAX: 10},
                {ID: 'LFH', MIN: 0, MAX: 20},
                {ID: 'LEP', MIN: 0, MAX: 3},
                {ID: 'LH4', MIN: 0, MAX: 1},
                {ID: 'LHT', MIN: 0, MAX: 3},
                {ID: 'LHR', MIN: 0, MAX: 5},
                {ID: 'PER', MIN: 0, MAX: 5},
                {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'PER', MIN: 0, MAX: 2},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
