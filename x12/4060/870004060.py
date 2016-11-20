from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSR', MIN: 1, MAX: 1},
    {ID: 'TD3', MIN: 0, MAX: 1},
    {ID: 'TD4', MIN: 0, MAX: 1},
    {ID: 'TD5', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'PWK', MIN: 0, MAX: 1},
    ]},
    {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'HL', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'PRF', MIN: 0, MAX: 1},
        {ID: 'ISR', MIN: 0, MAX: 104, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 6},
            {ID: 'QTY', MIN: 0, MAX: 4},
        ]},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'CS', MIN: 0, MAX: 3},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
        {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'PO1', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'SLN', MIN: 0, MAX: 100},
            {ID: 'PO3', MIN: 0, MAX: 1},
            {ID: 'PID', MIN: 0, MAX: 1000},
            {ID: 'MEA', MIN: 0, MAX: 40},
            {ID: 'PKG', MIN: 0, MAX: 25},
            {ID: 'ISR', MIN: 0, MAX: 104, LEVEL: [
                {ID: 'PID', MIN: 0, MAX: 6},
                {ID: 'QTY', MIN: 0, MAX: 4},
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'TD1', MIN: 0, MAX: 1},
                {ID: 'TD5', MIN: 0, MAX: 1},
                {ID: 'TD3', MIN: 0, MAX: 1},
                {ID: 'TD4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 12},
                {ID: 'SAC', MIN: 0, MAX: 25},
                {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
                ]},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'LM', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
