from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BIA', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'MEA', MIN: 0, MAX: 20},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 10000, LEVEL: [
        {ID: 'PID', MIN: 0, MAX: 200},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'CTP', MIN: 0, MAX: 25},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'SAC', MIN: 0, MAX: 25},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'SDQ', MIN: 0, MAX: 500},
        {ID: 'MAN', MIN: 0, MAX: 1},
        {ID: 'UIT', MIN: 0, MAX: 5},
        {ID: 'CS', MIN: 0, MAX: 1},
        {ID: 'DD', MIN: 0, MAX: 99999},
        {ID: 'G53', MIN: 0, MAX: 1},
        {ID: 'PCT', MIN: 0, MAX: 99999},
        {ID: 'LDT', MIN: 0, MAX: 12},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'MEA', MIN: 0, MAX: 40},
            {ID: 'PKG', MIN: 0, MAX: 25},
            {ID: 'MAN', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 40},
            ]},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'UIT', MIN: 0, MAX: 12},
            {ID: 'MEA', MIN: 0, MAX: 25},
            {ID: 'LDT', MIN: 0, MAX: 12},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'SCH', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 25},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'REF', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                    {ID: 'N1', MIN: 0, MAX: 1},
                    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'LQ', MIN: 1, MAX: 100},
                    ]},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
