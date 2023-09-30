from flask import Flask, request, jsonify
import openai
import random
import time
from secret_key import mytestkey
from citycheck import generate_city_data

# Initialize Flask
app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = mytestkey

@app.route('/generate_city_data', methods=['POST'])
def generate_city_data():
    try:
        data = request.get_json()

        # Get the city name from the request
        city_name = data.get("city_name")

        # ... (rest of your code for generating city data)

        return generate_city_data(city_name)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
