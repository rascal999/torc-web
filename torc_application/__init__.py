import os
import sys

sys.path.append(os.path.dirname(__name__))

from torc_application.torc_web import create_app

# create an app instance
app = create_app()

# Don't fetch from the CDN..
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

if os.path.isfile('/.dockerenv'):
    print("Running in docker")
    #app.run(host='0.0.0.0',debug=True,threaded=True,ssl_context=context)
    app.run(host='0.0.0.0',debug=True,threaded=True,port=8080)
else:
    #app.run(debug=True,threaded=True,ssl_context=context)
    app.run(debug=True,threaded=True,port=8080)
