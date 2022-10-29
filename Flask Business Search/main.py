from flask import Flask, request
import json
import requests


app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/detailed_search/<id>', methods=['GET'])
def detailed_search(id):
    api_key = '87HMETbGH1RdNiepFTLFgN1-7WSytnjQ4KyVI--vQaSz09vPpVyVSBhaIASTOR7HYX54UYqUNBI5Go4cyrtDDmXTe_j0KS8Ir6YdPn8VEFSd_nD4MJNKt94sTdUYY3Yx'
    endpoint = 'https://api.yelp.com/v3/businesses/' + id
    resp_header = {'Authorization': 'bearer %s' % api_key}

    PARAMETERS = {}

    data = requests.get(url=endpoint, params=PARAMETERS, headers=resp_header)
    business = data.json()
    return business


@app.route('/search', methods=['GET'])
def search():
    print(request.args)
    term = request.args.get('term')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    category = request.args.get('categories')
    radius = request.args.get('radius')

    # define api key, endpoint, and header for request to Yelp API
    api_key = '87HMETbGH1RdNiepFTLFgN1-7WSytnjQ4KyVI--vQaSz09vPpVyVSBhaIASTOR7HYX54UYqUNBI5Go4cyrtDDmXTe_j0KS8Ir6YdPn8VEFSd_nD4MJNKt94sTdUYY3Yx'
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    resp_header = {'Authorization': 'bearer %s' % api_key}

    if 'All' in category:
       PARAMETERS = {'term' : term, 
        'latitude': latitude, 
        'longitude': longitude,
        'radius' : radius}
    else: 
        PARAMETERS = {'term' : term, 
        'latitude': latitude, 
        'longitude': longitude,
        'radius' : radius,
       'categories': category} 
    print("final location ", latitude, longitude)

    data = requests.get(url=endpoint, params=PARAMETERS, headers=resp_header)
    print(data)
    businesses = data.json()
    return businesses 

if __name__ == '__main__':
    app.run(debug=True)
