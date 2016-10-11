#!/usr/bin/python
#coding:utf-8
import glob
bch_c = glob.bch_c
bch_k = glob.bch_k

def encode(origin_data):
    zero = [0]
    bb = []
    bb.extend((bch_c)*zero)
    for i in range(bch_k):
        freeback= origin_data[i] ^ bb[0]
        if freeback != 0:      
            for j in range(bch_c-1):
                if glob.g[j] !=0 :        
                    bb[j]=bb[j+1] ^freeback
                else:
                    bb[j]=bb[j+1]
            bb[bch_c-1] = glob.g[bch_c-1] & freeback
        else:
            for j in range(bch_c-1):
                bb[j]=bb[j+1]   
            bb[bch_c-1] = 0
    return bb
