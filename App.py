from flask import Flask, render_template
from flask_socketio import SocketIO, send
from dotenv import load_dotenv
import os
load_dotenv()

##Aqui se crea la aplicacion
app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

socketio = SocketIO(app) #Delegando en socket io todas las conexiones

@app.route('/')

def index():
    return render_template('index.html')

@socketio.on('message')#Aqui haremos que cuando el mensage se recciba el socket lo procese
def handleMessage(msg):
    print("Message: ",msg)
    send(msg,broadcast = True)
    
if __name__ == "__main__":
    socketio.run(app, port=5000, debug=True) ## El debug hace que el servidor refresque los cambios para que se mantenga actualizado





