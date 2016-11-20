from bots.botsconfig import *
from records005020 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HU',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'COM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'YNQ', MIN: 0, MAX: 99999},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'III', MIN: 0, MAX: 99999},
        {ID: 'LUI', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'PCT', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'CQ', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FOS', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'ISI', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'DEG', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'FOS', MIN: 0, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 99999},
            ]},
            {ID: 'CRS', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'CSU', MIN: 0, MAX: 1},
            ]},
            {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'EMS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'ISI', MIN: 0, MAX: 99999},
            {ID: 'ESI', MIN: 0, MAX: 1},
            {ID: 'LQ', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'ELV', MIN: 0, MAX: 15},
            {ID: 'AIN', MIN: 0, MAX: 25},
            {ID: 'CN1', MIN: 0, MAX: 1},
            {ID: 'CON', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PCT', MIN: 0, MAX: 1},
            ]},
            {ID: 'N1', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
            {ID: 'SES', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'WLD', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N1', MIN: 0, MAX: 1},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'PCT', MIN: 0, MAX: 99999},
                    {ID: 'YNQ', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
