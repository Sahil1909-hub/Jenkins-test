from flask import Flask, request
import numpy as np
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Diabetes Prediction</h2>
    <form action="/predict" method="post">
        Pregnancies: <input type="text" name="f1"><br><br>
        Glucose: <input type="text" name="f2"><br><br>
        BloodPressure: <input type="text" name="f3"><br><br>
        SkinThickness: <input type="text" name="f4"><br><br>
        Insulin: <input type="text" name="f5"><br><br>
        BMI: <input type="text" name="f6"><br><br>
        DiabetesPedigreeFunction: <input type="text" name="f7"><br><br>
        Age: <input type="text" name="f8"><br><br>

        <input type="submit" value="Predict">
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['f1']),
            float(request.form['f2']),
            float(request.form['f3']),
            float(request.form['f4']),
            float(request.form['f5']),
            float(request.form['f6']),
            float(request.form['f7']),
            float(request.form['f8'])
        ]

        final_features = np.array([features])

        prediction = model.predict(final_features)[0]

        result = "Diabetic" if prediction == 1 else "Not Diabetic"

        return f"<h2>Prediction: {result}</h2><br><a href='/'>Go Back</a>"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)