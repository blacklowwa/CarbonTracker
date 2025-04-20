from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Пример расчета для транспорта
    car_distance = float(request.form.get('car_distance', 0))
    transport_co2 = car_distance * 0.12 #0.12 кг CO₂ на км
    return render_template('result.html', co2=transport_co2)

if __name__ == '__main__':
    app.run(debug=True)