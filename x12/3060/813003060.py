from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTI', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'TIA', MIN: 0, MAX: 1000},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'TRN', MIN: 0, MAX: 1000},
    {ID: 'BPR', MIN: 0, MAX: 1000},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'IN2', MIN: 0, MAX: 10},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'TFS', MIN: 0, MAX: 100000, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 10},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'MSG', MIN: 0, MAX: 1000},
        {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'IN2', MIN: 0, MAX: 10},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'FGS', MIN: 0, MAX: 100000, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'IN2', MIN: 0, MAX: 10},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
            {ID: 'TIA', MIN: 0, MAX: 10000, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'MSG', MIN: 0, MAX: 1000},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
