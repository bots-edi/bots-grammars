#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD07AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'GEI', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'QTY', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'PNA', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'COT', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'DLI', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
        ]},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'PCD', MIN: 1, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 1, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 0, MAX: 9},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'PAI', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
