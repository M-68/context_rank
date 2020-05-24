# SEMANTYC
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
*Research project conducted for partial fulfilment for IIIT-H Megathon 2019*


### SEMANTYC
*REPLACING KEYWORDS WITH MEANING?*

Semantyc is a contextual search based approach that is user/ "People" centric and returns results to queries which is relevent and personalized to the user and is based on the meaning of the query of the user rather than the keywords in the query.

![Title Embeddings Cluster](https://github.com/UROP-X/semantyc/blob/master/Images/download%20(3).png)

### Introduction
The role of search plays a big role in user lifecycle. It is intended to eliminate the time spent and gain insightful information from our given queries. A common example of this would be search Engines which are primarily built for this purpose . A query q entered by the user and a target T has to be identified. There are a variety of techniques employed for efficient and insightful search results. 
Our problem statement was to find a method of finding similar research papers not domain specific , with the abstract being entered by the user. We employed a. DSSM model by Microsoft Research(MSR) and SenteceBERT on CORD-19 copus that uses similarity matching to find the relevant documents  given a query with similar meaning on Wikipedia Question Answer Dataset.
![Cluster Distribution](https://github.com/UROP-X/semantyc/blob/master/Images/download%20(2).png)

### Data Cleaning 
Cleaning a dataset should be done with as much care as one cleans his/her house.It should be noted that the cleaning procedure might heavily depend on the nature of the text as well!
Huge datasets usually are prone to having inconsistencies in the text. A general cleaning procedure  on text involves removal of stop-words, applying pattern matching regular expressions to remove unnecessary symbols in text such as +,-,&*etc., normalization (converting to lowercase) and stemming of the given text .The PorterStemmer from NLTK package was used in the following task. Highly occurring words can be discarded and considered as “virtual stop words” since they might not add any meaning and affect the model performance. 
The main goal of this particular task is to prepare our text to pass through our neural network  
#### Full Body Text



<div>
 <img src="https://github.com/UROP-X/semantyc/blob/master/Images/BODYTEXT2.png" width="500" height="300"/>
 </div>

On todays web information is distributed across various websites/platforms and is available in various foms of media which forces any user to surf mltiple websites and use various services to accomplish a certain task or get releant information on a certain query;todays traditional search is driven by advertisement and seo protocols rather than "People".


Moving furthur down the problem even after the user is directed towards the relevant website; it is almost always the case that the website provides a gigantic amount of information rather than the specific query,or the summary of the relevant information that the user is looking to find the answer for! Ths requiring the user to furthur dig into the pile of information and other hyperlinks/media to findthe desired outcome.


### Common  Search Models

*Boolean Model*


Boolean search is one of the most primitive forms of search using operators  AND , OR, NOT  with  inverted indexing in  database for efficient  retrieval. The goal of the system is to return a set of documents D which make the query q logically true. The weights wij are usually boolean values 0 /1. We could consider keyword search as a subset of the Boolean model.
This  model usually limits the heuristics and semantics of the given query might possess and relies on direct matching.[1]

*Vector Space Model*
The Vector Space Model uses the concept of words, documents as a vector to embed them and thus uses these vectors to generate semantics.

This also involves the Bag of Words technique but the term weights are represented by TF-IDF [2] scheme. Where TF: term frequency, IDF- inverse document frequency.


### Need for a  Deep Structured Model

An obvious question which the reader might encounter is the need for a deep structured model for semantics. Some of the methods which could have been employed as well are as follows.
Latent Semantic Analysis (LSA) [4] which is a common technique used for topic modeling of documents for semantic analysis along with other techniques such as Principal Component Analysis(PCA) ,Linear Discriminant Analysis(LDA) ,Latent Dirichlet Allocation(LDiA),  might have short-comings when used in combination with TF-IDF ,etc. .Word Embedding might  as well cause problems.
These models are statistical in nature and based on the distributional hypothesis[5]:words with similar context might appear in similar portions of text.  The LDiA technique heavily relies on probabilistic dirichlet distribution , it also does not care about the order of the words. Humans need to evaluate the number of latent/hidden states  which are the number of topics to be evaluated. Moreover , application of PCA and LDA leads to data loss,due to the curse of dimensionality [6] which is indeed very bad .
Word Vectors as well rely on representation of learned embeddings, this might cause issues for words outside of the given vocabulary(OOV). Moreover, word vectors dimensions are often very large as well and this may lead to problems in optimizing memory and significant impacts on training time.
Any of the above mentioned might work and yield good results as well but for large scale tasks while analysing , ranking of web data might have problems.






**run _test1.py** 

Has the pre-trained model along with the script.
Other files and models include:
*con-knrm.py  lsmod     mthzoo    nltk_data     parse.py       parse.py.save.1  run1.py       run_tests.py   run_tests1.py.save    run_tests1.py.save.2  temp.txt
example.csv  matchzoo  my-model  node_modules  parse.py.save  run.py           run1.py.save  run_tests1.py  run_tests1.py.save.1  run_tets.py           vim*

**parse.py** used to clean and accept the csv files

**Arxiv_api.py** used to extract and clean using API(still in progress

### Other Approaches
- Universal Sentence Encoder
- Sentence BERT
- BERT Embeddings +DSSM
- AnnoyIndex
- CUSTOM:)


**References & Useful Links:**

[1] https://www.semanticscholar.org/

[2] https://www.microsoft.com/en-us/research/project/dssm/

[3] https://www.microsoft.com/en-us/research/publication/learning-deep-structured-semantic-models-for-web-search-using-clickthrough-data/

[4] https://dl.acm.org/doi/abs/10.1145/775152.775250

[5]https://scholar.google.com/scholar?hl=en&as_sdt=0,5&q=recommendationsystem&btnG=&oq=recommendation%20s

[6]https://www.elastic.co/

**Supplementary Material**

[1]https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf

[2]https://pathmind.com/wiki/bagofwords-tf-idf

[3]https://www.microsoft.com/en-us/research/publication/learning-deep-structured-semantic-models-for-web-search-using-clickthrough-data/

[4]https://nlp.stanford.edu/IR-book/html/htmledition/latent-semantic-indexing-1.html

[5]http://soda.swedish-ict.se/3941/1/sahlgren.distr-hypo.pdf

[6]https://www.youtube.com/watch?v=QZ0DtNFdDko&t=3s

[7]https://en.wikipedia.org/wiki/Generative_model#Relationships_between_models




## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Agrover112"><img src="https://avatars3.githubusercontent.com/u/42321810?v=4" width="100px;" alt=""/><br /><sub><b>Agrover112</b></sub></a><br /><a href="#content-Agrover112" title="Content">🖋</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
