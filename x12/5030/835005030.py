from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BPR', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 99999},
    {ID: 'TRN', MIN: 0, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 99999},
        {ID: 'N3', MIN: 0, MAX: 99999},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'RDM', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'TS3', MIN: 0, MAX: 1},
        {ID: 'TS2', MIN: 0, MAX: 1},
        {ID: 'CLP', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'CAS', MIN: 0, MAX: 99},
            {ID: 'NM1', MIN: 1, MAX: 9},
            {ID: 'MIA', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'AMT', MIN: 0, MAX: 20},
            {ID: 'QTY', MIN: 0, MAX: 20},
            {ID: 'SVC', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'CAS', MIN: 0, MAX: 99},
                {ID: 'REF', MIN: 0, MAX: 99},
                {ID: 'AMT', MIN: 0, MAX: 20},
                {ID: 'QTY', MIN: 0, MAX: 20},
                {ID: 'LQ', MIN: 0, MAX: 99},
            ]},
        ]},
    ]},
    {ID: 'PLB', MIN: 0, MAX: 99999},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
