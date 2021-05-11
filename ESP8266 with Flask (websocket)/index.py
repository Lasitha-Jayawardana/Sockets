from flask import Flask, Blueprint
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

html = Blueprint(r'html', __name__)
ws = Blueprint(r'ws', __name__)


@html.route('/') #websites
def hello():
    return 'Hello World page' 

@ws.route('/sock_end')
def echo_socket(socket):
    print("client conected")
    while not socket.closed:
        message = socket.receive()
        socket.send("server msg")
        print("Data recieved")
        print(message)
        


app = Flask(__name__)
sockets = Sockets(app)

app.register_blueprint(html, url_prefix=r'/')
sockets.register_blueprint(ws, url_prefix=r'/')


if __name__ == "__main__":
    
    server = pywsgi.WSGIServer(('192.168.137.240', 8089), app, handler_class=WebSocketHandler)
    server.serve_forever()