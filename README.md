# Word Embeddings for Financial Domain
  This repository contains the code for the creattion and implementation of word embeddings for the financial domain.
  The dataset was created by scraping articles from investopedia and the word embeddings model was created using         **Word2Vec**
  All models generated are in the **models** directory and all the csv files nneded are in the **csv** directory
  
## Webscraping
The webscraping part was implemented using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library in Python which is useful pulling and parsing content out of HTML and XML files. The website used to scrape the data from is [Investopedia](https://www.investopedia.com/).
**scrap_term_definitions.py** has the code for scraping the paragraph content of all the financial term definitions given in Investopedia and **scrap_articles.py** is for scraping all the articles related to finance


## Data Preprocessing
The **dataset** folder consists of all the scraped content which is the dataset on which the model is trained upon

### Cleaning
The cleaning procedure is done in **clean.py**. It uses the [NLTK](https://www.nltk.org/) library for Python which has a lot of useful tools for Natural language processing tasks. The steps involved in cleaning are:
  * Remove punctuation using the **String** module
  * Remove stopwords using the NLTK library
  * Lemmatization using POS tag of all the words using WordNetLemmatizer from NLTK library

### Preprocessing
The cleaned corpus is then preprocessed in the **preprocess.py** file where the corpus is stored as a list of lists format to be given as input to the Word2Vec model


## Word2Vec
The Word2Vec model was implemented using the [Gensim](https://radimrehurek.com/gensim/) module for NLP. The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Words are distributed in a vector space depending on the context in which it is used.  
The **word2vec.py** contains the implementation of the word2vec model. In the model used here a window size of 5, hidden layer dimension of 300 was used on a CBOW model. In order to train your own custom corpus and build a model, place all your text files in a single or multiple folder. Place this folder inside the dataset directory and run the *word2vec.py* file. Change the name of the model and the resultant trained model will be stored in the models directory.
The **predict.py** has code for the desired predictions we want. For example using our model **word2vec.txt** when the word vector of *company* was subtraced from the word vector of *business* the resultant vector was of the word *enterpreunership*.

## GloVe
The GloVe algorithm was used to train the custom corpus to create the model **glove.txt**. This was trained by creating a corpus that was fed into the GloVe model implemented by Stanford Univeristy which can be found [here](https://github.com/stanfordnlp/GloVe). The corpus was created in the appropriate fromat by running the **corpus.py**.

All the models used can be found in the /models directory.

## FinHelper Module
The end product involves the user searching a word and the model returning the fucntion matches for that particlar word. Here the combination of both Word2Vec and GloVe was used for providing results.
The file **finhelper.py** when run, takes an input word from the user and returns the function/functions that is most similar in context to the input word. The following steps are involved in the process.

#### FinancePy Functions
All the FinancePy functions, its syntax and corresponding function description is obtained from [FinancePy documantation](https://github.com/domokane/FinancePy). This is contained in the **/csv/financepy.csv**. Each row corresponds to a singe function, its syntax and its function description. This file was cleaned and null values removed for better results.

#### FinHelper Module
This is the helper module that interacts with the user to provide a function match for any input word. It has the following steps
  * Creating keywords to be inputted into the model. The last term in the fucntion name was taken, and split appropriately for obtaining meaningnful words to be given as input to the model.
  * Creating the helper dictionary. The keyowrds generated are fed into the model and similarity words are obtained using a threshold value. Coresponding words are matched to functions and are stored in a dictionary. **make_helper_dictionary_4.csv** and **make_helper_dictionary_5.csv** contains the dictionary entries for the Word2Vec and Glove model respectively. The results are combined by running the file **combine_csv.py** to give the final dictionary **make_helper_dictionary_6.csv**.
  * **finhelper.py** references the input word from the user to find a match in the helper dictionary and return possible matcghes. The user can interactively choose which function he/she needs and recieve its syntax and function description
  * An interactive environment using tkinter is provided where the user can call the finhelper module and enter a word. FinHelper returns results , and the user can copy the syntax to his/her clipboard for easy use.




