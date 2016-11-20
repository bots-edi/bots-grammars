from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'TRN', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 10},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'AM1', MIN: 0, MAX: 99999},
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'LN1', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'PWK', MIN: 0, MAX: 99999},
        {ID: 'NTE', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 10},
            {ID: 'DTP', MIN: 0, MAX: 2},
        ]},
        {ID: 'NX1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 1, MAX: 99999},
            {ID: 'DTP', MIN: 1, MAX: 7},
            {ID: 'YNQ', MIN: 0, MAX: 16},
            {ID: 'REF', MIN: 0, MAX: 5},
            {ID: 'PDS', MIN: 0, MAX: 99999},
            {ID: 'PDE', MIN: 0, MAX: 99999},
            {ID: 'PEX', MIN: 0, MAX: 5},
            {ID: 'REC', MIN: 0, MAX: 1},
            {ID: 'REA', MIN: 0, MAX: 1},
            {ID: 'III', MIN: 0, MAX: 30},
            {ID: 'AM1', MIN: 0, MAX: 99999},
            {ID: 'API', MIN: 0, MAX: 10},
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'QTY', MIN: 0, MAX: 10},
            {ID: 'PCT', MIN: 0, MAX: 4},
            {ID: 'NTE', MIN: 0, MAX: 10},
            {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 2},
            ]},
            {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'IN2', MIN: 0, MAX: 10},
                {ID: 'III', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 2},
                {ID: 'DTM', MIN: 0, MAX: 2},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
