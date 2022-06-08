from flask import Flask
from views import views
import logging
from datetime import datetime

#Konfiguracja loggera

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    encoding='utf-8',
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

#Konfiguracja Flaska

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

PORT = 5000

logger.info(str(datetime.today()) + " Karol Kisinski - nasluchiwanie na porcie " + str(PORT)) #informacja do logow o starcie

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
