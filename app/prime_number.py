#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getPrimeNumber(startPoint, endPoint):
    primeList = []
    for val in range(startPoint, endPoint + 1): 
        
        # If num is divisible by any number 
        # between 2 and val, it is not prime 
        if val > 1: 
            for n in range(2, val): 
                if (val % n) == 0: 
                    break
            else: 
                primeList.append(val)
    return primeList 

