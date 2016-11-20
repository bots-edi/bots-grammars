from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BDD', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 20},
    {ID: 'K1', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 20},
    ]},
    {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 5},
        {ID: 'G62', MIN: 0, MAX: 1},
        {ID: 'G07', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'G61', MIN: 0, MAX: 1},
            {ID: 'Q8', MIN: 1, MAX: 999, LEVEL: [
                {ID: 'G62', MIN: 0, MAX: 1},
                {ID: 'K1', MIN: 0, MAX: 1},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
                        {ID: 'N2', MIN: 0, MAX: 2},
                        {ID: 'N3', MIN: 0, MAX: 2},
                        {ID: 'N4', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
