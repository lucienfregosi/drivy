import sys
import os
import json
import redis
from flask import Flask, escape, request
sys.path.append('../level_1')
import lib as l


app = Flask(__name__)

@app.route('/', methods = ['POST'])
def main():
    r = redis.Redis(host='localhost', port=6379, db=0)

    current_path = os.path.abspath(os.path.dirname(__file__))
    log_folder_path_output = "../parsed"
    path_directory_output = current_path + "/" + log_folder_path_output
    # Create folder if not exist
    if not os.path.exists(path_directory_output):
        os.makedirs(path_directory_output)

    log = request.get_json()['log']
    logCleaned = l.convertStringToDict(log)

    # Write logs in redis
    key = logCleaned['id']
    del logCleaned['id']

    r.set(key, json.dumps(logCleaned))
    return 'OK'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)