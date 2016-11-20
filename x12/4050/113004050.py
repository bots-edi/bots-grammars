from bots.botsconfig import *
from records004050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'LQ', MIN: 0, MAX: 99999},
    {ID: 'MTX', MIN: 0, MAX: 99999},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'N9', MIN: 0, MAX: 99999},
    ]},
    {ID: 'AWD', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'NX2', MIN: 0, MAX: 99999},
            {ID: 'LQ', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'NX2', MIN: 0, MAX: 99999},
            {ID: 'EMS', MIN: 0, MAX: 99999},
            {ID: 'TPB', MIN: 0, MAX: 99999},
            {ID: 'PWK', MIN: 0, MAX: 99999},
            {ID: 'PAM', MIN: 0, MAX: 99999},
            {ID: 'G86', MIN: 0, MAX: 1},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
            {ID: 'AWD', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'PDL', MIN: 0, MAX: 99999},
                {ID: 'LQ', MIN: 0, MAX: 99999},
                {ID: 'N1', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
