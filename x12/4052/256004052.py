from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSC', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 9},
    {ID: 'DTP', MIN: 0, MAX: 9},
    {ID: 'NM1', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'BLI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'BLN', MIN: 0, MAX: 9},
            {ID: 'RPA', MIN: 0, MAX: 99999},
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 9},
            ]},
            {ID: 'AM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'III', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 0, MAX: 1},
                    {ID: 'MSG', MIN: 0, MAX: 9},
                    {ID: 'RPA', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'III', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
        {ID: 'ENT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'ADX', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'BLN', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
