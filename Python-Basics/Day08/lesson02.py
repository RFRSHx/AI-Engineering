import requests

def get_users():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/does-not-exist",
            timeout=5
        )

        response.raise_for_status()

        return response.json()
    
    except requests.exceptions.RequestException as error:
        print(f"The API request failed: {error}")
        return []

def display_users(users):
    for user in users:
        print(f"\nName: {user['name']}")
        print(f"Email: {user['email']}")
        print("-----------------------")

users = get_users()

print(f"Retrieved {len(users)} users.")

display_users(users)