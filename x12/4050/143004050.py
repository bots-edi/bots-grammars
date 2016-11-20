from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'WA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 2},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'CID', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'PWK', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 3},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 2},
            {ID: 'QTY', MIN: 0, MAX: 1},
        ]},
        {ID: 'PRR', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'MSG', MIN: 0, MAX: 99999},
            {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 99999},
            ]},
            {ID: 'REP', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'PRT', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 2},
            ]},
            {ID: 'ITA', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 2},
            ]},
            {ID: 'PRR', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'REP', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                ]},
                {ID: 'PRT', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'N1', MIN: 0, MAX: 1},
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 3},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'PER', MIN: 0, MAX: 2},
                ]},
                {ID: 'ITA', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'CUR', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
