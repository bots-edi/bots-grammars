from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'SPI', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'CUR', MIN: 0, MAX: 99999},
    {ID: 'MTX', MIN: 0, MAX: 99999},
    {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'G61', MIN: 0, MAX: 5},
    ]},
    {ID: 'PPL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'PD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PDD', MIN: 0, MAX: 99999},
        ]},
        {ID: 'PL', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'PCT', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 99999},
            {ID: 'PD', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SPI', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'PDD', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'QTY', MIN: 1, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 2},
                {ID: 'NTE', MIN: 0, MAX: 5},
                {ID: 'REF', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
