from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BPP', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'CAL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'RSC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'PCT', MIN: 0, MAX: 99999},
        {ID: 'RPA', MIN: 0, MAX: 99999},
    ]},
    {ID: 'TID', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'PCT', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'NM1', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'RSC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'PCT', MIN: 0, MAX: 99999},
            {ID: 'RPA', MIN: 0, MAX: 99999},
            {ID: 'PAM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'MLS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'PCT', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
