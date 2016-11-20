from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'WA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 3, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 100},
        ]},
        {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 99999},
            ]},
            {ID: 'PSC', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SSS', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'CUR', MIN: 0, MAX: 1},
                {ID: 'ITA', MIN: 0, MAX: 1},
                {ID: 'TXI', MIN: 0, MAX: 1},
                {ID: 'ITD', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 99999},
            ]},
            {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PID', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 3},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'PER', MIN: 0, MAX: 99999},
                ]},
                {ID: 'PSC', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'SSS', MIN: 0, MAX: 99999},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'CUR', MIN: 0, MAX: 1},
                    {ID: 'ITA', MIN: 0, MAX: 1},
                    {ID: 'TXI', MIN: 0, MAX: 1},
                    {ID: 'ITD', MIN: 0, MAX: 1},
                    {ID: 'N9', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
