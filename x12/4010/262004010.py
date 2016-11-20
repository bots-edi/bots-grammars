from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'TRN', MIN: 0, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'AM1', MIN: 0, MAX: 99999},
        {ID: 'PWK', MIN: 0, MAX: 5},
        {ID: 'SPI', MIN: 0, MAX: 99999},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'NX1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'NX2', MIN: 1, MAX: 99999},
            {ID: 'PDS', MIN: 0, MAX: 99999},
            {ID: 'PDE', MIN: 0, MAX: 99999},
            {ID: 'REA', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 25},
            {ID: 'REF', MIN: 0, MAX: 30},
            {ID: 'DTP', MIN: 0, MAX: 6},
            {ID: 'YNQ', MIN: 0, MAX: 43},
            {ID: 'CRC', MIN: 0, MAX: 10},
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'PCT', MIN: 0, MAX: 8},
            {ID: 'REC', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'API', MIN: 0, MAX: 1},
                {ID: 'NTE', MIN: 0, MAX: 4},
            ]},
            {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 10},
            ]},
            {ID: 'PEX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 1},
                {ID: 'III', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 10},
                {ID: 'MEA', MIN: 0, MAX: 10},
                {ID: 'AMT', MIN: 0, MAX: 7},
                {ID: 'MSG', MIN: 0, MAX: 3},
                {ID: 'DTP', MIN: 0, MAX: 2},
                {ID: 'AIN', MIN: 0, MAX: 4},
                {ID: 'III', MIN: 0, MAX: 99999},
            ]},
            {ID: 'RET', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'PTF', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'III', MIN: 0, MAX: 99999},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 1},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'PER', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                ]},
                {ID: 'LN2', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
        {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'IN2', MIN: 1, MAX: 10},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 2},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'REF', MIN: 1, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 2},
                {ID: 'III', MIN: 0, MAX: 50, LEVEL: [
                    {ID: 'MSG', MIN: 0, MAX: 10},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
