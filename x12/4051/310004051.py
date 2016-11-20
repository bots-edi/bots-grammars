from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B3', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 0, MAX: 1},
    {ID: 'Y6', MIN: 0, MAX: 2},
    {ID: 'G3', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 15},
    {ID: 'V1', MIN: 1, MAX: 2},
    {ID: 'M0', MIN: 0, MAX: 1},
    {ID: 'M1', MIN: 0, MAX: 5},
    {ID: 'C2', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'Y2', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'R4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 15},
    ]},
    {ID: 'R2A', MIN: 0, MAX: 25},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'K1', MIN: 0, MAX: 12},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'L5', MIN: 0, MAX: 1},
    {ID: 'C8', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'C8C', MIN: 0, MAX: 5},
    ]},
    {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N7', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'V4', MIN: 0, MAX: 1},
            {ID: 'N12', MIN: 0, MAX: 1},
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'W09', MIN: 0, MAX: 1},
            {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'C3', MIN: 0, MAX: 1},
            ]},
            {ID: 'L7', MIN: 0, MAX: 1},
            {ID: 'X1', MIN: 0, MAX: 1},
            {ID: 'X2', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 3},
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
        {ID: 'L0', MIN: 0, MAX: 120, LEVEL: [
            {ID: 'L5', MIN: 0, MAX: 999},
            {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'C3', MIN: 0, MAX: 1},
            ]},
            {ID: 'L7', MIN: 0, MAX: 1},
            {ID: 'X1', MIN: 0, MAX: 1},
            {ID: 'X2', MIN: 0, MAX: 1},
            {ID: 'C8', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'C8C', MIN: 0, MAX: 5},
            ]},
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
    ]},
    {ID: 'L3', MIN: 1, MAX: 1},
    {ID: 'PWK', MIN: 0, MAX: 25},
    {ID: 'L1', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'C3', MIN: 0, MAX: 1},
    ]},
    {ID: 'V9', MIN: 0, MAX: 10},
    {ID: 'C8', MIN: 0, MAX: 20},
    {ID: 'K1', MIN: 0, MAX: 999},
    {ID: 'L11', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
