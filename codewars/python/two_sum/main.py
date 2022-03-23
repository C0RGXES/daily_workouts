
def main():
    number_list = [2, 2, 3]
    target_value = 4
    
    result = two_sum(number_list, target_value)
    print(result)

def two_sum(numbers, target):
    
    sum = []
    hashtable = {}

    for num in numbers:

        target_minus_num = target - num

        if target_minus_num in hashtable:
            return (numbers.index(num), numbers.index(target_minus_num))

        hashtable[num] = num

if __name__ == "__main__":
    main()
