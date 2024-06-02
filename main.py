import pickle
from flask import Flask, render_template, request 


# Create an object of the class flask

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

# url/
@app.route('/')
def index():
    return render_template('index.html')    


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    temperature = request.form.get('temperature')
    try:
        if temperature is not None:
            temperature = float(temperature)
            prediction = model.predict([[temperature]])
            output = round(prediction[0], 2)
            return render_template('index.html', prediction_text = f'Total revenue generated is Rs. {output}/-')
        else:
            return render_template('index.html', prediction_text = f'iNVALID INPUT')
    except:
        return render_template('index.html', prediction_text = f'iNVALID INPUT')
    

if __name__=='__main__':
    app.run(debug=True)