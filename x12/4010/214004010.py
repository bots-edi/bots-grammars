from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'QM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B10', MIN: 1, MAX: 1},
    {ID: 'L11', MIN: 0, MAX: 300},
    {ID: 'MAN', MIN: 0, MAX: 9999},
    {ID: 'K1', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 1},
        {ID: 'L11', MIN: 0, MAX: 10},
    ]},
    {ID: 'MS3', MIN: 0, MAX: 12},
    {ID: 'LX', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'AT7', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'MS1', MIN: 0, MAX: 1},
            {ID: 'MS2', MIN: 0, MAX: 1},
        ]},
        {ID: 'L11', MIN: 0, MAX: 10},
        {ID: 'MAN', MIN: 0, MAX: 9999},
        {ID: 'Q7', MIN: 0, MAX: 10},
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'AT5', MIN: 0, MAX: 10},
        {ID: 'AT8', MIN: 0, MAX: 10},
        {ID: 'CD3', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'L11', MIN: 0, MAX: 20},
            {ID: 'AT7', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'MS1', MIN: 0, MAX: 1},
                {ID: 'MS2', MIN: 0, MAX: 1},
            ]},
            {ID: 'NM1', MIN: 0, MAX: 1},
            {ID: 'Q7', MIN: 0, MAX: 10},
            {ID: 'AT8', MIN: 0, MAX: 1},
            {ID: 'MAN', MIN: 0, MAX: 9999},
            {ID: 'N1', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 3},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'L11', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'PRF', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'L11', MIN: 0, MAX: 10},
            ]},
            {ID: 'CD3', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'L11', MIN: 0, MAX: 20},
                {ID: 'AT7', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'MS1', MIN: 0, MAX: 1},
                    {ID: 'MS2', MIN: 0, MAX: 1},
                ]},
                {ID: 'MAN', MIN: 0, MAX: 9999},
            ]},
        ]},
        {ID: 'SPO', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
        {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'BIN', MIN: 1, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
