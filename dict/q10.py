Laiba = []



for laiba_num in range(100):
    new_laiba = {}
    new_laiba['color'] = 'green'
    new_laiba['points'] = 5
    new_laiba['x'] = 20 * laiba_num
    new_laiba['y'] = 7 * int(new_laiba['x'])
    Laiba.append(new_laiba)


# Prove the list contains a million aliens.
num_laiba = len(Laiba)
print("Number of aliens created:")
print(num_laiba)
print(Laiba)