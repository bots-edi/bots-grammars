from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CW',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'ERP', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'COM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'SCT', MIN: 0, MAX: 99999},
        {ID: 'OPX', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DEG', MIN: 0, MAX: 99999},
        {ID: 'ISI', MIN: 0, MAX: 99999},
        {ID: 'LQ', MIN: 0, MAX: 99999},
        {ID: 'EDF', MIN: 0, MAX: 99999},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PPA', MIN: 0, MAX: 99999},
            {ID: 'COM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'YNQ', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'PCT', MIN: 0, MAX: 99999},
        ]},
        {ID: 'FOS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DEG', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 99999},
        ]},
        {ID: 'SP', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'NM1', MIN: 0, MAX: 99999},
        ]},
        {ID: 'SLA', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FOS', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'ENM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FOS', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'NTE', MIN: 0, MAX: 99999},
        ]},
        {ID: 'ATV', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
