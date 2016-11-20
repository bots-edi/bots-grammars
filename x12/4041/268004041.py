from bots.botsconfig import *
from records004041 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 9},
    {ID: 'NM1', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 3},
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SPA', MIN: 0, MAX: 3},
            {ID: 'LIN', MIN: 0, MAX: 9},
            {ID: 'III', MIN: 0, MAX: 9},
        ]},
        {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SPA', MIN: 0, MAX: 3},
            {ID: 'AMT', MIN: 0, MAX: 3},
            {ID: 'III', MIN: 0, MAX: 9},
        ]},
        {ID: 'ACT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'SPA', MIN: 0, MAX: 3},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'LIN', MIN: 0, MAX: 9},
            {ID: 'PAM', MIN: 0, MAX: 9},
            {ID: 'III', MIN: 0, MAX: 9},
        ]},
        {ID: 'CON', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'LIN', MIN: 0, MAX: 9},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'SPA', MIN: 0, MAX: 3},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'PAM', MIN: 0, MAX: 9},
            {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 3},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'BEN', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'ASI', MIN: 0, MAX: 1},
            ]},
            {ID: 'BLI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LIN', MIN: 0, MAX: 3},
                {ID: 'SPA', MIN: 0, MAX: 3},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'AM1', MIN: 0, MAX: 9},
            ]},
            {ID: 'IT1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'AM1', MIN: 0, MAX: 99},
                {ID: 'SPA', MIN: 0, MAX: 3},
                {ID: 'MSG', MIN: 0, MAX: 9},
                {ID: 'ACT', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LIN', MIN: 0, MAX: 9},
                    {ID: 'SPA', MIN: 0, MAX: 3},
                    {ID: 'AM1', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 9},
                    {ID: 'MSG', MIN: 0, MAX: 9},
                ]},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 3},
                    {ID: 'N3', MIN: 0, MAX: 3},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'SPA', MIN: 0, MAX: 3},
                    {ID: 'PDL', MIN: 0, MAX: 1},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                    {ID: 'G86', MIN: 0, MAX: 1},
                    {ID: 'EFI', MIN: 1, MAX: 99999, LEVEL: [
                        {ID: 'BIN', MIN: 0, MAX: 1},
                    ]},
                ]},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AM1', MIN: 1, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'RPA', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 3},
                    {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'REF', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
