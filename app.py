from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'nw7s3vfvrwfd5av5v0war6st8nsuqzf7'
API_URL = 'https://shortenworld.com/api/v1/shorten'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    payload = {'url': original_url, 'api_key': API_KEY}

    response = requests.post(API_URL, json=payload)
    data = json.loads(response.text)

    if response.status_code == 200 and data['status'] == 'success':
        short_url = data['short_url']
        return render_template('success.html', original_url=original_url, short_url=short_url)
    else:
        error_message = data['message']
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

