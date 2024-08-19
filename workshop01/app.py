# Import flask and datetime module for showing date and time
from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import random


# Initializing flask app
app = Flask(__name__, static_folder='workshop01/frontend/webapp/build', static_url_path='')
cors = CORS(app)
# Route for seeing a data
@app.route('/line')
@cross_origin()
def get_line():
    list = [
        "Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it so simple"
        " that there are obviously no deficiencies and the other is to make it so complicated "
        "that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."
    ]

    return {"sentence":random.choice(list)}

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')
# Running app
if __name__ == '__main__':
    app.run()