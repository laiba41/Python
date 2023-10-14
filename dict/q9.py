fav_languages = {'laiba': ['python', 'ruby'], 'noor': ['c'], 'fiza': ['ruby', 'go'], 'ali': ['python', 'haskell']}
# Show all responses for each person.
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)