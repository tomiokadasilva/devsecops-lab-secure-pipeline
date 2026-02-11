# app/app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ⚠️ Hardcoded secret
API_SECRET = "devsecops_lab_2026_supersecret_key"

@app.route("/")
def home():
    name = request.args.get("name", "Guest")
    # ⚠️ XSS refletido
    return render_template_string(f"<h1>Hello, {name}!</h1><p>Try ?name=<script>alert('xss')</script></p>")

@app.route("/user")
def user():
    user_id = request.args.get("id", "1")
    # ⚠️ SQL Injection (simulada com string format — NÃO use em produção!)
    query = f"SELECT * FROM users WHERE id = {user_id};"
    return f"<pre>Executed query: {query}</pre>"

@app.route("/health")
def health():
    return {"status": "ok", "secret_present": bool(API_SECRET)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)