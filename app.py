from flask import Flask
import json
import os
from settings import *
import ansible_runner

app = Flask(__name__)

DATA = "ansible_data"
ANSIBLE_FILE = os.path.join(os.getcwd(), "playbook.yml")

@app.route("/test")
def test():

    res = {
        'status': 'Ok',
        'code': 200,
        'message':'success'
    }

    r = ansible_runner.run(private_data_dir=os.path.join(os.getcwd(), DATA), playbook=ANSIBLE_FILE)
    print("{}: {}".format(r.status, r.rc))
    print("Final status:")
    print(r.stats)

    return res


# end point to create a new request
@app.route("/create", methods=['GET', 'POST'])
def create():
    res = {
        'status': 'Ok',
        'code': 200,
        'message':'success'
    }

    return res


# endpoint to update the request
@app.route("/update", methods=['GET', 'POST'])
def update():
    res = {
        'status': 'Ok',
        'code': 200,
        'message':'success'
    }

    return res


# main method to run the app
def run():
    # start server at given host and port
    app.run(SERVER_HOST, SERVER_PORT)


# start the server
if __name__ == '__main__':
    run()
