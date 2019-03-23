from flask import Flask
from flask_ask import Ask, statement, question, session
app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def entry():
    welcome_msg = "Welcome, This is aws doctor. Version 1.o. Which AWS account that you want to control?"
    return question(welcome_msg)

@ask.intent('GetEnvironmentIntent')
def get_environment(environment=None):
    environment, taking_or_assuming = ('Dev', 'Assuming') if environment is None else (environment, 'Taking')
    message = '{0} {1} environment, which service you want to control?'.format(taking_or_assuming, environment)
    return question(message)

@ask.intent('GetServiceIntent')
def get_service(service=None):
    message = 'confirmed {} service, what do you want to do?'.format(service)
    return question(message)

@ask.intent('ECStartIntent')
def start_ec2_service():
    message = 'started ec2 service'
    return statement(message)

@ask.intent('ECStopIntent')
def stop_ec2_service():
    message = 'stopped ec2 service'
    return statement(message)

@app.route('/')
def health():
    return 'Ok'

if __name__ == '__main__':
    app.run()