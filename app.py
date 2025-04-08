from flask import Flask
import os
import time
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Bibek Kumar Shah"
    username = os.getenv("USER") or os.getenv("USERNAME")
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True).decode()
    except Exception as e:
        top_output = str(e)

    html = f"""
    <h2>Name: {name}</h2>
    <h3>User: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>TOP Output:\n{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
