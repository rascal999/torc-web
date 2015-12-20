import os
import sys

sys.path.append(os.path.dirname(__name__))

from torc_application.torc_web import create_app

# create an app instance
app = create_app()

app.run(debug=True, port=8080)
