import requests

request_url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request_url)

    if response.status_code == 200:
        answer = response.json()
        print("Chuck Norris Joke:")
        print(answer["value"])
    else:
        print(f"There was an error with the server. Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request could not be completed: {e}")
