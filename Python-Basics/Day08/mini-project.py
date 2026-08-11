import requests

def get_users():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users",
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

def search_users(users, search_query):
    for user in users:
        if search_query.lower() in user["name"].lower():
            print(f"\nName: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Phone: {user['phone']}")
            print(f"Company: {user['company']['name']}")
            return True

    print(f"\nUser {search_query} not found!")
    return False

        
def print_menu():
    print("\n1. Search user")
    print("2. Display all users")
    print("3. Exit")

    selection = input("\nChoose an option: ")
    return selection

print("=======================")
print("     User Directory    ")
print("=======================")

users = get_users()

print(f"\nRetrieved {len(users)} users.")


while True:
    selection = print_menu()

    if selection == "1":

        while True:
            search_query = input("\nSearch for: ")

            found = search_users(users, search_query)

            if found:
                break

            another_search = input(
                "\nWould you like to search again? (y/n): "
            )

            if another_search.lower() != "y":
                break
      
    elif selection == '2':
        display_users(users)

    elif selection == '3':
        print("\nGoodbye!")
        break

    else:
        print("\nOption not available. Try again!")
        