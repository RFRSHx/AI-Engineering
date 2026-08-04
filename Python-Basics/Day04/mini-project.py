languages = []

lang_num = int(input("How many programming languages do you know? "))

for i in range(lang_num):
    lang = input(f"Enter programming language {i + 1}: ")
    languages.append(lang)

def display_languages(languages):
    print("\n======================")
    print('Programming Languages')
    print("======================")

    for index,language in enumerate(languages, start=1):
        print(f"\n{index}. {language}")

    print("\nTotal languages known:", len(languages))

display_languages(languages)

add_more = input("\nDo you want to add more languages? (y/n): ").lower()

while add_more == "y":
    lang = input("Enter a programming language: ")
    languages.append(lang)
    add_more = input("Do you want to add more languages? (y/n): ").lower()

display_languages(languages)

search_lang = input("\nDo you want to search for a Language? (y/n): ").lower()

if search_lang == "y":
    search_query = input("\nEnter the programming language to search for: ")
    if search_query.lower() in [lang.lower() for lang in languages]:
        print(f"\n{search_query} is in your list of known languages.")
    else:
        print(f"{search_query} is not in your list of known languages.")