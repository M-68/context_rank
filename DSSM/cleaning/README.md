# Data Cleaning Steps
- Unicode format checking
- Special Character Removal
-Stopwords Removal/Optional
- Numbers Removal/Optional
- others








Not TL:DR
Cleaning a dataset should be done with as much care as one cleans his/her house.It should be noted that the cleaning procedure might heavily depend on the nature of the text as well! Huge datasets usually are prone to having inconsistencies in the text. A general cleaning procedure on text involves removal of stop-words, applying pattern matching regular expressions to remove unnecessary symbols in text such as +,-,&*etc., normalization (converting to lowercase) and stemming of the given text .The PorterStemmer from NLTK package was used in the following task. Highly occurring words can be discarded and considered as “virtual stop words” since they might not add any meaning and affect the model performance. The main goal of this particular task is to prepare our text to pass through our neural network.
