from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'PWK', MIN: 0, MAX: 99999},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'LUI', MIN: 0, MAX: 1},
    {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PDL', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'CUR', MIN: 0, MAX: 1},
    ]},
    {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 99999},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NX1', MIN: 0, MAX: 2},
            {ID: 'N2', MIN: 0, MAX: 99999},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'PCT', MIN: 0, MAX: 99999},
            {ID: 'LUI', MIN: 0, MAX: 99999},
            {ID: 'TPB', MIN: 0, MAX: 99999},
            {ID: 'PWK', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'NX2', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MTX', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'NX2', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'LIN', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'NX2', MIN: 0, MAX: 99999},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'PCT', MIN: 0, MAX: 99999},
                    {ID: 'PDL', MIN: 0, MAX: 99999},
                    {ID: 'PWK', MIN: 0, MAX: 99999},
                    {ID: 'CUR', MIN: 0, MAX: 1},
                    {ID: 'CDS', MIN: 0, MAX: 1},
                    {ID: 'MTX', MIN: 0, MAX: 99999},
                    {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'AMT', MIN: 0, MAX: 1},
                        {ID: 'DTM', MIN: 0, MAX: 99999},
                        {ID: 'CUR', MIN: 0, MAX: 1},
                    ]},
                ]},
            ]},
        ]},
        {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'BIN', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
