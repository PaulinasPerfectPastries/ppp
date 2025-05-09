from flask import Flask, send_file
import os

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/styles.css')
def styles():
    return send_file('styles.css')

@app.route('/photos/<path:filename>')
def serve_photo(filename):
    return send_file(os.path.join('photos', filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 