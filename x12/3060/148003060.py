from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'IJ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'QTY', MIN: 0, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'ACT', MIN: 0, MAX: 9},
        {ID: 'DTP', MIN: 0, MAX: 9},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
    ]},
    {ID: 'HL', MIN: 1, MAX: 999999, LEVEL: [
        {ID: 'ACT', MIN: 0, MAX: 2},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'FC', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'CRI', MIN: 0, MAX: 99999},
        {ID: 'EMT', MIN: 0, MAX: 1},
        {ID: 'CRC', MIN: 0, MAX: 99999},
        {ID: 'VEH', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'ACT', MIN: 0, MAX: 9},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'ESI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'CRC', MIN: 0, MAX: 9},
            {ID: 'AIN', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
                {ID: 'TXI', MIN: 0, MAX: 9},
                {ID: 'WS', MIN: 0, MAX: 99},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'LN', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 2},
            {ID: 'AMT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'IMP', MIN: 0, MAX: 6},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'CRC', MIN: 0, MAX: 9},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999},
            ]},
            {ID: 'NM1', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 2},
                {ID: 'ACT', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'AD1', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'REL', MIN: 0, MAX: 30},
            {ID: 'NM1', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 2},
                {ID: 'ACT', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 99},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
