def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person


name = build_person('laiba', 'noor', 20)
print(name)
name = build_person('huda', 'huda')
print(name)