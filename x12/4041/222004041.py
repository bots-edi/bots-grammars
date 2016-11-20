from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'SCN', MIN: 1, MAX: 1},
    {ID: 'L11', MIN: 0, MAX: 5},
    {ID: 'G62', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 3},
    ]},
    {ID: 'PLC', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N7', MIN: 1, MAX: 10},
        {ID: 'L11', MIN: 0, MAX: 10},
        {ID: 'AT5', MIN: 0, MAX: 6},
        {ID: 'NTE', MIN: 0, MAX: 10},
        {ID: 'LX', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'L11', MIN: 0, MAX: 5},
            {ID: 'AT3', MIN: 1, MAX: 1},
        ]},
        {ID: 'S5', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'L11', MIN: 0, MAX: 10},
            {ID: 'G62', MIN: 0, MAX: 10},
            {ID: 'AT5', MIN: 0, MAX: 6},
            {ID: 'PLD', MIN: 0, MAX: 2},
            {ID: 'NTE', MIN: 0, MAX: 10},
            {ID: 'N1', MIN: 1, MAX: 1, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'G61', MIN: 0, MAX: 3},
            ]},
            {ID: 'LAD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'G61', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'L11', MIN: 0, MAX: 5},
                    {ID: 'LH6', MIN: 0, MAX: 6},
                    {ID: 'LH1', MIN: 1, MAX: 25, LEVEL: [
                        {ID: 'LH2', MIN: 0, MAX: 4},
                        {ID: 'LH3', MIN: 0, MAX: 10},
                        {ID: 'LFH', MIN: 0, MAX: 20},
                        {ID: 'LEP', MIN: 0, MAX: 3},
                        {ID: 'LH4', MIN: 0, MAX: 1},
                        {ID: 'LHT', MIN: 0, MAX: 3},
                    ]},
                ]},
            ]},
            {ID: 'LX', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'L11', MIN: 0, MAX: 10},
                {ID: 'AT3', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
