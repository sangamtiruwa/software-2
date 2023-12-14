import json
import math

from flask import Flask,Response

def primality_test(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    return True

app= Flask(__name__)


@app.route('/prime_number/<numberstring>')
def prime(numberstring):
    try:
        number = int(numberstring)
        response = {
            "Number": number,
            "isPrime": primality_test(number)
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=404, mimetype="application/json")
        return http_response

@app.route('/prime_number')
def error_stub():
    try:
        number = 666
        response = {
            "Message": "Prime beast!",
            "Number": number,
            "isPrime": primality_test(number)
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=404, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response={
        "message":"Invalid endpoint",
        "status":404
    }
    json_response=json.dumps(response)
    http_response=Response(response=json_response,status=404,mimetype="application/json")
    return http_response



if __name__ == '__main__':
     app.run(use_reloader=True, host='127.0.0.1', port=5000)