# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 2016

Autor: DiegoDZ

Compute the cross correlation of all columns of two input matrix, A and B.
"""
import numpy as np
import sys

def crossCorrelation(arg1,arg2):

    #Load files
    A = np.loadtxt(str(arg1))
    B = np.loadtxt(str(arg2))

    #Number rows (nSteps) and columns (nNodes). A and B have the same size.
    nSteps = len(A)
    nNodes = len(A[0])
    #Checkpoint
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        sys.exit("Error: A and B do not have the same size")

    #Take FFT of each column of both input matrix.
    #Multiply one resulting transform by the comples conjugate of the other.
    #Calculate the inverse transform of the product.
    CAB = np.zeros((nSteps, nNodes))
    for i in range(0,nNodes,1):
         CAB[:,i] = np.fft.ifft(np.fft.fft(A[:,i] - np.mean(A[:,i]) ) \
         * np.conjugate(np.fft.fft(B[:,i]- np.mean(B[:,i]))))
    CAB /= nSteps
    return CAB


CAB = crossCorrelation(sys.argv[1],sys.argv[2])
#Print the result
aux = ''
for line in CAB:
    for element in line:
        aux = aux + str(element) + ' '
    aux = aux + '\n'

print aux


#EOF

