from bots.botsconfig import *
from records004060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'VD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'SUP', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'MSG', MIN: 0, MAX: 99999},
    ]},
    {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'TXI', MIN: 0, MAX: 99999},
        {ID: 'YNQ', MIN: 0, MAX: 99999},
        {ID: 'AP1', MIN: 0, MAX: 1},
        {ID: 'SUP', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LM', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 1},
            {ID: 'CTP', MIN: 0, MAX: 1},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'SAC', MIN: 0, MAX: 99999},
        ]},
        {ID: 'VEH', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'BCI', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'LID', MIN: 0, MAX: 1},
            {ID: 'LQ', MIN: 0, MAX: 99999},
            {ID: 'DAM', MIN: 0, MAX: 1},
            {ID: 'CRC', MIN: 0, MAX: 1},
            {ID: 'DVI', MIN: 0, MAX: 1},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'III', MIN: 0, MAX: 1},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'VAT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'PER', MIN: 0, MAX: 99999},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'F13', MIN: 0, MAX: 99999},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'TXI', MIN: 0, MAX: 99999},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'N9', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'ID', MIN: 0, MAX: 1},
                {ID: 'DP', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'DL', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'PCT', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
