from flask import Flask, render_template
from flask import request
from flask_socketio import SocketIO, emit

temperature_value = 0
app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
 
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    global temperature_value
    content = request.get_json()
    print (content, flush = True)
    temperature_value = content['temperature']
    socketio.emit('temperature', {'data': temperature_value})
    return 'JSON posted'

@socketio.on('my event')
def test_message(message):
    global temperature_value
    print ("Send", flush = True)
    emit('temperature', {'data': message[temperature_value]})
    
#@socketio.on('my_event', namespace='/')                                                                   
#def test_message(message):                                                                                    
#    session['receive_count'] = session.get('receive_count', 0) + 1                                            
#    emit('my_response',                                                                                       
#         {'data': message['data'], 'count': session['receive_count']})  

@app.route('/')
@app.route('/index')
def index():
    global temperature_value
    #temp = {'temperature': temperature_value}  
    return render_template('index.html', 
                           async_mode=socketio.async_mode)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)
 #   app.run(host='0.0.0.0')