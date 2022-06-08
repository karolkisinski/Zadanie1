from flask import Blueprint, render_template
import requests
import pytz
from datetime import datetime
import json

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    API_KEY ='25927a6212054e13b7e65841003e25a8'
    request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + API_KEY
    response = requests.get(request_url)
    result = json.loads(response.content)
    ip = result['ip_address'] # wyciagniecie ip klienta z odpowiedzi API
    location = result['timezone']['name'] # wyciagniecie nazwy strefy czasowej z odpowiedzi API
    time = datetime.now(pytz.timezone(location)) # otrzymujemy czas na podstawie nazwy strefy czasowej
    return render_template("index.html", ip=ip, location=location, time=time)

@views.route('/logs')
def log():
    with open("logfile.log", "r") as f:
        log = []
        f = f.readlines()
        for line in f:
            log.append(line)
    return render_template('log.html', content=log, mimetypes='text/plain')
