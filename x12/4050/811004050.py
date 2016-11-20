from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BIG', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'ITD', MIN: 0, MAX: 5},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'TXI', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DMG', MIN: 0, MAX: 1},
    ]},
    {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FA2', MIN: 1, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'VEH', MIN: 0, MAX: 1},
            {ID: 'SI', MIN: 0, MAX: 8},
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'MEA', MIN: 0, MAX: 20},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 8},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'DMG', MIN: 0, MAX: 1},
        ]},
        {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'TXI', MIN: 0, MAX: 99999},
        ]},
        {ID: 'IT1', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'SI', MIN: 0, MAX: 2},
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'MEA', MIN: 0, MAX: 20},
            {ID: 'INC', MIN: 0, MAX: 1},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'CAD', MIN: 0, MAX: 1},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'LQ', MIN: 0, MAX: 99999},
            {ID: 'LCD', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 1},
            ]},
            {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'TXI', MIN: 0, MAX: 99999},
            ]},
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 3},
                {ID: 'NX2', MIN: 0, MAX: 99999},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'LCD', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SI', MIN: 0, MAX: 2},
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'MEA', MIN: 0, MAX: 20},
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'INC', MIN: 0, MAX: 1},
            {ID: 'ITA', MIN: 0, MAX: 10},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'AMT', MIN: 0, MAX: 15},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 1},
            ]},
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 8},
                {ID: 'PER', MIN: 0, MAX: 3},
                {ID: 'DMG', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'TCD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SI', MIN: 0, MAX: 2},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'ITA', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'USD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SI', MIN: 0, MAX: 2},
            {ID: 'ITA', MIN: 0, MAX: 2},
            {ID: 'TRF', MIN: 0, MAX: 18},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 5},
            {ID: 'PCT', MIN: 0, MAX: 5},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 5},
                {ID: 'PCT', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'TDS', MIN: 1, MAX: 1},
    {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 5},
    ]},
    {ID: 'BAL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'BAL', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'SI', MIN: 0, MAX: 2},
            {ID: 'REF', MIN: 0, MAX: 5},
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
        {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
