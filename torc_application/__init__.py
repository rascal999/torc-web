import os
import sys

sys.path.append(os.path.dirname(__name__))

from torc_application.torc_web import create_app

# create an app instance
app = create_app()

if os.path.isfile('/.dockerinit'):
    print("Running in docker")
    #app.run(host='0.0.0.0',debug=True,threaded=True,ssl_context=context)
    app.run(host='0.0.0.0',debug=True,threaded=True,port=8080)
else:
    #app.run(debug=True,threaded=True,ssl_context=context)
    app.run(debug=True,threaded=True,port=8080)
