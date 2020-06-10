# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    if (req.get('queryResult').get('action') == 'ug'):
         return {'fulfillmentText': 'I did my under graduate studies in SSN college of Engineering}
    elif (req.get('queryResult').get('action') == 'ug_follow'):
         return {'fulfillmentText': 'My cumulative score is 7.2 from my university exams.'}
    
         

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
    app.run()
