from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'API', MIN: 0, MAX: 2},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 2},
        {ID: 'AMT', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 2},
            {ID: 'PER', MIN: 0, MAX: 2},
        ]},
        {ID: 'N9', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 2},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
            {ID: 'API', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'CRC', MIN: 0, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 1},
                {ID: 'INT', MIN: 0, MAX: 1},
                {ID: 'PCT', MIN: 0, MAX: 1},
                {ID: 'NTE', MIN: 0, MAX: 100},
                {ID: 'VEH', MIN: 0, MAX: 1},
                {ID: 'PID', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
