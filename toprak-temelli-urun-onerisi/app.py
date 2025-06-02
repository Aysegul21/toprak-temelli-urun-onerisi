from flask import Flask, render_template, request, url_for
import numpy as np
import joblib

app = Flask(__name__)

# Model, scaler, label encoder yükle

model = joblib.load('/home/Random Forest_model.pkl')
scaler = joblib.load('/home/Random Forest_scaler.pkl')
label_encoder = joblib.load('/home/label_names.pkl')

# Tahmin işlemi
@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    image_path = None

    if request.method == 'POST':
        try:
            # Formdan verileri al
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Veriyi hazırlayıp ölçekle
            new_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            scaled_data = scaler.transform(new_data)

            # Tahmin yap
            predicted_class = model.predict(scaled_data)
            predicted_label = label_encoder[predicted_class[0]]
            prediction = predicted_label

            # Görsel dosya yolunu ayarla (dosya adları ürün etiketleriyle aynı olmalı)
            image_path = url_for('static', filename=f'images/{predicted_label}.jpg')

        except Exception as e:
            prediction = f"Hata: {e}"

    return render_template('arayüz.html', prediction=prediction, image_path=image_path)
