import json

person = {
    'name':'Sergiu',
    'age': 29,
    'country' : 'Moldova',
    'languages' : ['romanian','english','italian','russian','german'],
    'family' : {
        'mother' : 'Rodica',
        'father' : 'Olimpiu',
        'brother' : 'Leo',
        },
}

with open('json_person.json','w') as file:
    json.dump(person, file, indent = 4 )

with open('json_person.json','r') as file:
    python_person = json.load(file)
   

for key,value in python_person.items():
    if isinstance(value, list):
        print(f'{key.capitalize()}:')
        for lang in value:
            print(f"\n- {lang}")
    elif isinstance(value, dict):
        print(f'\n{key.capitalize()}:')
        for nested_key, nested_value in value.items():
            print(f'- {nested_key}: {nested_value}')
    else:    
        print(f'{key.capitalize()}: {value}')