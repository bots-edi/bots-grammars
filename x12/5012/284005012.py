from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IH',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'PWK', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'YNQ', MIN: 0, MAX: 99999},
        {ID: 'TC2', MIN: 0, MAX: 1},
        {ID: 'H1', MIN: 0, MAX: 1},
        {ID: 'LH2', MIN: 0, MAX: 1},
        {ID: 'LH3', MIN: 0, MAX: 1},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'MAN', MIN: 0, MAX: 99999},
        {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'III', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'LOD', MIN: 0, MAX: 1},
            {ID: 'SRE', MIN: 0, MAX: 1},
            {ID: 'VEH', MIN: 0, MAX: 1},
            {ID: 'DVI', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'EMS', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 99999},
            {ID: 'DMA', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'LIE', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'MTX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
