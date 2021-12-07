import pickle

loaded_logreg = pickle.load(open('logreg.pkl', 'rb'))

url = ['stackoverflow.com/questions/']
res = loaded_logreg.predict(url)
print(res)