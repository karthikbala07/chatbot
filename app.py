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
         return {'fulfillmentText': 'I did my under graduate studies in SSN college of Engineering'}
    elif (req.get('queryResult').get('action') == 'ug_grade'):
         return {'fulfillmentText': 'My Bachelors cumulative score is 7.2 out of 10 from university exams.'}
    elif (req.get('queryResult').get('action') == 'ug_name'):
         return {'fulfillmentText': 'My course was  B.E in electrical engineering .'}
    elif (req.get('queryResult').get('action') == 'school'):
         return {'fulfillmentText': 'I did my high schooling in MLM Mamallan Mat Hr.sec school'}
    elif (req.get('queryResult').get('action') == 'school_grade'):
         return {'fulfillmentText': 'My high school grade is 9.4 out of 10 from the final exams.'}
    elif (req.get('queryResult').get('action') == 'pg'):
         return {'fulfillmentText': 'I did my graduate studies in State University of New York,Buffalo '}
    elif (req.get('queryResult').get('action') == 'pg_grade'):
         return {'fulfillmentText': 'My Masters cumulative score is 3.8 out of 4 from the final exams'}
    elif (req.get('queryResult').get('action') == 'pg_name'):
         return {'fulfillmentText': 'My course was  M.S in electrical engineering with a focus in Semiconductors .'}
         

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
    app.run()
