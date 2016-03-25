# coding=UTF-8


import scipy.stats


def stat(sample, n):
    for i in xrange(n):
        moment = [0 for _ in xrange(2 ** (i + 1))]
        for j in xrange(len(sample) - i):
            index = int(''.join(map(str, sample[j:(j + i + 1)])), 2)
            moment[index] += 1

        # Напечатать распределения (чтобы работало, в следующей строке удалить '#')
        # print moment

        # Напечатать p-значения
        print scipy.stats.chisquare(moment)[1]


def main():
    file = open('sample.txt', 'r')
    lines = file.readlines()
    file.close()
    sample = map(int, lines[0][:-1])

    # Второй аргумент --- максимальный размер (т.е. n) подсчитываемых n-грамм
    stat(sample, 10)


if __name__ == '__main__':
    main()
