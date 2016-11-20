from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QG',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 99999},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'G93', MIN: 0, MAX: 50},
    {ID: 'G62', MIN: 1, MAX: 1},
    {ID: 'LDT', MIN: 0, MAX: 99999},
    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 100},
    ]},
    {ID: 'G53', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'G62', MIN: 0, MAX: 3},
        {ID: 'NTE', MIN: 0, MAX: 20},
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'G39', MIN: 0, MAX: 1},
            {ID: 'G69', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'LIN', MIN: 0, MAX: 1},
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'PKG', MIN: 0, MAX: 25},
            {ID: 'G23', MIN: 0, MAX: 10},
            {ID: 'G62', MIN: 0, MAX: 2},
            {ID: 'G36', MIN: 0, MAX: 1},
            {ID: 'G26', MIN: 0, MAX: 2},
            {ID: 'G43', MIN: 0, MAX: 9999},
            {ID: 'G24', MIN: 0, MAX: 999},
            {ID: 'G40', MIN: 0, MAX: 99},
            {ID: 'G93', MIN: 0, MAX: 50},
            {ID: 'G22', MIN: 0, MAX: 5},
            {ID: 'G46', MIN: 0, MAX: 99},
            {ID: 'H1', MIN: 0, MAX: 5},
            {ID: 'G54', MIN: 0, MAX: 99},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'UIT', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'TD1', MIN: 0, MAX: 1},
            {ID: 'LDT', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'PAL', MIN: 0, MAX: 99999},
                {ID: 'G93', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 1},
            ]},
            {ID: 'G55', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'G69', MIN: 0, MAX: 5},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'LIN', MIN: 0, MAX: 1},
                {ID: 'PID', MIN: 0, MAX: 200},
                {ID: 'H1', MIN: 0, MAX: 5},
                {ID: 'REF', MIN: 0, MAX: 10},
                {ID: 'PKG', MIN: 0, MAX: 25},
                {ID: 'MEA', MIN: 0, MAX: 10},
                {ID: 'TD1', MIN: 0, MAX: 1},
                {ID: 'SLN', MIN: 0, MAX: 100},
                {ID: 'LDT', MIN: 0, MAX: 1},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 100},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
