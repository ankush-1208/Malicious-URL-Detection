from flask import Flask, request, jsonify, render_template, redirect
import pickle

app = Flask(__name__)
model = pickle.load(open('logreg.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form.get("url_name")
        lst = []
        lst.append(url)
        prediction = model.predict(lst)
        lst.clear()
        for op in prediction:
            if op == 'good':
                return render_template('index.html', prediction_text = 'This URL is Safe')
            elif op == 'bad':
                return render_template('index.html', prediction_text = 'This URL might be Malicious')
            else:
                return render_template('index.html', prediction_text = 'Try Again...')
    else:
        return redirect('/')
        
        
            
            

if __name__ == '__main__':
    app.run(debug=True)