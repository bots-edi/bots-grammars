from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SW',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'W06', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 5},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'W27', MIN: 0, MAX: 1},
    {ID: 'W6', MIN: 0, MAX: 1},
    {ID: 'W28', MIN: 0, MAX: 1},
    {ID: 'W10', MIN: 0, MAX: 10},
    {ID: 'G72', MIN: 0, MAX: 5},
    {ID: 'TD1', MIN: 0, MAX: 5},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'MAN', MIN: 0, MAX: 99999},
        {ID: 'PAL', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 5},
        {ID: 'W12', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'G69', MIN: 0, MAX: 5},
            {ID: 'N9', MIN: 0, MAX: 200},
            {ID: 'G62', MIN: 0, MAX: 10},
            {ID: 'QTY', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'R4', MIN: 0, MAX: 5},
            {ID: 'W27', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
            ]},
            {ID: 'G72', MIN: 0, MAX: 5},
            {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'N9', MIN: 0, MAX: 99999},
                    {ID: 'G62', MIN: 0, MAX: 10},
                    {ID: 'N1', MIN: 0, MAX: 1},
                    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'LQ', MIN: 1, MAX: 100},
                    ]},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
            {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'FA2', MIN: 1, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'W03', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
