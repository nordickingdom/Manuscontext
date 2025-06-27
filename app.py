import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
CORS(app)

# Simple in-memory storage for contexts
contexts = []

@app.route('/')
def home():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/contexts', methods=['GET'])
def get_contexts():
    """Get all saved contexts"""
    return jsonify(contexts)

@app.route('/api/contexts', methods=['POST'])
def save_context():
    """Save a new context"""
    data = request.get_json()
    
    context = {
        'id': len(contexts) + 1,
        'title': data.get('title', 'Untitled Context'),
        'description': data.get('description', ''),
        'content': data.get('content', ''),
        'timestamp': data.get('timestamp', '')
    }
    
    contexts.append(context)
    return jsonify({'success': True, 'context': context})

@app.route('/api/contexts/<int:context_id>', methods=['DELETE'])
def delete_context(context_id):
    """Delete a context"""
    global contexts
    contexts = [c for c in contexts if c['id'] != context_id]
    return jsonify({'success': True})

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'contexts_count': len(contexts)})

if __name__ == '__main__':
    # Railway deployment configuration
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

