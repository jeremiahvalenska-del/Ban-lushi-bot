import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='text-align:center;background:black;color:lime;padding:50px'>🔥 CDT ETERNEL 24h/24 🔥<br><br>BAN LUSHI BOT ONLINE<br><br>✅ PUBLIC</h1>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
