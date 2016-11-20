from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'ED',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'ERP', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 1, MAX: 10},
    {ID: 'DMG', MIN: 0, MAX: 1},
    {ID: 'LUI', MIN: 0, MAX: 99999},
    {ID: 'IND', MIN: 0, MAX: 2},
    {ID: 'DTP', MIN: 0, MAX: 1},
    {ID: 'RAP', MIN: 0, MAX: 99999},
    {ID: 'PCL', MIN: 0, MAX: 30},
    {ID: 'NTE', MIN: 0, MAX: 100},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'IN1', MIN: 1, MAX: 15, LEVEL: [
        {ID: 'EMS', MIN: 0, MAX: 5},
        {ID: 'IN2', MIN: 1, MAX: 10},
        {ID: 'N3', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'PER', MIN: 0, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 10},
        {ID: 'NTE', MIN: 0, MAX: 1},
    ]},
    {ID: 'SST', MIN: 0, MAX: 500, LEVEL: [
        {ID: 'SSE', MIN: 0, MAX: 1000},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'ATV', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'DTP', MIN: 0, MAX: 2},
    ]},
    {ID: 'TST', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'SBT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SRE', MIN: 0, MAX: 3},
            {ID: 'NTE', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'SUM', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'NTE', MIN: 0, MAX: 50},
    ]},
    {ID: 'LX', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'HS', MIN: 0, MAX: 10},
        {ID: 'IMM', MIN: 0, MAX: 1000},
        {ID: 'HC', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'N2', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'SP', MIN: 0, MAX: 30, LEVEL: [
            {ID: 'PER', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 1},
            {ID: 'OPS', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'OPX', MIN: 0, MAX: 2},
                {ID: 'DTP', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'SES', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'SSE', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 50},
            {ID: 'N1', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 1},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'SUM', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'NTE', MIN: 0, MAX: 5},
            ]},
            {ID: 'CRS', MIN: 0, MAX: 50, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 5},
                {ID: 'CSU', MIN: 0, MAX: 1},
                {ID: 'LUI', MIN: 0, MAX: 10},
                {ID: 'RAP', MIN: 0, MAX: 5},
                {ID: 'NTE', MIN: 0, MAX: 50},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'MKS', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'LUI', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'DEG', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'SUM', MIN: 0, MAX: 5},
                {ID: 'FOS', MIN: 0, MAX: 30},
                {ID: 'N1', MIN: 0, MAX: 10},
                {ID: 'NTE', MIN: 0, MAX: 30},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
