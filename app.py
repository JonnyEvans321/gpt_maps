from flask import Flask, render_template, request, jsonify, redirect, url_for
from gpt_responses import get_first_response, get_coordinates
import os
app = Flask(__name__)

@app.route('/plot_coordinates', methods=['POST'])
def plot_coordinates():
    description = request.form['description']
    response = get_coordinates(description)
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    bing_api_key = os.environ.get("BING_API_KEY")
    if request.method == 'POST':
        user_input = request.form['user_input']
        return get_first_response(user_input)
    return render_template('initial.html', bing_api_key=bing_api_key)

@app.route('/response', methods=['GET'])
def response():
    bing_api_key = os.environ.get("BING_API_KEY")
    return render_template('response.html', bing_api_key=bing_api_key)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
