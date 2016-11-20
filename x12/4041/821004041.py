from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FR',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 4},
    {ID: 'TRN', MIN: 1, MAX: 2},
    {ID: 'N1', MIN: 0, MAX: 2},
    {ID: 'PER', MIN: 0, MAX: 99999},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FA2', MIN: 1, MAX: 99999},
    ]},
    {ID: 'ENT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 99999},
            {ID: 'N3', MIN: 0, MAX: 99999},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
        {ID: 'ACT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 3},
                ]},
            ]},
            {ID: 'RTE', MIN: 0, MAX: 13, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'BLN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AVA', MIN: 0, MAX: 99999},
            ]},
            {ID: 'TSU', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AVA', MIN: 0, MAX: 99999},
            ]},
            {ID: 'FIR', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'AVA', MIN: 0, MAX: 99999},
                {ID: 'TRN', MIN: 0, MAX: 1},
                {ID: 'N1', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'CTP', MIN: 0, MAX: 99999},
                {ID: 'RTE', MIN: 0, MAX: 99999},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 99999},
                    {ID: 'N3', MIN: 0, MAX: 99999},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 1},
                    {ID: 'N9', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
