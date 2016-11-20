from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'TRN', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
        ]},
    ]},
    {ID: 'HL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'TRN', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'DMG', MIN: 0, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'PWK', MIN: 0, MAX: 99999},
            {ID: 'TRN', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
            ]},
            {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
            ]},
            {ID: 'MTX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
