age = int(input("What is your age? "))

if age > 18:
    print("You are an adult.")
    experience = int(input("Years of experience in Python: "))
    if experience == 0:
        print("You are a beginner in Python.")
    elif experience < 2:
        print("You are a Junior developer.")
    elif experience < 5:
        print("You are a Mid-level developer.")
    else:
        print("You are a Senior developer.")
else:
    print("You are a minor.")

