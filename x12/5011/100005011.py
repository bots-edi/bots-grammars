from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 99999},
    {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 99999},
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'III', MIN: 0, MAX: 9},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LIN', MIN: 0, MAX: 9},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'NM1', MIN: 0, MAX: 99999},
            {ID: 'BLI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'III', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'SI', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'AM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 99999},
            ]},
            {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LIN', MIN: 0, MAX: 9},
                {ID: 'SPA', MIN: 0, MAX: 3},
                {ID: 'III', MIN: 0, MAX: 99999},
            ]},
            {ID: 'N4', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SPA', MIN: 0, MAX: 3},
                {ID: 'AM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
                {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'SPA', MIN: 0, MAX: 3},
                    {ID: 'III', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
