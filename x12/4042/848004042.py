from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BMS', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 99999},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 99999},
        {ID: 'N3', MIN: 0, MAX: 99999},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'MSS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'SD1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 99999},
                {ID: 'PKG', MIN: 0, MAX: 99999},
                {ID: 'TD4', MIN: 0, MAX: 99999},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'CID', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'MEA', MIN: 1, MAX: 99999},
                ]},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'CID', MIN: 0, MAX: 1},
                {ID: 'MEA', MIN: 0, MAX: 99999},
                {ID: 'STA', MIN: 0, MAX: 1},
                {ID: 'TMD', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'SD1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'MEA', MIN: 0, MAX: 99999},
                    {ID: 'PKG', MIN: 0, MAX: 99999},
                    {ID: 'TD4', MIN: 0, MAX: 99999},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                    {ID: 'CID', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'MEA', MIN: 1, MAX: 99999},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
