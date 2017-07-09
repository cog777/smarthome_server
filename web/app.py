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
    print ("postjson", flush = True)
    print (content, flush = True)
    temperature_value = content['temperature']
    socketio.emit('temperature', {'data': temperature_value})
    return 'JSON posted'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           async_mode=socketio.async_mode)

@app.route('/odense')
def odense_temperature():
    global temperature_value
    return render_template('/odense/temperature.html',
                           async_mode=socketio.async_mode)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)
