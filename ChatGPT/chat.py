import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Set up the OpenAI API credentials
openai.api_key = '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'

# Define the endpoint for handling incoming queries
@app.route('/query', methods=['POST'])
def handle_query():
    # Get the user's input from the request body
    input_text = request.json['text']

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='davinci',  # Change this to the GPT-3 model you want to use
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Return the response to the user
    return jsonify({'text': response.choices[0].text})

# Start the Flask app
if __name__ == '__main__':
    app.run()
