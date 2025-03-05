from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Replace with your actual Supabase credentials
SUPABASE_URL = "https://glvqdlzsvdmvplohpmgq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdsdnFkbHpzdmRtdnBsb2hwbWdxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDExNjAxNTYsImV4cCI6MjA1NjczNjE1Nn0.UauGe2SIarphoWwwAHweqDdV13wkK1k1lSgfFSjW0lc"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/profile', methods=['GET'])
def get_profile():
    # Get profile data from a Supabase table named 'profile'
    response = supabase.table("profile").select("*").execute()
    # Return the data as JSON
    return jsonify(response.data)

@app.route('/profile', methods=['POST'])
def update_profile():
    data = request.get_json()
    # Here we assume data is a dict with keys such as "name" and "bio"
    # This example inserts a new profile entry. You might want to adjust it for updates.
    response = supabase.table("profile").insert(data).execute()
    return jsonify(response.data)

if __name__ == '__main__':
    app.run(debug=True)
