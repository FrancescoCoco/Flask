from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

#Decorator 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Return json file
@app.route("/health")
def health():
    return jsonify(
        status= 'UP'
    )

# Render template 
@app.route("/news")
def last_news():
    hostname, ip = fetchDetails()
    # Render template send automatically to the folder of the templates
    return render_template('index.html',hostname=hostname, ip_address = ip)

# function to fetch details 
def fetchDetails():
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    return str(hostname), str(ip_address)

