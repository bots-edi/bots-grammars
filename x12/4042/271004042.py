from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'TRN', MIN: 0, MAX: 9},
        {ID: 'AAA', MIN: 0, MAX: 9},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'AAA', MIN: 0, MAX: 9},
            {ID: 'PRV', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'INS', MIN: 0, MAX: 1},
            {ID: 'HI', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'LUI', MIN: 0, MAX: 9},
            {ID: 'MPI', MIN: 0, MAX: 9},
            {ID: 'EB', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'HSD', MIN: 0, MAX: 9},
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 20},
                {ID: 'AAA', MIN: 0, MAX: 9},
                {ID: 'VEH', MIN: 0, MAX: 1},
                {ID: 'PID', MIN: 0, MAX: 1},
                {ID: 'PDR', MIN: 0, MAX: 1},
                {ID: 'PDP', MIN: 0, MAX: 1},
                {ID: 'LIN', MIN: 0, MAX: 1},
                {ID: 'EM', MIN: 0, MAX: 1},
                {ID: 'SD1', MIN: 0, MAX: 1},
                {ID: 'PKD', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 10},
                {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 5},
                    {ID: 'AMT', MIN: 0, MAX: 5},
                    {ID: 'PCT', MIN: 0, MAX: 5},
                    {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'AMT', MIN: 0, MAX: 5},
                        {ID: 'PCT', MIN: 0, MAX: 5},
                    ]},
                ]},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
                        {ID: 'N2', MIN: 0, MAX: 1},
                        {ID: 'N3', MIN: 0, MAX: 1},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'PER', MIN: 0, MAX: 3},
                        {ID: 'PRV', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
