from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[feature]) for feature in ["radius_mean", 'perimeter_mean', 'area_mean', 'symmetry_mean', 'compactness_mean', 'concave_points_mean']]
        prediction = model.predict([features])

        if prediction[0] == 0:
            prediction_text = "Do not worry, you are safe."
        else:
            prediction_text = "Please consult a doctor for further evaluation."
    except Exception as e:
        print(f"An error occurred: {e}")
        prediction_text = "Error: Please check your input values."

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
