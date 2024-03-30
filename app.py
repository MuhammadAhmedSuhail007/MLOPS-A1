from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        carat = float(request.form['carat'])
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])

        prediction = model.predict([[
            carat, depth, table, x,
            y, z
        ]])

        return render_template('result.html', prediction=prediction[0])

    return render_template('predict.html')


if __name__ == '__main__':
    app.run(port=8081, host="0.0.0.0")
