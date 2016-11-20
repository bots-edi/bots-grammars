from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'MIS', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'QTY', MIN: 0, MAX: 2},
        {ID: 'AMT', MIN: 0, MAX: 2},
        {ID: 'DTP', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 1, MAX: 10},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 2},
                {ID: 'REF', MIN: 0, MAX: 4},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'REC', MIN: 1, MAX: 1, LEVEL: [
                    {ID: 'N3', MIN: 0, MAX: 1},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'DFI', MIN: 0, MAX: 1},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'AMT', MIN: 0, MAX: 10},
                    {ID: 'INT', MIN: 0, MAX: 1},
                    {ID: 'SOM', MIN: 0, MAX: 10},
                    {ID: 'DTP', MIN: 0, MAX: 14},
                    {ID: 'MRC', MIN: 0, MAX: 2},
                    {ID: 'MSG', MIN: 0, MAX: 11},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'QTY', MIN: 0, MAX: 2},
    {ID: 'AMT', MIN: 0, MAX: 2},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
