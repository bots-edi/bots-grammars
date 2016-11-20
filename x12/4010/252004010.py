from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 99999},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'ENT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'ASI', MIN: 1, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'YNQ', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'DMA', MIN: 0, MAX: 1},
        {ID: 'AM1', MIN: 0, MAX: 99999},
        {ID: 'MSG', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 3},
            {ID: 'EMS', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'N3', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NM1', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'UC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'III', MIN: 0, MAX: 99999},
            {ID: 'EMS', MIN: 0, MAX: 1},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 9},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'CDS', MIN: 0, MAX: 1},
            {ID: 'CED', MIN: 0, MAX: 99999},
            {ID: 'TST', MIN: 0, MAX: 1},
            {ID: 'SRE', MIN: 0, MAX: 1},
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LIC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SPA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N4', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'YNQ', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 3},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
        {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'BIN', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
