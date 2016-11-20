from bots.botsconfig import *
from records003050 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SM',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B2', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'Y6', MIN: 0, MAX: 4},
    {ID: 'C2', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 300},
    {ID: 'MAN', MIN: 0, MAX: 300},
    {ID: 'G62', MIN: 0, MAX: 6},
    {ID: 'R3', MIN: 0, MAX: 12},
    {ID: 'H3', MIN: 0, MAX: 6},
    {ID: 'H6', MIN: 0, MAX: 6},
    {ID: 'LH6', MIN: 0, MAX: 6},
    {ID: 'K1', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 5},
        {ID: 'G61', MIN: 0, MAX: 3},
    ]},
    {ID: 'N7', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N7A', MIN: 0, MAX: 1},
        {ID: 'N7B', MIN: 0, MAX: 1},
        {ID: 'M7', MIN: 0, MAX: 2},
    ]},
    {ID: 'SPO', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'SDQ', MIN: 0, MAX: 10},
    ]},
    {ID: 'S5', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'LAD', MIN: 0, MAX: 999},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'MAN', MIN: 0, MAX: 300},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'H3', MIN: 0, MAX: 6},
        {ID: 'H6', MIN: 0, MAX: 6},
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'SPO', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
        {ID: 'N1', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 5},
            {ID: 'G61', MIN: 0, MAX: 3},
            {ID: 'N7', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N7A', MIN: 0, MAX: 1},
                {ID: 'N7B', MIN: 0, MAX: 1},
                {ID: 'M7', MIN: 0, MAX: 2},
            ]},
        ]},
    ]},
    {ID: 'LX', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 5},
        {ID: 'MAN', MIN: 0, MAX: 300},
        {ID: 'L5', MIN: 0, MAX: 30},
        {ID: 'LAD', MIN: 0, MAX: 999},
        {ID: 'H1', MIN: 0, MAX: 3},
        {ID: 'H2', MIN: 0, MAX: 2},
        {ID: 'L0', MIN: 0, MAX: 10},
        {ID: 'L1', MIN: 0, MAX: 10},
        {ID: 'L4', MIN: 0, MAX: 10},
        {ID: 'L7', MIN: 0, MAX: 10},
        {ID: 'K1', MIN: 0, MAX: 10},
        {ID: 'G61', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'N9', MIN: 0, MAX: 5},
            {ID: 'LH6', MIN: 0, MAX: 6},
            {ID: 'LH1', MIN: 0, MAX: 25, LEVEL: [
                {ID: 'LH2', MIN: 0, MAX: 4},
                {ID: 'LH3', MIN: 0, MAX: 10},
                {ID: 'LFH', MIN: 0, MAX: 20},
                {ID: 'LEP', MIN: 0, MAX: 3},
                {ID: 'LH4', MIN: 0, MAX: 1},
                {ID: 'LHT', MIN: 0, MAX: 3},
                {ID: 'N9', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'N1', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 10},
            {ID: 'CD3', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 20},
                {ID: 'H6', MIN: 0, MAX: 10},
                {ID: 'L9', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'SPO', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'SDQ', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'L3', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
