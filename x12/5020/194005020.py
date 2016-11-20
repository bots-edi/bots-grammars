from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'GT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'LDT', MIN: 0, MAX: 99999},
    {ID: 'PWK', MIN: 0, MAX: 99999},
    {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
    ]},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'AMT', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'PAM', MIN: 0, MAX: 99999},
        {ID: 'HSD', MIN: 0, MAX: 99999},
        {ID: 'NX1', MIN: 0, MAX: 99999},
        {ID: 'YNQ', MIN: 0, MAX: 99999},
        {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'L11', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'INX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'K3', MIN: 1, MAX: 99999},
            ]},
        ]},
        {ID: 'PO1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'MTX', MIN: 0, MAX: 99999},
        ]},
        {ID: 'PPL', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PD', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PDD', MIN: 0, MAX: 99999},
            ]},
            {ID: 'PL', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 1},
                {ID: 'PCT', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'NTE', MIN: 0, MAX: 99999},
                {ID: 'PD', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'SPI', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'PDD', MIN: 0, MAX: 99999},
                    {ID: 'MTX', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 10},
                ]},
            ]},
        ]},
        {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'DMG', MIN: 0, MAX: 99999},
            {ID: 'EMS', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'L11', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
            {ID: 'DEG', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'FOS', MIN: 0, MAX: 99999},
                {ID: 'N1', MIN: 0, MAX: 99999},
            ]},
            {ID: 'K2', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'NM1', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
