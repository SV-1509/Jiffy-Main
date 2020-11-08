import gensim


model = gensim.models.KeyedVectors.load_word2vec_format('word2vec.txt', binary = False)
print(model.similarity('profit','gain'))
print(model.most_similar(positive = ['company'],negative = ['expenditure']))


