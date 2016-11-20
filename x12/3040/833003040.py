from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ME',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'CRO', MIN: 1, MAX: 200, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'K2', MIN: 0, MAX: 10},
        {ID: 'LN1', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'PWK', MIN: 0, MAX: 1},
        ]},
        {ID: 'NX1', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'NX2', MIN: 0, MAX: 30},
        ]},
        {ID: 'LX', MIN: 1, MAX: 2, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'AIN', MIN: 0, MAX: 10},
            {ID: 'PPY', MIN: 0, MAX: 10},
            {ID: 'CAI', MIN: 0, MAX: 10},
            {ID: 'CIV', MIN: 0, MAX: 20},
            {ID: 'REA', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'FPT', MIN: 0, MAX: 1},
                {ID: 'AIN', MIN: 0, MAX: 5},
                {ID: 'NX1', MIN: 0, MAX: 1},
                {ID: 'NX2', MIN: 0, MAX: 30},
            ]},
            {ID: 'IN1', MIN: 1, MAX: 30, LEVEL: [
                {ID: 'IN2', MIN: 0, MAX: 10},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'N10', MIN: 0, MAX: 1},
            ]},
            {ID: 'NX1', MIN: 1, MAX: 10, LEVEL: [
                {ID: 'NX2', MIN: 1, MAX: 30},
                {ID: 'DTP', MIN: 1, MAX: 1},
                {ID: 'ARS', MIN: 0, MAX: 1},
            ]},
            {ID: 'N1', MIN: 0, MAX: 500, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 12},
                {ID: 'PER', MIN: 0, MAX: 3},
                {ID: 'EMP', MIN: 0, MAX: 20, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 1},
                    {ID: 'EMS', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'DTP', MIN: 0, MAX: 1},
                        {ID: 'AIN', MIN: 0, MAX: 10},
                    ]},
                ]},
                {ID: 'FAA', MIN: 0, MAX: 100, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 1},
                    {ID: 'AIN', MIN: 0, MAX: 4},
                    {ID: 'IN1', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'IN2', MIN: 0, MAX: 10},
                        {ID: 'FPT', MIN: 0, MAX: 1},
                    ]},
                ]},
                {ID: 'CDA', MIN: 0, MAX: 100, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 1},
                    {ID: 'PEX', MIN: 0, MAX: 5},
                    {ID: 'IN1', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'IN2', MIN: 0, MAX: 10},
                        {ID: 'FPT', MIN: 0, MAX: 1},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
