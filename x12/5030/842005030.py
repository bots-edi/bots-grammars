from bots.botsconfig import *
from records005030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'NC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BNR', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 99999},
    {ID: 'PID', MIN: 0, MAX: 99999},
    {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
    ]},
    {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
    ]},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 1},
        {ID: 'PID', MIN: 0, MAX: 99999},
        {ID: 'PRS', MIN: 0, MAX: 99999},
        {ID: 'CID', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'CS', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'TMD', MIN: 0, MAX: 1},
        {ID: 'PSD', MIN: 0, MAX: 1},
        {ID: 'PWK', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
        ]},
        {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
        ]},
        {ID: 'SPS', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PSD', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
            {ID: 'STA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'NCD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'YNQ', MIN: 0, MAX: 1},
            {ID: 'NTE', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'RC', MIN: 0, MAX: 99999},
            {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'BIN', MIN: 1, MAX: 1},
            ]},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999},
            ]},
            {ID: 'NCA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NTE', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                ]},
                {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'PER', MIN: 0, MAX: 99999},
                ]},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
            ]},
            {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'FA2', MIN: 1, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
