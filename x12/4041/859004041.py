from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B3', MIN: 1, MAX: 1},
    {ID: 'B3A', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 30},
    {ID: 'CM', MIN: 0, MAX: 1},
    {ID: 'Y6', MIN: 0, MAX: 4},
    {ID: 'Y7', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'NA', MIN: 0, MAX: 30},
    {ID: 'F9', MIN: 0, MAX: 1},
    {ID: 'D9', MIN: 0, MAX: 1},
    {ID: 'R1', MIN: 0, MAX: 1},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'PS', MIN: 0, MAX: 5},
    {ID: 'H6', MIN: 0, MAX: 6},
    {ID: 'M1', MIN: 0, MAX: 1},
    {ID: 'M2', MIN: 0, MAX: 1},
    {ID: 'L7', MIN: 0, MAX: 30},
    {ID: 'NTE', MIN: 0, MAX: 30},
    {ID: 'XH', MIN: 0, MAX: 1},
    {ID: 'P1', MIN: 0, MAX: 1},
    {ID: 'ITA', MIN: 0, MAX: 1},
    {ID: 'N8', MIN: 0, MAX: 499},
    {ID: 'R9', MIN: 0, MAX: 1},
    {ID: 'H1', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'H2', MIN: 0, MAX: 2},
    ]},
    {ID: 'N7', MIN: 0, MAX: 600, LEVEL: [
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'N5', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'IC', MIN: 0, MAX: 1},
        {ID: 'VC', MIN: 0, MAX: 36},
        {ID: 'G4', MIN: 0, MAX: 1},
        {ID: 'GA', MIN: 0, MAX: 15},
    ]},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'S5', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'G62', MIN: 0, MAX: 6},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'H6', MIN: 0, MAX: 6},
        {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
        {ID: 'L5', MIN: 0, MAX: 10},
        {ID: 'L0', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'L1', MIN: 0, MAX: 20},
            {ID: 'MEA', MIN: 0, MAX: 5},
        ]},
        {ID: 'L7', MIN: 0, MAX: 10},
        {ID: 'SL1', MIN: 0, MAX: 1},
        {ID: 'R1', MIN: 0, MAX: 1},
        {ID: 'LH', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'X1', MIN: 0, MAX: 6},
        {ID: 'X2', MIN: 0, MAX: 1},
        {ID: 'P1', MIN: 0, MAX: 1},
        {ID: 'POD', MIN: 0, MAX: 1},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'ITA', MIN: 0, MAX: 20},
        {ID: 'L8', MIN: 0, MAX: 1},
        {ID: 'V9', MIN: 0, MAX: 1},
        {ID: 'P2', MIN: 0, MAX: 1},
        {ID: 'N7', MIN: 0, MAX: 5},
        {ID: 'H1', MIN: 0, MAX: 3, LEVEL: [
            {ID: 'H2', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'L3', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
