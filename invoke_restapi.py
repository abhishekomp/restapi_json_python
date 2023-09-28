import requests
import json

def getPosts():
  url = 'https://jsonplaceholder.typicode.com/posts'
  response = requests.get(url)
  # Convert the response to a python object (dictionary/list)
  response_json = json.loads(response.text)
  #Below command does the same work in converting the response to python object (dictionary/list)
  #response_json = response.json()
  #posts = json.loads(response.text)
  print(type(response_json))  #In ths case <class 'list'> since the response is returned as an array
  print(response_json)
  #return response_json

if __name__ == "__main__":
  getPosts()
