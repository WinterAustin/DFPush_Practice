from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for handling GET requests
@app.route('/get', methods=['GET'])
def get_route():
    return jsonify({"message": "success"})

# Route for handling POST requests
@app.route('/post', methods=['POST'])
def post_route():
    data = request.json  # Extract JSON data from the POST request
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
