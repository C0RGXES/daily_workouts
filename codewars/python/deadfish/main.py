
import string


def parce_data_Deadfish(data: string):
    
    result_arr = []
    num = 0

    for simbol in data:
        if simbol == 'i':
            num += 1
        elif simbol == 'd':
            num -= 1
        elif simbol == 's':
            num *= num
        elif simbol == 'o':
            result_arr.append(num)

    return result_arr



def main():
    data = 'iodisoiodsfiosdfiisoio'
    result = parce_data_Deadfish(data)
    print('My dead fish => ', result)

if __name__ == '__main__':
    main()