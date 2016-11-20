from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'LN',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 10},
    {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'MSG', MIN: 0, MAX: 99999},
    ]},
    {ID: 'NM1', MIN: 0, MAX: 15, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 15},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'LID', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 10},
        {ID: 'BCI', MIN: 0, MAX: 1},
        {ID: 'SI', MIN: 0, MAX: 2},
        {ID: 'LIE', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
        {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 5},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
        ]},
        {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'NM1', MIN: 1, MAX: 10, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 15},
                {ID: 'PER', MIN: 0, MAX: 5},
                {ID: 'LIE', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'N3', MIN: 0, MAX: 1},
                    {ID: 'N4', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
        {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'VEH', MIN: 0, MAX: 1},
            {ID: 'VAT', MIN: 0, MAX: 100},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'DVI', MIN: 0, MAX: 1},
            {ID: 'VRC', MIN: 0, MAX: 1},
            {ID: 'DAM', MIN: 0, MAX: 99999},
            {ID: 'LIE', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
            {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NM1', MIN: 1, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 10},
                {ID: 'PER', MIN: 0, MAX: 10},
                {ID: 'ICH', MIN: 0, MAX: 1},
                {ID: 'CRC', MIN: 0, MAX: 99999},
                {ID: 'BCI', MIN: 0, MAX: 1},
                {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 5},
                    {ID: 'AMT', MIN: 0, MAX: 5},
                    {ID: 'PCT', MIN: 0, MAX: 5},
                    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                        {ID: 'LQ', MIN: 1, MAX: 99999, LEVEL: [
                            {ID: 'AMT', MIN: 0, MAX: 5},
                            {ID: 'PCT', MIN: 0, MAX: 5},
                        ]},
                        {ID: 'LE', MIN: 1, MAX: 1},
                    ]},
                ]},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
                        {ID: 'N2', MIN: 0, MAX: 2},
                        {ID: 'N3', MIN: 0, MAX: 2},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'N9', MIN: 0, MAX: 10},
                        {ID: 'PER', MIN: 0, MAX: 10},
                        {ID: 'ICH', MIN: 0, MAX: 1},
                        {ID: 'CRC', MIN: 0, MAX: 99999},
                        {ID: 'BCI', MIN: 0, MAX: 1},
                        {ID: 'III', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'DTP', MIN: 0, MAX: 5},
                            {ID: 'AMT', MIN: 0, MAX: 5},
                            {ID: 'PCT', MIN: 0, MAX: 5},
                            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                            {ID: 'LQ', MIN: 1, MAX: 99999, LEVEL: [
                                {ID: 'AMT', MIN: 0, MAX: 5},
                                {ID: 'PCT', MIN: 0, MAX: 5},
                            ]},
                            {ID: 'LE', MIN: 1, MAX: 1},
                        ]},
                    ]},
                ]},
                ]},
            ]},
            {ID: 'PIN', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'BCI', MIN: 1, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 1},
                    {ID: 'N9', MIN: 0, MAX: 5},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'NM1', MIN: 0, MAX: 1},
                    {ID: 'PER', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
