
ten = [1, 2, 4, 6, 7, 8, 10]

evens = list(filter(lambda x: x, ten))
our_dict = ten
our_dict = list(map(lambda x: x, ten))

while True:
    indx = input('Enter an index! ')
    if indx == 'q':
        print('programm completed!')
    try:
        print(ten[int(indx)])
    except:
        print(f" Only numbers! or index from 0 to {len(ten) - 1}")



























