import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cloud Environment Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 40px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto; }
        h1 { color: #2c3e50; font-size: 24px; }
        .status { padding: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>☁️ Cloud Environment Manager</h1>
        <p>Elastic Beanstalk PaaS Deployment</p>
        <div class="status">
            <strong>System Status:</strong> Operational<br>
            <strong>Environment:</strong> Production<br>
            <strong>Automation Engine:</strong> Active via AWS EventBridge & Lambda
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)