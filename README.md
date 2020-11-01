# Word Embeddings for Financial Domain
  This repository contains the code for the creattion and implementation of word embeddings for the financial domain.
  The dataset was created by scraping articles from investopedia and the word embeddings model was created using         **Word2Vec**
  
## Webscraping
The webscraping part was implemented using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library in Python which is useful pulling and parsing content out of HTML and XML files. The website used to scrape the data from is [Investopedia](https://www.investopedia.com/).
**scrap_term_definitions.py** has the code for scraping the paragraph content of all the financial term definitions given in Investopedia and **scrap_articles.py** is for scraping all the articles related to finance


## Data Preprocessing
The **dataset** folder consists of all the scraped content which is the dataset on which the model is trained upon

### Cleaning
The cleaning procedure is done in **clean.py**. It uses the [NLTK](https://www.nltk.org/) library for Python which has a lot of useful tools for Natural language processing tasks. The steps involved in cleaning are:
  * Remove punctuation using the **String** module
  * Remove stopwords using the NLTK library
  * Lemmatization of all the words using WordNetLemmatizer from NLTK library

### Preprocessing
The cleaned corpus is then preprocessed in the **preprocess.py** file where the corpus is stored as a list of lists format to be given as input to the Word2Vec model


## Word2Vec
The Word2Vec model was implemented using the [Gensim](https://radimrehurek.com/gensim/) module for NLP. The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Words are distributed in a vector space depending on the context in which it is used.  
The **word2vec.py** contains the implementation of the word2vec model. In the model used here a window size of 5, hidden layer dimension of 300 was used on a CBOW model
The **predict.py** has code for the desired predictions we want. For example using our model **finance3.model** when the word vector of *company* was subtraced from the word vector of *business* the resultant vector was of the word *enterpreunership*

