from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'DTP', MIN: 0, MAX: 99999},
    {ID: 'AMT', MIN: 0, MAX: 99999},
    {ID: 'QTY', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'ACT', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 5},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'INS', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 1, MAX: 99999},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'PM', MIN: 0, MAX: 1},
            {ID: 'EC', MIN: 0, MAX: 99999},
            {ID: 'ICM', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'HLH', MIN: 0, MAX: 1},
            {ID: 'HI', MIN: 0, MAX: 10},
            {ID: 'LUI', MIN: 0, MAX: 99999},
        ]},
        {ID: 'DSB', MIN: 0, MAX: 4, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 10},
            {ID: 'AD1', MIN: 0, MAX: 10},
        ]},
        {ID: 'HD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 10},
            {ID: 'AMT', MIN: 0, MAX: 3},
            {ID: 'REF', MIN: 0, MAX: 5},
            {ID: 'IDC', MIN: 0, MAX: 99999},
            {ID: 'LX', MIN: 0, MAX: 30, LEVEL: [
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'N1', MIN: 0, MAX: 3},
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 2},
                {ID: 'PER', MIN: 0, MAX: 2},
                {ID: 'PRV', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 6},
                {ID: 'PLA', MIN: 0, MAX: 1},
            ]},
            {ID: 'COB', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 2},
                {ID: 'NM1', MIN: 0, MAX: 3, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 1},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'PER', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
        {ID: 'LC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 5},
            {ID: 'DTP', MIN: 0, MAX: 2},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'BEN', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DMG', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'FSA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'DTP', MIN: 0, MAX: 10},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'RP', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'INV', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 20},
            {ID: 'QTY', MIN: 0, MAX: 20},
            {ID: 'K3', MIN: 0, MAX: 3},
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'BEN', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N3', MIN: 0, MAX: 1},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'FC', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'INV', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'ENT', MIN: 0, MAX: 99999},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'AMT', MIN: 0, MAX: 20},
                    {ID: 'K3', MIN: 0, MAX: 3},
                ]},
            ]},
            {ID: 'AIN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 1, MAX: 1},
                    {ID: 'DTP', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
