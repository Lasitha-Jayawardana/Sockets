# Basic blask server to catch events
from flask import Flask, render_template,request
import time
from flask_socketio import SocketIO, emit



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app,cors_allowed_origins='*')#, message_queue='redis://', async_mode='eventlet'
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')                     
def connecting():                       # Trigger when connect
    emit('my response', {'data': 'Connected','number': 2589})       
    print(request.sid )
    print("connected.....................")
                                             
@socketio.on('eventtest')                      # Decorator to catch an event called "eventtest":
def eventtest(message):                        # eventtest() is the event callback function.
    emit('Server response', {'data': 'got it!'})        # Trigger a new event called "my response" in client side 
    #print(message)
    print("eventtest trigged.....................")                                            

@socketio.on('event_name')                      # Decorator to catch an event called "event_name":
def event_name(message):                        # event_name() is the event callback function.
    emit('my response', {'data': 'got it!','number': 2589},broadcast=True)         # Trigger a new event called "my response" in all client
    print("event_name trigged .....................")
                                                  

if __name__ == '__main__':
    socketio.run(app, host='192.168.137.240',port=8089)

