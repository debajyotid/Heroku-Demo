"""
This file is used to demonstrate the capability to invoke the Flask based WebAPI locally, and passing the features via a url, w/o having to render and access the index.html via a browser
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
