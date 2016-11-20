from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BR', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 5},
    {ID: 'NTE', MIN: 0, MAX: 5},
    {ID: 'LM', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'N1', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 5},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'CS', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'RCD', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'G62', MIN: 0, MAX: 10},
            {ID: 'GF', MIN: 0, MAX: 1},
            {ID: 'DD', MIN: 0, MAX: 100},
            {ID: 'N9', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 5},
            {ID: 'G66', MIN: 0, MAX: 5},
            {ID: 'LM', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
            {ID: 'CS', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PO4', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 5},
                {ID: 'G62', MIN: 0, MAX: 5},
                {ID: 'G69', MIN: 0, MAX: 5},
                {ID: 'LM', MIN: 0, MAX: 25, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
                ]},
            ]},
            {ID: 'N1', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'G61', MIN: 0, MAX: 1},
            ]},
            {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'G62', MIN: 0, MAX: 10},
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'LM', MIN: 0, MAX: 50, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
                ]},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'LM', MIN: 0, MAX: 100, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
                ]},
            ]},
            {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'FA2', MIN: 1, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
