import requests

response = requests.get("https://jsonplaceholder.typicode.com/does-not-exist")

try:
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("The API request failed!")

data = response.json()

def display_person(person):
    for item in person:
        for key,value in item.items():
            title = key.capitalize()
            if key == 'name':
                print(f'{title}: {value}')
            elif key == 'email':
                print(f'{title}: {value}\n')           

display_person(data)