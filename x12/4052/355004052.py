from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'AZ',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'K1', MIN: 0, MAX: 10},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'LX', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'M13', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
            ]},
            {ID: 'M11', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
            ]},
            {ID: 'N9', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
            ]},
            {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
                {ID: 'N3', MIN: 0, MAX: 2, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                ]},
                {ID: 'N4', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                ]},
                {ID: 'PER', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                ]},
            ]},
            {ID: 'M12', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
                {ID: 'P5', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                ]},
                {ID: 'M21', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                ]},
            ]},
            {ID: 'M14', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
            ]},
            {ID: 'M15', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
            ]},
            {ID: 'M20', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
            ]},
            {ID: 'VID', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'K1', MIN: 0, MAX: 10},
                {ID: 'MBL', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                    {ID: 'M13', MIN: 0, MAX: 999, LEVEL: [
                        {ID: 'K1', MIN: 0, MAX: 10},
                    ]},
                ]},
                {ID: 'VC', MIN: 0, MAX: 36, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                ]},
                {ID: 'N10', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'K1', MIN: 0, MAX: 10},
                    {ID: 'H1', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'K1', MIN: 0, MAX: 10},
                        {ID: 'H2', MIN: 0, MAX: 99, LEVEL: [
                            {ID: 'K1', MIN: 0, MAX: 10},
                        ]},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'K3', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
