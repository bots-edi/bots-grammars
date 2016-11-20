from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ID',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'UD', MIN: 0, MAX: 1},
    {ID: 'NM1', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'ACT', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'UD', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 19},
        {ID: 'BLI', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 9},
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'K3', MIN: 0, MAX: 3},
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'BLI', MIN: 0, MAX: 1},
            {ID: 'INV', MIN: 0, MAX: 9},
            {ID: 'UD', MIN: 0, MAX: 1},
            {ID: 'M1', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 9},
            {ID: 'RPA', MIN: 0, MAX: 1},
            {ID: 'K3', MIN: 0, MAX: 3},
            {ID: 'BEN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 1},
            ]},
            {ID: 'ENT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 3},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'DMA', MIN: 0, MAX: 1},
                {ID: 'REL', MIN: 0, MAX: 1},
                {ID: 'UD', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'K3', MIN: 0, MAX: 3},
                {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'V9', MIN: 0, MAX: 1},
                    {ID: 'SPA', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 9},
                    {ID: 'K3', MIN: 0, MAX: 3},
                    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'N3', MIN: 0, MAX: 3},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'G61', MIN: 0, MAX: 9},
                    ]},
                ]},
                {ID: 'BEN', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'NM1', MIN: 0, MAX: 1},
                    {ID: 'N2', MIN: 0, MAX: 1},
                    {ID: 'N3', MIN: 0, MAX: 1},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'DTP', MIN: 0, MAX: 1},
                ]},
                {ID: 'BLI', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'INV', MIN: 0, MAX: 9},
                    {ID: 'UD', MIN: 0, MAX: 1},
                    {ID: 'UDA', MIN: 0, MAX: 99999},
                    {ID: 'M1', MIN: 0, MAX: 1},
                    {ID: 'DTP', MIN: 0, MAX: 9},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'RPA', MIN: 0, MAX: 99999},
                    {ID: 'K3', MIN: 0, MAX: 3},
                    {ID: 'BEN', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'NM1', MIN: 0, MAX: 1},
                        {ID: 'N2', MIN: 0, MAX: 1},
                        {ID: 'N3', MIN: 0, MAX: 1},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'DTP', MIN: 0, MAX: 1},
                    ]},
                ]},
            ]},
        ]},
        {ID: 'MSG', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 1},
            {ID: 'NM1', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
