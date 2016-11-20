from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'IN1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'IN2', MIN: 1, MAX: 10},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'API', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 5},
                {ID: 'PER', MIN: 0, MAX: 1},
                {ID: 'AIN', MIN: 0, MAX: 5},
                {ID: 'DTP', MIN: 0, MAX: 1},
                {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'PER', MIN: 0, MAX: 1},
                    {ID: 'EMS', MIN: 0, MAX: 1},
                    {ID: 'NTE', MIN: 0, MAX: 10},
                    {ID: 'DTP', MIN: 0, MAX: 4},
                    {ID: 'REF', MIN: 0, MAX: 5},
                    {ID: 'AIN', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'DTP', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'NX2', MIN: 0, MAX: 10},
                        {ID: 'ACT', MIN: 0, MAX: 1},
                        {ID: 'NM1', MIN: 0, MAX: 10},
                        {ID: 'PRD', MIN: 0, MAX: 1},
                        {ID: 'PEX', MIN: 0, MAX: 10},
                        {ID: 'AMT', MIN: 0, MAX: 5},
                        {ID: 'QTY', MIN: 0, MAX: 5},
                        {ID: 'YNQ', MIN: 0, MAX: 5},
                        {ID: 'DTP', MIN: 0, MAX: 10},
                        {ID: 'MSG', MIN: 0, MAX: 20},
                    ]},
                    {ID: 'FAA', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'NM1', MIN: 0, MAX: 5},
                        {ID: 'QTY', MIN: 0, MAX: 1},
                        {ID: 'MSG', MIN: 0, MAX: 20},
                        {ID: 'DTP', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'AMT', MIN: 0, MAX: 1},
                        ]},
                    ]},
                    {ID: 'CDA', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'NM1', MIN: 0, MAX: 5},
                        {ID: 'QTY', MIN: 0, MAX: 1},
                        {ID: 'DTP', MIN: 0, MAX: 20},
                        {ID: 'MSG', MIN: 0, MAX: 20},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
