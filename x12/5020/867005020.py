from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'PT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BPT', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'MEA', MIN: 0, MAX: 20},
    {ID: 'PSA', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
        {ID: 'LCD', MIN: 0, MAX: 2},
    ]},
    {ID: 'PTD', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 20},
        {ID: 'PRF', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'MAN', MIN: 0, MAX: 1},
        {ID: 'LCD', MIN: 0, MAX: 2},
        {ID: 'LQ', MIN: 0, MAX: 99999},
        {ID: 'MEA', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 20},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'SII', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LIN', MIN: 0, MAX: 1},
            {ID: 'PO3', MIN: 0, MAX: 25},
            {ID: 'PO4', MIN: 0, MAX: 1},
            {ID: 'UIT', MIN: 0, MAX: 12},
            {ID: 'AMT', MIN: 0, MAX: 12},
            {ID: 'ITA', MIN: 0, MAX: 10},
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'MEA', MIN: 0, MAX: 40},
            {ID: 'PWK', MIN: 0, MAX: 25},
            {ID: 'PKG', MIN: 0, MAX: 25},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'DD', MIN: 0, MAX: 99999},
            {ID: 'LDT', MIN: 0, MAX: 1},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 0, MAX: 100},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 100},
                ]},
            ]},
            {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'FA2', MIN: 1, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'AMT', MIN: 0, MAX: 12},
        {ID: 'ITA', MIN: 0, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
