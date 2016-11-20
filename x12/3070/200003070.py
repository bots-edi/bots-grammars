from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CRO', MIN: 1, MAX: 1},
    {ID: 'AAA', MIN: 0, MAX: 5},
    {ID: 'DTP', MIN: 0, MAX: 5},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'AMT', MIN: 0, MAX: 3},
    {ID: 'NX1', MIN: 0, MAX: 1},
    {ID: 'NX2', MIN: 0, MAX: 10},
    {ID: 'G32', MIN: 0, MAX: 100},
    {ID: 'N1', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 3},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'LX', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'IN1', MIN: 1, MAX: 15, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 10},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'N10', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'QTY', MIN: 0, MAX: 15},
            {ID: 'YNQ', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 20},
        ]},
        {ID: 'NX1', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'NX2', MIN: 0, MAX: 10},
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'N10', MIN: 0, MAX: 1},
            {ID: 'ARS', MIN: 0, MAX: 1},
            {ID: 'YNQ', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 20},
        ]},
        {ID: 'N1', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 4},
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'YNQ', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 20},
            {ID: 'SOI', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'EMS', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 1},
                {ID: 'N10', MIN: 0, MAX: 1},
                {ID: 'YNQ', MIN: 0, MAX: 1},
                {ID: 'AIN', MIN: 0, MAX: 7, LEVEL: [
                    {ID: 'YNQ', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'TLN', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'N1', MIN: 1, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 4},
        {ID: 'DTP', MIN: 0, MAX: 7},
        {ID: 'TBI', MIN: 0, MAX: 5},
        {ID: 'PPD', MIN: 0, MAX: 15},
        {ID: 'NTE', MIN: 0, MAX: 20},
        {ID: 'AMT', MIN: 0, MAX: 6, LEVEL: [
            {ID: 'NTE', MIN: 0, MAX: 20},
        ]},
    ]},
    {ID: 'RO', MIN: 0, MAX: 500, LEVEL: [
        {ID: 'CDS', MIN: 0, MAX: 1},
        {ID: 'TBI', MIN: 0, MAX: 5},
        {ID: 'DTP', MIN: 0, MAX: 5},
        {ID: 'NTE', MIN: 0, MAX: 20},
        {ID: 'AMT', MIN: 0, MAX: 6, LEVEL: [
            {ID: 'NTE', MIN: 0, MAX: 20},
        ]},
        {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'CCI', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 3},
        {ID: 'MSG', MIN: 0, MAX: 4},
    ]},
    {ID: 'INQ', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'TBI', MIN: 0, MAX: 5},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'YNQ', MIN: 0, MAX: 1},
        {ID: 'NTE', MIN: 0, MAX: 20},
    ]},
    {ID: 'VAR', MIN: 0, MAX: 25, LEVEL: [
        {ID: 'NTE', MIN: 0, MAX: 50},
        {ID: 'IN1', MIN: 0, MAX: 1},
        {ID: 'IN2', MIN: 0, MAX: 10},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'N10', MIN: 0, MAX: 1},
        {ID: 'NX1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'NX2', MIN: 0, MAX: 10},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'EMS', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 2},
        ]},
        {ID: 'SCM', MIN: 0, MAX: 3, LEVEL: [
            {ID: 'SCS', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'NTE', MIN: 1, MAX: 20, LEVEL: [
            {ID: 'TBI', MIN: 0, MAX: 5},
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
