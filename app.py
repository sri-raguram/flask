from flask import Flask, jsonify

app = Flask(__name__)

# The General GET command processing
@app.route('/api', methods=['GET'])  # Add '/api' to specify the API route
def index():
    return jsonify({
        'message': 'Welcome to BRTGPT',
        'status': 'SUCCESS'
    })

if __name__ == '__main__':
    app.run()
