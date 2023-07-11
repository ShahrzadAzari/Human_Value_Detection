#!/usr/bin/env python

import argparse
import numpy as np
import random

from utils.gradcheck import gradcheck_naive, grad_tests_softmax, grad_tests_negsamp
from utils.utils import normalizeRows, softmax


def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s


def naiveSoftmaxLossAndGradient(
    centerWordVec,
    outsideWordIdx,
    outsideVectors,
    dataset
):
    y_hat = softmax(np.matmul(centerWordVec, outsideVectors.T))
    loss = - np.log(y_hat[outsideWordIdx])
    gradCenterVec = np.matmul(outsideVectors.T, y_hat) - outsideVectors[outsideWordIdx]
    gradOutsideVecs = np.matmul(y_hat[:, np.newaxis], centerWordVec[np.newaxis, :])
    gradOutsideVecs[outsideWordIdx] -= centerWordVec
    return loss, gradCenterVec, gradOutsideVecs


def getNegativeSamples(outsideWordIdx, dataset, K):
    negSampleWordIndices = [None] * K
    for k in range(K):
        newidx = dataset.sampleTokenIdx()
        while newidx == outsideWordIdx:
            newidx = dataset.sampleTokenIdx()
        negSampleWordIndices[k] = newidx
    return negSampleWordIndices


def negSamplingLossAndGradient(
    centerWordVec,
    outsideWordIdx,
    outsideVectors,
    dataset,
    K=10
):
    negSampleWordIndices = getNegativeSamples(outsideWordIdx, dataset, K)
    indices = [outsideWordIdx] + negSampleWordIndices

    u_o = outsideVectors[outsideWordIdx]
    u_oTv = np.matmul(u_o.T, centerWordVec)
    u_w_s = outsideVectors[negSampleWordIndices]
    u_w_sv = np.matmul(u_w_s, centerWordVec)
    loss = - np.log(sigmoid(u_oTv)) - np.sum(np.log(sigmoid(-u_w_sv)))
    
    gradCenterVec = (-np.multiply(u_o, (1- sigmoid(u_oTv))) +
                        np.sum(
                            np.multiply(u_w_s, 1 - sigmoid(-u_w_sv)[:, np.newaxis]), axis=0
                        )
                    )

    gradOutsideVecs = np.zeros(outsideVectors.shape)
    neg_grads = np.multiply((1 - sigmoid(-u_w_sv)[:, np.newaxis]), centerWordVec.T)
    for i in range(K):
        gradOutsideVecs[negSampleWordIndices[i]] += neg_grads[i]
    gradOutsideVecs[outsideWordIdx] = -np.multiply((1 - sigmoid(np.matmul(u_o, centerWordVec))), centerWordVec.T)

    return loss, gradCenterVec, gradOutsideVecs


def skipgram(currentCenterWord, windowSize, outsideWords, word2Ind,
             centerWordVectors, outsideVectors, dataset,
             word2vecLossAndGradient=naiveSoftmaxLossAndGradient):

    loss = 0.0
    gradCenterVecs = np.zeros(centerWordVectors.shape)
    gradOutsideVectors = np.zeros(outsideVectors.shape)

    ### YOUR CODE HERE (~8 Lines)
    currentCenterInx = word2Ind[currentCenterWord]
    v_c = centerWordVectors[currentCenterInx]
    for j in range(2*windowSize):
        if j < len(outsideWords):
            w_tj = word2Ind[outsideWords[j]]
            loss_grands = word2vecLossAndGradient(v_c, w_tj, outsideVectors, dataset)
            loss += loss_grands[0]
            gradCenterVecs[currentCenterInx] += loss_grands[1]
            gradOutsideVectors += loss_grands[2]
    ### END YOUR CODE
    
    return loss, gradCenterVecs, gradOutsideVectors


def word2vec_sgd_wrapper(word2vecModel, word2Ind, wordVectors, dataset,
                         windowSize,
                         word2vecLossAndGradient=naiveSoftmaxLossAndGradient):
    batchsize = 50
    loss = 0.0
    grad = np.zeros(wordVectors.shape)
    N = wordVectors.shape[0]
    centerWordVectors = wordVectors[:int(N/2),:]
    outsideVectors = wordVectors[int(N/2):,:]
    for i in range(batchsize):
        windowSize1 = random.randint(1, windowSize)
        centerWord, context = dataset.getRandomContext(windowSize1)

        c, gin, gout = word2vecModel(
            centerWord, windowSize1, context, word2Ind, centerWordVectors,
            outsideVectors, dataset, word2vecLossAndGradient
        )
        loss += c / batchsize
        grad[:int(N/2), :] += gin / batchsize
        grad[int(N/2):, :] += gout / batchsize

    return loss, grad
