from bots.botsconfig import *
from records004040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 1},
    {ID: 'MSG', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'SI', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 2},
        {ID: 'RLT', MIN: 0, MAX: 1},
        {ID: 'REC', MIN: 0, MAX: 1},
        {ID: 'LN', MIN: 0, MAX: 1},
        {ID: 'PWK', MIN: 0, MAX: 5},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'DTP', MIN: 0, MAX: 10},
        {ID: 'AMT', MIN: 0, MAX: 20},
        {ID: 'NTE', MIN: 0, MAX: 5},
        {ID: 'CTP', MIN: 0, MAX: 1},
        {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 12},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 5},
        ]},
        {ID: 'NX1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 1, MAX: 99999},
            {ID: 'PDS', MIN: 0, MAX: 99999},
            {ID: 'PDE', MIN: 0, MAX: 99999},
            {ID: 'REA', MIN: 0, MAX: 1},
            {ID: 'III', MIN: 0, MAX: 5},
            {ID: 'REC', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 2},
            {ID: 'YNQ', MIN: 0, MAX: 20},
            {ID: 'NTE', MIN: 0, MAX: 10},
            {ID: 'PWK', MIN: 0, MAX: 2},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'AMT', MIN: 0, MAX: 20},
            {ID: 'CTP', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 10},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
                {ID: 'CRC', MIN: 0, MAX: 1},
                {ID: 'DFI', MIN: 0, MAX: 5},
                {ID: 'YNQ', MIN: 0, MAX: 10},
                {ID: 'AMT', MIN: 0, MAX: 5},
                {ID: 'NTE', MIN: 0, MAX: 10},
                {ID: 'OBI', MIN: 0, MAX: 99999},
                {ID: 'AIN', MIN: 0, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 3},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
