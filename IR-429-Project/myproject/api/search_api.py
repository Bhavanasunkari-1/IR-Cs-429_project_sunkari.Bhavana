from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import logging
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, content_security_policy=None, force_https=False)  # Enforce HTTPS and set security headers but disable CSP for local testing

# Configure logging
logging.basicConfig(filename='api.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Load TF-IDF model and matrix
try:
    with open('/mnt/c/users/pamid/Downloads/nws/myproject/data/tfidf_model.pkl', 'rb') as f:
        vectorizer, tfidf_matrix = pickle.load(f)
    with open('/mnt/c/users/pamid/Downloads/nws/myproject/data/output.json', 'r') as f:
        data = json.load(f)
except Exception as e:
    app.logger.error(f"Failed to load the model or data: {e}")
    vectorizer, tfidf_matrix, data = None, None, None

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return render_template('index.html')  # Ensure 'index.html' is located in the 'templates' folder

@app.route('/search', methods=['POST'])
def search():
    if request.json and 'query' in request.json:
        query = request.json.get('query', '')
        top_k = request.json.get('top_k', 5)

        if not query:
            app.logger.warning("Empty query provided")
            return jsonify({'error': 'Empty query provided'}), 400

        try:
            query_vec = vectorizer.transform([query])
            scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
            top_indices = np.argsort(scores)[::-1][:top_k]
            results = [{'title': data[i]['title'], 'score': scores[i]} for i in top_indices]
            return jsonify(results)
        except Exception as e:
            app.logger.error(f"Error processing the search: {e}")
            return jsonify({'error': 'Error processing your query'}), 500
    else:
        app.logger.warning("Invalid request format")
        return jsonify({'error': 'Invalid request format'}), 400

@app.route('/api-docs')
def api_docs():
    return jsonify({
        "routes": {
            "/": "Home page",
            "/search": "POST to perform a search. Requires JSON payload with 'query'. Optional 'top_k' for number of results."
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
