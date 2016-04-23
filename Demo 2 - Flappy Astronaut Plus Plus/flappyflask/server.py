from flask import Flask, request, render_template 
from sense_hat import SenseHat
from threading import Thread
import astroflap

host_name = "<place your flappy server here>"

sense = SenseHat()

app = Flask(__name__, static_url_path='')
    
@app.route("/")
def hello():
    return "Main Page. Intended to be blank."

@app.route("/flappycmd")
def flappycontrol():
    if ('cmd' in request.args) and (request.args['cmd'] == 'flapup'):
        astroflap.flapup()
    elif ('cmd' in request.args) and (request.args['cmd'] == 'flapdown'):
        astroflap.flapdown()  
    elif ('cmd' in request.args) and (request.args['cmd'] == 'stopgame'):
        astroflap.stopgame()  
    elif ('cmd' in request.args) and (request.args['cmd'] == 'startgame'):
        astroflap.startgame()  
    return "Command Sent."
    
@app.route('/flappycontrol')
def index():
    return render_template('flappycontrol.html')
 
    
if __name__ == "__main__":
    app.run(host=host_name,port=5000, debug=True)
