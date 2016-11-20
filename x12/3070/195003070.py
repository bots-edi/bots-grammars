from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'LA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'QTY', MIN: 0, MAX: 99999},
    {ID: 'PWK', MIN: 0, MAX: 99999},
    {ID: 'CRC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'NTE', MIN: 0, MAX: 99999},
    ]},
    {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'MSG', MIN: 0, MAX: 99999},
    ]},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 3},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'NTE', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
        {ID: 'CRC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LIE', MIN: 0, MAX: 99999},
        ]},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LIE', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 3},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'CRC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999},
            ]},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 3},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
