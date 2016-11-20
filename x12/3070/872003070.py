from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 1, MAX: 1},
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'MII', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'LRQ', MIN: 1, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 5},
            {ID: 'PEX', MIN: 0, MAX: 20},
            {ID: 'LN1', MIN: 1, MAX: 1},
            {ID: 'RLD', MIN: 0, MAX: 5},
            {ID: 'PRD', MIN: 1, MAX: 1},
            {ID: 'PAY', MIN: 0, MAX: 1},
            {ID: 'RAT', MIN: 0, MAX: 1},
            {ID: 'REA', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 10},
            ]},
            {ID: 'MCD', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 10},
            ]},
            {ID: 'BUY', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'TBA', MIN: 0, MAX: 10},
            ]},
            {ID: 'PRJ', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'PER', MIN: 0, MAX: 10},
            ]},
            {ID: 'PWK', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 12},
                {ID: 'PER', MIN: 0, MAX: 3},
            ]},
            {ID: 'NX1', MIN: 1, MAX: 5, LEVEL: [
                {ID: 'NX2', MIN: 1, MAX: 30},
                {ID: 'PAS', MIN: 1, MAX: 5, LEVEL: [
                    {ID: 'N1', MIN: 0, MAX: 2},
                    {ID: 'PER', MIN: 0, MAX: 10},
                    {ID: 'MSG', MIN: 0, MAX: 10},
                ]},
            ]},
            {ID: 'IN1', MIN: 1, MAX: 12, LEVEL: [
                {ID: 'IN2', MIN: 1, MAX: 10},
                {ID: 'YNQ', MIN: 0, MAX: 5},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 1},
                {ID: 'N10', MIN: 0, MAX: 1},
                {ID: 'BFS', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
