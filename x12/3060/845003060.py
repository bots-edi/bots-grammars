from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BPA', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 10000, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 10},
    ]},
    {ID: 'CON', MIN: 1, MAX: 10000, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'CTB', MIN: 0, MAX: 10},
        {ID: 'ITD', MIN: 0, MAX: 2},
        {ID: 'N1', MIN: 0, MAX: 10000, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'CTB', MIN: 0, MAX: 25},
        ]},
        {ID: 'PAD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CTB', MIN: 0, MAX: 10},
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'MEA', MIN: 0, MAX: 40},
            {ID: 'UIT', MIN: 0, MAX: 20},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 5},
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'SSS', MIN: 0, MAX: 1},
            {ID: 'SHP', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'LIN', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'SLN', MIN: 0, MAX: 100},
            ]},
            {ID: 'N1', MIN: 0, MAX: 10000, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'CTB', MIN: 0, MAX: 25},
            ]},
            {ID: 'CTP', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'CTB', MIN: 0, MAX: 25},
                {ID: 'N1', MIN: 0, MAX: 10000, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 10},
                    {ID: 'CTB', MIN: 0, MAX: 25},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
