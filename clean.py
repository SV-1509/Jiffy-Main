from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import re
import string

stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def clean(doc):
	doc = ''.join([i for i in doc if not i.isdigit()])
	doc = doc.lower()
	doc = re.sub("[!@#$+%*:()'-]", ' ', doc)
	doc = doc.translate(str.maketrans("","",string.punctuation))
	word_list = doc.split()
	filtered_words = [word for word in word_list if word not in stopwords and len(word)>2]
	lem_text = [lemmatizer.lemmatize(i) for i in filtered_words]
	return lem_text