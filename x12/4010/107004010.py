from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'MC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'AT5', MIN: 0, MAX: 99},
    {ID: 'PR', MIN: 0, MAX: 99},
    {ID: 'ID4', MIN: 0, MAX: 1},
    {ID: 'IV1', MIN: 0, MAX: 1},
    {ID: 'MI1', MIN: 0, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'MCT', MIN: 0, MAX: 999},
    {ID: 'MS2', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'AT9', MIN: 0, MAX: 1},
    ]},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'GY', MIN: 1, MAX: 999},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'PR', MIN: 0, MAX: 99},
        {ID: 'ID4', MIN: 0, MAX: 1},
        {ID: 'AT5', MIN: 0, MAX: 99},
        {ID: 'MS2', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'AT9', MIN: 0, MAX: 1},
        ]},
        {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'G62', MIN: 0, MAX: 10},
        ]},
        {ID: 'CA1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'GY', MIN: 1, MAX: 999},
            {ID: 'PR', MIN: 0, MAX: 99},
            {ID: 'ID4', MIN: 0, MAX: 1},
            {ID: 'IV1', MIN: 0, MAX: 1},
            {ID: 'SV', MIN: 0, MAX: 1},
            {ID: 'AT5', MIN: 0, MAX: 99},
            {ID: 'MCT', MIN: 0, MAX: 999},
            {ID: 'MS2', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'AT9', MIN: 0, MAX: 1},
            ]},
            {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'G62', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
