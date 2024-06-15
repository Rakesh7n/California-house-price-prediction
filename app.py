        
   
from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib
from joblib import load
app = Flask(__name__)

#model = pickle.load(open('model.pkl', 'rb'))
model = joblib.load('model.joblib')
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/pred',methods=['POST','GET'])
def predict_house_price():


    longitude = float(request.form.get('longitude'))



    latitude =float(request.form.get('latitude'))


    housing_median_age=int(request.form.get('housing_median_age'))


    total_rooms=float(request.form.get('total_rooms'))


    total_bedrooms=float(request.form.get('total_bedrooms'))


    population=float(request.form.get('population'))


    households =float(request.form.get('households'))


    median_income=float(request.form.get('median_income'))



    ocean_proximity_OCEAN=int(request.form.get('ocean_proximity_OCEAN'))



    ocean_proximity_INLAND=int(request.form.get('ocean_proximity_INLAND'))


    ocean_proximity_ISLAND=int(request.form.get('ocean_proximity_ISLAND'))
    
        
    ocean_proximity_NEARBAY=int(request.form.get('ocean_proximity_NEARBAY'))
        
    ocean_proximity_NEAROCEAN=int(request.form.get('ocean_proximity_NEAROCEAN'))

    result = model.predict(np.array([[longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity_OCEAN,ocean_proximity_INLAND,ocean_proximity_ISLAND,ocean_proximity_NEARBAY,ocean_proximity_NEAROCEAN]]))
    result=str(result)
    output = result.strip("[]")
    output = "${:.2f}".format(float(output))

    return render_template('result.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    

