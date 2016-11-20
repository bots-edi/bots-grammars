from bots.botsconfig import *
from records004040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'MSG', MIN: 0, MAX: 99999},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'DTP', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LX', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'VEH', MIN: 0, MAX: 1},
            {ID: 'VAT', MIN: 0, MAX: 20},
            {ID: 'DVI', MIN: 0, MAX: 1},
            {ID: 'SI', MIN: 0, MAX: 8},
            {ID: 'PID', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 5},
            {ID: 'AD1', MIN: 0, MAX: 20},
            {ID: 'DTP', MIN: 0, MAX: 20},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 1},
            ]},
            {ID: 'EFI', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'BIN', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'DMA', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'NX2', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
        {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SI', MIN: 0, MAX: 2},
            {ID: 'PID', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 10},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'AD1', MIN: 0, MAX: 20},
            {ID: 'CRC', MIN: 0, MAX: 50},
            {ID: 'PCT', MIN: 0, MAX: 10},
            {ID: 'PDP', MIN: 0, MAX: 99999},
            {ID: 'PDR', MIN: 0, MAX: 99999},
            {ID: 'PDS', MIN: 0, MAX: 99999},
            {ID: 'SUP', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'AD1', MIN: 0, MAX: 99999},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 1},
            ]},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 10},
                {ID: 'AD1', MIN: 0, MAX: 10},
                {ID: 'PCT', MIN: 0, MAX: 10},
            ]},
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'DMA', MIN: 0, MAX: 1},
                {ID: 'NX2', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 99999},
            ]},
            {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 5},
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'TDS', MIN: 1, MAX: 1},
    {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'CUR', MIN: 0, MAX: 1},
    ]},
    {ID: 'BAL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 99999},
    ]},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'BAL', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 99999},
        ]},
        {ID: 'ITA', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
