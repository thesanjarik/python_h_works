
country = {
    # key : values
    'kg': {'red', 'yellow'},
    'ru': {'red', 'blue'},
    'ua': {'red'},
    'tr': {'red'}
}

while True:
    p = input("\nEnter the color: \n").lower()

    if p == 'q':
        print('programm stopped!!!')
        break
    elif country.values() != p:
        print()

    for key, value in country.items():
        if set(p.split()).issubset(value):
            print(key)



















