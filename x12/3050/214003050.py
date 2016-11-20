from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B10', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 300},
    {ID: 'MAN', MIN: 0, MAX: 300},
    {ID: 'K1', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
    ]},
    {ID: 'R3', MIN: 0, MAX: 12},
    {ID: 'LX', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'Q5', MIN: 0, MAX: 10},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'MAN', MIN: 0, MAX: 300},
        {ID: 'Q7', MIN: 0, MAX: 10},
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'H3', MIN: 0, MAX: 10},
        {ID: 'G86', MIN: 0, MAX: 1},
        {ID: 'Q6', MIN: 0, MAX: 1},
        {ID: 'CD3', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 20},
            {ID: 'Q5', MIN: 0, MAX: 10},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'Q7', MIN: 0, MAX: 10},
            {ID: 'Q6', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'PRF', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 10},
            ]},
            {ID: 'CD3', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 20},
                {ID: 'Q5', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'SPO', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'REF', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'Q5', MIN: 0, MAX: 1},
        {ID: 'M7', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 5},
        {ID: 'N7', MIN: 0, MAX: 1},
        {ID: 'LX', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'BLR', MIN: 0, MAX: 1},
            {ID: 'MAN', MIN: 0, MAX: 300},
            {ID: 'G62', MIN: 0, MAX: 5},
            {ID: 'TSD', MIN: 0, MAX: 1},
            {ID: 'SPO', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'SDQ', MIN: 0, MAX: 9999},
            ]},
            {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
