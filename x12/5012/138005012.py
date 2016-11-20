from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'ERP', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'IN1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'IN2', MIN: 1, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'SSE', MIN: 0, MAX: 1},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'IND', MIN: 0, MAX: 1},
        {ID: 'LUI', MIN: 0, MAX: 5},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'RQS', MIN: 0, MAX: 99999},
        {ID: 'SCA', MIN: 0, MAX: 99999},
        {ID: 'EMS', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'TST', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'SBT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SRE', MIN: 0, MAX: 5},
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'RAP', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'EMS', MIN: 0, MAX: 1},
            ]},
            {ID: 'SCA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'FOS', MIN: 0, MAX: 1},
            ]},
            {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'DEG', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'FOS', MIN: 0, MAX: 5},
    ]},
    {ID: 'SST', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'SSE', MIN: 0, MAX: 1},
        {ID: 'SUM', MIN: 0, MAX: 1},
        {ID: 'FOS', MIN: 0, MAX: 99999},
        {ID: 'RQS', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'PCL', MIN: 0, MAX: 25, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'SSE', MIN: 0, MAX: 1},
        {ID: 'FOS', MIN: 0, MAX: 99999},
        {ID: 'DEG', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'SUM', MIN: 0, MAX: 1},
            {ID: 'FOS', MIN: 0, MAX: 30},
        ]},
    ]},
    {ID: 'ATV', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'EMS', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
