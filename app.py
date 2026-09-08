from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Ban Lushi Bot</title>
    <style>body{background:#000;color:#fff;font-family:Arial;padding:20px;text-align:center}
    h1{color:#00ff88} .box{background:#111;padding:20px;border-radius:15px;border:1px solid #00ff88}
    textarea,select,button{width:100%;padding:15px;margin:10px 0;border-radius:10px;font-size:16px}
    textarea{background:#000;color:#fff;border:1px solid #333} select{background:#222;color:#fff}
    button{background:#00ff88;color:#000;font-weight:bold;border:none} #res{background:#000;padding:15px;border:1px solid #00ff88;border-radius:10px;min-height:40px}</style>
    </head><body><h1>🌍 BAN LUSHI BOT<br>LUBUMBASHI 24h/24</h1>
    <div class='box'><textarea id='t' placeholder='Tape texte ici...'></textarea>
    <select id='f'><option value='fr'>Francais</option><option value='en'>English</option><option value='es'>Espanol</option></select>
    <select id='to'><option value='en'>English</option><option value='fr'>Francais</option><option value='es'>Espanol</option></select>
    <button onclick='tr()'>TRADUIRE</button><div id='res'>Resultat...</div></div>
    <script>async function tr(){let txt=document.getElementById('t').value;let f=document.getElementById('f').value;let to=document.getElementById('to').value;
    if(!txt){document.getElementById('res').innerText='Tape texte!';return;} document.getElementById('res').innerText='...';
    let r=await fetch('https://api.mymemory.translated.net/get?q='+encodeURIComponent(txt)+'&langpair='+f+'|'+to);let d=await r.json();
    document.getElementById('res').innerText=d.responseData.translatedText;}</script></body></html>
    """

@app.route('/health')
def health():
    return "OK LIVE"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
