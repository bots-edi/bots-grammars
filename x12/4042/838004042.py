from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'TD',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTP', MIN: 1, MAX: 1},
    {ID: 'REQ', MIN: 0, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 1},
    {ID: 'SPI', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PLA', MIN: 0, MAX: 1},
        {ID: 'LCD', MIN: 0, MAX: 99999},
        {ID: 'LIN', MIN: 0, MAX: 99999},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'CUR', MIN: 0, MAX: 99999},
            {ID: 'TAX', MIN: 0, MAX: 99999},
            {ID: 'FOB', MIN: 0, MAX: 99999},
            {ID: 'ITD', MIN: 0, MAX: 99999},
            {ID: 'TD5', MIN: 0, MAX: 99999},
            {ID: 'SPI', MIN: 0, MAX: 99999},
            {ID: 'FBB', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'LCD', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DMG', MIN: 0, MAX: 99999},
                {ID: 'MEA', MIN: 0, MAX: 99999},
            ]},
            {ID: 'TPD', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'PID', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'TUD', MIN: 1, MAX: 99999, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 99999},
                        {ID: 'N1', MIN: 0, MAX: 1},
                        {ID: 'N2', MIN: 0, MAX: 2},
                        {ID: 'N3', MIN: 0, MAX: 2},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'PER', MIN: 0, MAX: 99999},
                    ]},
                    {ID: 'LE', MIN: 1, MAX: 1},
                ]},
                {ID: 'SPR', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N9', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'PAM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'TAX', MIN: 0, MAX: 99999},
                {ID: 'CUR', MIN: 0, MAX: 99999},
            ]},
            {ID: 'TXN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999},
            ]},
        ]},
        {ID: 'ENE', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'TPD', MIN: 0, MAX: 99999},
                {ID: 'PID', MIN: 0, MAX: 99999},
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 99999},
            ]},
            {ID: 'TXN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'ERI', MIN: 0, MAX: 99999},
    {ID: 'AMT', MIN: 0, MAX: 99999},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
