from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'WA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 4, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 99999},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'PSC', MIN: 0, MAX: 99999},
            {ID: 'SSS', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 2},
            {ID: 'PER', MIN: 0, MAX: 2},
        ]},
        {ID: 'PRR', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'LIN', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'RC', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'PSC', MIN: 0, MAX: 99999},
            {ID: 'SSS', MIN: 0, MAX: 99999},
            {ID: 'CID', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'TMD', MIN: 0, MAX: 99999},
                {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                    {ID: 'LIN', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
        {ID: 'REP', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'N1', MIN: 0, MAX: 2},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'RC', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'LIN', MIN: 0, MAX: 99999},
            {ID: 'ITA', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'PRT', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'LIN', MIN: 0, MAX: 99999},
            ]},
            {ID: 'IT1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LIN', MIN: 0, MAX: 99999},
                {ID: 'N1', MIN: 0, MAX: 99999},
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'PRT', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'ITA', MIN: 0, MAX: 99999},
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'AMT', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'TDS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'TXI', MIN: 0, MAX: 99999},
        {ID: 'CUR', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
