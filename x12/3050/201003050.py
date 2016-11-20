from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'LRQ', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 3},
        {ID: 'YNQ', MIN: 1, MAX: 4},
        {ID: 'N1', MIN: 1, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'III', MIN: 0, MAX: 2},
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'RLD', MIN: 0, MAX: 15},
        {ID: 'MCD', MIN: 0, MAX: 1},
        {ID: 'NX1', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'NX2', MIN: 1, MAX: 30},
            {ID: 'REA', MIN: 0, MAX: 1},
            {ID: 'PDS', MIN: 0, MAX: 10},
            {ID: 'PDE', MIN: 0, MAX: 50},
        ]},
        {ID: 'PEX', MIN: 1, MAX: 20, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 1},
        ]},
        {ID: 'AMT', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 1},
        ]},
        {ID: 'IN1', MIN: 1, MAX: 15, LEVEL: [
            {ID: 'IN2', MIN: 1, MAX: 10},
            {ID: 'YNQ', MIN: 1, MAX: 19},
            {ID: 'DTP', MIN: 1, MAX: 3},
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'N10', MIN: 0, MAX: 1},
            {ID: 'MSG', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'FTH', MIN: 0, MAX: 1},
            {ID: 'AIN', MIN: 0, MAX: 10},
            {ID: 'PPY', MIN: 0, MAX: 20},
            {ID: 'PEX', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 1},
            ]},
            {ID: 'NX1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'NX2', MIN: 1, MAX: 30},
                {ID: 'N10', MIN: 0, MAX: 1},
                {ID: 'ARS', MIN: 0, MAX: 1},
            ]},
            {ID: 'N1', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
                {ID: 'ACT', MIN: 0, MAX: 10},
                {ID: 'YNQ', MIN: 0, MAX: 1},
                {ID: 'EMS', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 2},
                {ID: 'DTP', MIN: 0, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 1},
            ]},
            {ID: 'REA', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'AMT', MIN: 1, MAX: 6},
                {ID: 'NX1', MIN: 1, MAX: 1},
                {ID: 'NX2', MIN: 1, MAX: 30},
            ]},
            {ID: 'CDA', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'YNQ', MIN: 1, MAX: 1},
                {ID: 'N1', MIN: 1, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
            ]},
            {ID: 'FAA', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'N1', MIN: 1, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 1},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'AMT', MIN: 1, MAX: 10, LEVEL: [
                    {ID: 'MSG', MIN: 0, MAX: 1},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
        ]},
        {ID: 'LX', MIN: 1, MAX: 5, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
