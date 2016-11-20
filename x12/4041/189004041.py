from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'REF', MIN: 1, MAX: 15, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 1},
    ]},
    {ID: 'IN1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'IN2', MIN: 1, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 10},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'IND', MIN: 0, MAX: 1},
        {ID: 'IMM', MIN: 0, MAX: 99999},
        {ID: 'HC', MIN: 0, MAX: 99999},
        {ID: 'LUI', MIN: 0, MAX: 99999},
        {ID: 'III', MIN: 0, MAX: 10},
        {ID: 'NTE', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 2},
        ]},
        {ID: 'COM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 2},
        ]},
        {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'EMS', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 2},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'ATV', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 2},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'AMT', MIN: 1, MAX: 15, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 1},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'SSE', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DEG', MIN: 0, MAX: 1},
        {ID: 'FOS', MIN: 0, MAX: 5},
    ]},
    {ID: 'LQ', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'PDL', MIN: 0, MAX: 1},
    ]},
    {ID: 'RSD', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N4', MIN: 1, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
    ]},
    {ID: 'RQS', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'MSG', MIN: 0, MAX: 99999},
    ]},
    {ID: 'SST', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'SSE', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 1},
        {ID: 'SUM', MIN: 0, MAX: 5},
        {ID: 'MSG', MIN: 0, MAX: 1},
        {ID: 'SES', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'CRS', MIN: 0, MAX: 50, LEVEL: [
                {ID: 'NTE', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'TST', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'SBT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SRE', MIN: 0, MAX: 3},
            {ID: 'NTE', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'PCL', MIN: 0, MAX: 25, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 1},
        {ID: 'SSE', MIN: 0, MAX: 1},
        {ID: 'SUM', MIN: 0, MAX: 1},
        {ID: 'MSG', MIN: 0, MAX: 1},
        {ID: 'SES', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'CRS', MIN: 0, MAX: 50, LEVEL: [
                {ID: 'NTE', MIN: 0, MAX: 1},
            ]},
            {ID: 'DEG', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'SUM', MIN: 0, MAX: 1},
                {ID: 'FOS', MIN: 0, MAX: 30},
                {ID: 'NTE', MIN: 0, MAX: 30},
            ]},
        ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'MSG', MIN: 1, MAX: 99999},
    ]},
    {ID: 'LT', MIN: 0, MAX: 15, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'LTE', MIN: 0, MAX: 15},
        {ID: 'MSG', MIN: 0, MAX: 99999},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
