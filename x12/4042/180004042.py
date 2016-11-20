from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'RDR', MIN: 0, MAX: 1},
    {ID: 'PRF', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'PER', MIN: 0, MAX: 2},
    {ID: 'SAC', MIN: 0, MAX: 10},
    {ID: 'G38', MIN: 0, MAX: 1},
    {ID: 'PKG', MIN: 0, MAX: 5},
    {ID: 'TD1', MIN: 0, MAX: 10},
    {ID: 'TD5', MIN: 0, MAX: 10},
    {ID: 'NTE', MIN: 0, MAX: 5},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'BLI', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 20},
        {ID: 'PID', MIN: 0, MAX: 5},
        {ID: 'RDR', MIN: 0, MAX: 1},
        {ID: 'SAC', MIN: 0, MAX: 10},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'CRC', MIN: 0, MAX: 99999},
        {ID: 'NTE', MIN: 0, MAX: 99999},
        {ID: 'PRF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 15},
        {ID: 'DD', MIN: 0, MAX: 100},
        {ID: 'GF', MIN: 0, MAX: 1},
        {ID: 'TD5', MIN: 0, MAX: 5},
        {ID: 'SDQ', MIN: 0, MAX: 100},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 5},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
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
