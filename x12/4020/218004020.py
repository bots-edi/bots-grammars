from bots.botsconfig import *
from records004020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FH',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'TF', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 5},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 5},
        {ID: 'N9', MIN: 0, MAX: 10},
    ]},
    {ID: 'TS', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'G62', MIN: 0, MAX: 5},
        {ID: 'CL', MIN: 0, MAX: 1},
        {ID: 'WGP', MIN: 0, MAX: 1},
        {ID: 'TFR', MIN: 0, MAX: 10},
        {ID: 'TFM', MIN: 0, MAX: 10},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'SCL', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'TFM', MIN: 0, MAX: 10},
            {ID: 'RTS', MIN: 0, MAX: 1},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'SCL', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'TFM', MIN: 0, MAX: 10},
            {ID: 'CL', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'RTS', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'GY', MIN: 0, MAX: 99},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'GY', MIN: 0, MAX: 99},
                {ID: 'SCL', MIN: 0, MAX: 1},
                {ID: 'TFR', MIN: 0, MAX: 10},
                {ID: 'TFM', MIN: 0, MAX: 10},
                {ID: 'RTS', MIN: 0, MAX: 1},
                {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'SCL', MIN: 1, MAX: 9999, LEVEL: [
                    {ID: 'RTS', MIN: 0, MAX: 1},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
        ]},
        ]},
    ]},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'GY', MIN: 0, MAX: 99},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'GY', MIN: 0, MAX: 99},
                {ID: 'SCL', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'TFR', MIN: 0, MAX: 10},
                    {ID: 'TFM', MIN: 0, MAX: 10},
                    {ID: 'CL', MIN: 0, MAX: 999, LEVEL: [
                        {ID: 'RTS', MIN: 0, MAX: 1},
                    ]},
                ]},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
    ]},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'GY', MIN: 0, MAX: 99},
            {ID: 'SCL', MIN: 0, MAX: 1},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'GY', MIN: 0, MAX: 99},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'GY', MIN: 0, MAX: 99},
                {ID: 'TFA', MIN: 0, MAX: 1},
                {ID: 'TFD', MIN: 0, MAX: 10},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
    ]},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'SCL', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'CL', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'TFA', MIN: 0, MAX: 1},
                {ID: 'TFD', MIN: 0, MAX: 10},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
    ]},
    ]},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'MCT', MIN: 0, MAX: 99},
            {ID: 'GY', MIN: 0, MAX: 99},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
