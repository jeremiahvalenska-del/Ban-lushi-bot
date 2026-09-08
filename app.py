from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return "<h1>BAN LUSHI BOT LIVE - LUBUMBASHI CDT</h1><p>Site marche! On ajoute traducteur apres.</p>"
if __name__ == "__main__": app.run(host="0.0.0.0", port=10000)
