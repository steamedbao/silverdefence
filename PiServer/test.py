from flask import Flask 
from flask_sockets import Sockets


app = Flask(__name__) 
sockets = Sockets(app)


@sockets.route('/accelerometer')
def echo_socket(ws):
	f=open("accelerometer.txt","a")
	while True:
		message = ws.receive()
        # print(message)
		x,y,z = message.split(",")
		rss = (float(x)*float(x) + float(y)*float(y) + float(z)*float(z))**0.5
		# if rss > 
		print(rss)
        # ws.send(message)
        # print(message, file=f)
	f.close()

@sockets.route('/gyroscope')
def echo_socket(ws):
	f=open("gyroscope.txt","a")
	while True:
		message = ws.receive()
		# print(message)
		x,y,z = message.split(",")
		rss = (float(x)*float(x) + float(y)*float(y) + float(z)*float(z))**0.5
		# if rss > 
		print(rss)
		# ws.send(message)
		# print(message, file=f)
	f.close()
	

@app.route('/') 
def hello(): 
	return 'Hello World!'

if __name__ == "__main__":
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()
