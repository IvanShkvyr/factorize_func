"""Напишіть реалізацію функції factorize, яка приймає список чисел та повертає список чисел, на які
 числа із вхідного списку діляться без залишку.
Реалізуйте синхронну версію та виміряйте час виконання.
Потім покращіть продуктивність вашої функції, реалізувавши використання кількох ядер процесора 
для паралельних обчислень, і виміряйте час виконання знову.
Для перевірки правильності роботи алгоритму самої функції можете скористатися тестом:"""


from multiprocessing import Pool, cpu_count
from time import sleep, time



def logged_func(func):
    def inner(number):

        start_time = time()
        print(f'Start of calculations')

        result = func(number)
        
        end_time = time()
        print(f'End of calculations')
        print(f'The calculation lasted {end_time-start_time} seconds')
        return result
    return inner


def factorize_num(divident: int):
    divisor = 1 
    divisors = []

    while divisor != (divident + 1):
        if divident % divisor == 0:
            divisors.append(divisor)
        divisor += 1

    if len(divisors) == 0:
        raise NotImplementedError()

    return divisors


def factorize(number):

    if isinstance(number, list):
        return [factorize_num(divident) for divident in number]
    elif isinstance(number, int):
        factorize_num(number)


if __name__ == '__main__':
    print('Simple example')
    args_num = [128, 255, 99999, 10651060]

    start_time = time()
    print(f'Start of calculations')

    a, b, c, d  = factorize(args_num)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    end_time = time()
    print(f'End of calculations')
    print(f'The calculation lasted {end_time-start_time} seconds')


    print('\n\nAn example of using processes')

    cpu = cpu_count()
    

    start_time2 = time()
    print(f'Start of calculations')


    with Pool(processes=cpu) as pool:
        pool.map(factorize, args_num)

    end_time2 = time()
    print(f'End of calculations')
    print(f'The calculation lasted {end_time2-start_time2} seconds')


    print('\n\nAn example of using processes')
       
    start_time3 = time()
    print(f'Start of calculations')

    pool =  Pool(processes=4)
    pool.map(factorize, [128, 255, 99999, 10651060])
    pool.close()
    pool.join()

    end_time3 = time()
    print(f'End of calculations')
    print(f'The calculation lasted {end_time3-start_time3} seconds')






