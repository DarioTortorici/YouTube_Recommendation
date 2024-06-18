from flask import Flask, render_template, request, jsonify
from app import app
import requests
from transformers import DistilBertTokenizer, DistilBertModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_videos():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify({'error': 'Invalid query parameter'}), 400

    api_key = 'YOUR_API_KEY' # INSERT YOUR YOUTUBE API KEY HERE
    api_url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&part=snippet&type=video&maxResults=10&q={query}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch videos: {str(e)}'}), 500
    
# Load model and tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')


def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

@app.route('/relevance', methods=['POST'])
def compute_relevance():
    data = request.json
    if data is None:
        app.logger.error('Invalid JSON data received')
        return jsonify({'error': 'Invalid JSON data received'}), 400
    
    query = data.get('query')
    video_description = data.get('video_description')
    
    if not query or not video_description:
        app.logger.error('Invalid input: query or video_description missing')
        return jsonify({'error': 'Invalid input'}), 400

    try:
        query_embedding = get_embedding(query)
        video_embedding = get_embedding(video_description)
        similarity = cosine_similarity(query_embedding, video_embedding)

        relevance_score =  relevance_score = float(similarity[0][0]) 
        return jsonify({'relevance_score': relevance_score})
    except Exception as e:
        app.logger.error(f'Error computing relevance: {e}')
        return jsonify({'error': 'Error computing relevance'}), 500

if __name__ == '__main__':
    app.run(debug=True)








