def creates_profile(name, age, country, job):
    return(
        f"======== Profile ========\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Country: {country}\n"
        f"Future Job: {job}\n"
        f"========================="
    )

name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")
job = input("Enter your future job: ")

profile = creates_profile(name, age, country, job)
print(profile)