from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B2', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 0, MAX: 1},
    {ID: 'Y6', MIN: 0, MAX: 2},
    {ID: 'G1', MIN: 0, MAX: 1},
    {ID: 'G2', MIN: 0, MAX: 1},
    {ID: 'G3', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 100},
    {ID: 'YNQ', MIN: 0, MAX: 10},
    {ID: 'V1', MIN: 0, MAX: 2},
    {ID: 'V3', MIN: 0, MAX: 1},
    {ID: 'M0', MIN: 0, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'M1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'CUR', MIN: 0, MAX: 1},
    ]},
    {ID: 'M2', MIN: 0, MAX: 1},
    {ID: 'C2', MIN: 0, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 20},
    {ID: 'N1', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 3},
    ]},
    {ID: 'R4', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 15},
    ]},
    {ID: 'R2A', MIN: 0, MAX: 25},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'K1', MIN: 0, MAX: 12},
    {ID: 'L11', MIN: 0, MAX: 99},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'L5', MIN: 0, MAX: 999},
    {ID: 'X1', MIN: 0, MAX: 25},
    {ID: 'X2', MIN: 0, MAX: 5},
    {ID: 'C8', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'C8C', MIN: 0, MAX: 5},
        {ID: 'SUP', MIN: 0, MAX: 10},
    ]},
    {ID: 'LX', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'Y2', MIN: 0, MAX: 10},
        {ID: 'N7', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'L4', MIN: 0, MAX: 1},
            {ID: 'N12', MIN: 0, MAX: 1},
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'M7A', MIN: 0, MAX: 100},
            {ID: 'W09', MIN: 0, MAX: 1},
            {ID: 'LH6', MIN: 0, MAX: 6},
            {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'L7', MIN: 0, MAX: 1},
            {ID: 'X1', MIN: 0, MAX: 25},
            {ID: 'X2', MIN: 0, MAX: 5},
            {ID: 'N9', MIN: 0, MAX: 100},
            {ID: 'H1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'H2', MIN: 0, MAX: 10},
            ]},
            {ID: 'LH1', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'LH2', MIN: 0, MAX: 4},
                {ID: 'LH3', MIN: 0, MAX: 10},
                {ID: 'LFH', MIN: 0, MAX: 25},
                {ID: 'LEP', MIN: 0, MAX: 3},
                {ID: 'LH4', MIN: 0, MAX: 1},
                {ID: 'LHT', MIN: 0, MAX: 3},
                {ID: 'LHR', MIN: 0, MAX: 5},
                {ID: 'PER', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'L11', MIN: 0, MAX: 100},
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'PO4', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'MAN', MIN: 0, MAX: 5},
            {ID: 'N9', MIN: 0, MAX: 5},
        ]},
        {ID: 'L0', MIN: 0, MAX: 120, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'N9', MIN: 0, MAX: 100},
            {ID: 'PO4', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 5},
                {ID: 'MAN', MIN: 0, MAX: 5},
                {ID: 'N9', MIN: 0, MAX: 5},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'L4', MIN: 0, MAX: 1},
            {ID: 'LH6', MIN: 0, MAX: 6},
            {ID: 'PAL', MIN: 0, MAX: 3, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 1},
            ]},
            {ID: 'CTP', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'L5', MIN: 0, MAX: 999},
            {ID: 'LIN', MIN: 0, MAX: 1},
            {ID: 'L12', MIN: 0, MAX: 20},
            {ID: 'YNQ', MIN: 0, MAX: 10},
            {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'L7', MIN: 0, MAX: 1},
            {ID: 'SAC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'L9', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'X1', MIN: 0, MAX: 25},
            {ID: 'X2', MIN: 0, MAX: 5},
            {ID: 'C8', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'C8C', MIN: 0, MAX: 5},
                {ID: 'SUP', MIN: 0, MAX: 10},
            ]},
            {ID: 'H1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'H2', MIN: 0, MAX: 10},
            ]},
            {ID: 'LH1', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'LH2', MIN: 0, MAX: 4},
                {ID: 'LH3', MIN: 0, MAX: 10},
                {ID: 'LFH', MIN: 0, MAX: 25},
                {ID: 'LEP', MIN: 0, MAX: 3},
                {ID: 'LH4', MIN: 0, MAX: 1},
                {ID: 'LHT', MIN: 0, MAX: 3},
                {ID: 'LHR', MIN: 0, MAX: 5},
                {ID: 'PER', MIN: 0, MAX: 5},
            ]},
            {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'G61', MIN: 0, MAX: 3},
            ]},
        ]},
    ]},
    {ID: 'L3', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'PWK', MIN: 0, MAX: 50},
        {ID: 'SUP', MIN: 0, MAX: 999},
        {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
        {ID: 'TDS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
        {ID: 'SAC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
        {ID: 'L9', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
        {ID: 'ISS', MIN: 0, MAX: 5},
        {ID: 'V9', MIN: 0, MAX: 10},
        {ID: 'K1', MIN: 0, MAX: 999},
        {ID: 'L11', MIN: 0, MAX: 24},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
