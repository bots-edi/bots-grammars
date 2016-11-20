from bots.botsconfig import *
from records005011 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PH',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'PCT', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
        ]},
        {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'QTY', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'NTE', MIN: 0, MAX: 99999},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
                {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'PER', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                    {ID: 'CS', MIN: 0, MAX: 99999},
                    {ID: 'FOB', MIN: 0, MAX: 99999},
                    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'LQ', MIN: 1, MAX: 99999},
                    ]},
                ]},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
