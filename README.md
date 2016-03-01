# CRF++ 
##Why Visual Studio
The [CRF++](https://taku910.github.io/crfpp/) project is very famous in the research and industry domains. But it's hard to get the CRF++-0.58(The latest version) source code and build it in Windows. So today I build it with Visual Studio in Windows and hope it can help you.

##Introduction
[CRF++](https://taku910.github.io/crfpp/) is a simple, customizable, and open source implementation of Conditional Random Fields (CRFs) for segmenting/labeling sequential data. CRF++ is designed for generic purpose and will be applied to a variety of NLP tasks, such as Named Entity Recognition, Information Extraction and Text Chunking.

##Features
*	Can redefine feature sets
*	Written in C++ with STL
*	Fast training based on LBFGS, a quasi-newton algorithm for large scale numerical optimization problem
*	Less memory usage both in training and testing
*	encoding/decoding in practical time
*	Can perform n-best outputs
*	Can perform single-best MIRA training
*	Can output marginal probabilities for all candidates
*	Available as an open source software


##Train(encoding)
**Use crf_learn command:**

	crf_learn template_file train_file model_file

where template_file and train_file are the files you need to prepare in advance. crf_learn generates the trained model file in model_file.

crf_learn outputs the following information.

    CRF++: Yet Another CRF Tool Kit
    Copyright(C) 2005 Taku Kudo, All rights reserved.

    reading training data: 100.. 200.. 300.. 400.. 500.. 600.. 700.. 800.. 
    Done! 1.94 s

    Number of sentences: 823
    Number of features:  1075862
    Number of thread(s): 1
    Freq:                1
    eta:                 0.00010
    C:                   1.00000
    shrinking size:      20
    Algorithm:           CRF

    iter=0 terr=0.99103 serr=1.00000 obj=54318.36623 diff=1.00000
    iter=1 terr=0.35260 serr=0.98177 obj=44996.53537 diff=0.17161
    iter=2 terr=0.35260 serr=0.98177 obj=21032.70195 diff=0.53257
    iter=3 terr=0.23879 serr=0.94532 obj=13642.32067 diff=0.35138
    iter=4 terr=0.15324 serr=0.88700 obj=8985.70071 diff=0.34134
    iter=5 terr=0.11605 serr=0.80680 obj=7118.89846 diff=0.20775
    iter=6 terr=0.09305 serr=0.72175 obj=5531.31015 diff=0.22301
    iter=7 terr=0.08132 serr=0.68408 obj=4618.24644 diff=0.16507
    iter=8 terr=0.06228 serr=0.59174 obj=3742.93171 diff=0.18953
    
*	iter: number of iterations processed
*	terr: error rate with respect to tags. (# of error tags/# of all tag)
*	serr: error rate with respect to sentences. (# of error sentences/# of all sentences)
*	obj: current object value. When this value converges to a fixed point, CRF++ stops the iteration.
*	diff: relative difference from the previous object value.

##Testing (decoding)
**Use crf_test command:**

	crf_test -m model_file test_files ...
    
where model_file is the file crf_learncreates. In the testing, you don't need to specify the template file, because the model file has the same information for the template. test_file is the test data you want to assign sequential tags. This file has to be written in the same format as training file.

**Here is an output of crf_test:**


    Rockwell        NNP     B       B
    International   NNP     I       I
    Corp.   NNP     I       I
    's      POS     B       B
    Tulsa   NNP     I       I
    unit    NN      I       I
    ..