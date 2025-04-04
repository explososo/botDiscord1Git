#Flask crée un petit site web juste pour que ton hébergeur pense que le projet est actif, et ne le mette pas en veille.

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return 'le bot est en ligne'

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run) #lance le serveur dans un thread séparé, en parallèle de mon code pour le bot
    t.start()