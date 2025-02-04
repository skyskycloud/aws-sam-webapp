from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from AWS Lambda!",
        "version": os.getenv("VERSION", "1.0")
    })

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": home().data.decode('utf-8')
    }

if __name__ == "__main__":
    app.run(debug=True)
