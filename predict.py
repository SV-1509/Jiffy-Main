import gensim

model = gensim.models.Word2Vec.load('finance3.model')
#print(model.similarity('profit','gain'))
print(model.most_similar(positive = ['business','start']))
print(model.wv.vectors.shape[0])
