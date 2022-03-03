us = "`qwertyuiop[]asdfghjkl;'zxcvbnm,.1234567890!@#$%^&*()_+ "
ru = 'ёйцукенгшщзхъфывапролджэячсмитьбю1234567890!"№;%:?*()_+ '

while True:
    word = input("\nвведите слово: (для выхода нажмите 'q')\n").lower()

    if word == 'q':
        print('программа завершена!!!')
        break

    for i in word:
        if i in us:
            index1 = us.index(i)
            r = ru[index1]
            print(r, end='')
        else:
            index2 = ru.index(i)
            u = us[index2]
            print(u, end='')