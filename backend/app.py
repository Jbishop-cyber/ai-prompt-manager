from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- import CORS properly
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # <-- enable cross-origin requests

# ------------------------
# Home route (for testing)
# ------------------------
@app.route('/')
def home():
    return jsonify({"message": "AI Prompt Manager API is running!"})

# ------------------------
# Database helper
# ------------------------
def get_db_connection():
    # Path to prompts.db relative to this script
    db_path = os.path.join(os.path.dirname(__file__), '../data/prompts.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Allows dict-like access to rows
    return conn

# ------------------------
# List all prompts
# ------------------------
@app.route('/prompts', methods=['GET'])
def list_prompts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prompts")
    prompts = cursor.fetchall()
    conn.close()

    # Convert rows to list of dicts
    prompt_list = []
    for p in prompts:
        prompt_list.append({
            "id": p["id"],
            "title": p["title"],
            "category": p["category"],
            "prompt_text": p["prompt_text"],
            "example_output": p["example_output"]
        })
    return jsonify(prompt_list)

# ------------------------
# Create a new prompt
# ------------------------
@app.route('/prompts', methods=['POST'])
def create_prompt():
    data = request.get_json()

    title = data.get('title')
    category = data.get('category')
    prompt_text = data.get('prompt_text')
    example_output = data.get('example_output')

    if not title or not prompt_text:
        return jsonify({"error": "Title and prompt_text are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO prompts (title, category, prompt_text, example_output) VALUES (?, ?, ?, ?)",
        (title, category, prompt_text, example_output)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({"message": "Prompt created", "id": new_id}), 201

# ------------------------
# Run the server
# ------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)