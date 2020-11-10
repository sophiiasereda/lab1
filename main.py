import sys
import re

def open_file():
    try:
        return open("lab1_sereda.txt")
    except FileNotFoundError:
        print("Файл не знайдено...")
        exit()



def walds_maximin_model(matrix):
    minOfRows = []
    for row in matrix:
        minOfRows.append(min(row))

    maxValue = max(minOfRows)
    print("Найменші елементи для кожного рядка:", minOfRows)
    print("Найбільший з найменших елементів:", maxValue)
    return minOfRows.index(maxValue)


def laplace_criterion(matrix):
    sumOfRows = []
    for row in matrix:
        sumOfRows.append(sum(row) / len(row))

    maxValue = max(sumOfRows)
    print("Сумовування розділених значень для кожного рядка:", sumOfRows)
    print("Найбільший елемент:", maxValue)
    return sumOfRows.index(maxValue)


def hurwitz_criterion(matrix, coefficient):
    minOfRows = []
    maxOfRows = []

    for row in matrix:
        minOfRows.append(min(row))
        maxOfRows.append(max(row))

    result = []
    for i in range(len(minOfRows)):
        result.append(coefficient * minOfRows[i] + (1 - coefficient) * maxOfRows[i])

    print("Коефіцієнт:", coefficient)
    print("Найменші елементи для кожного рядка:", minOfRows)
    print("Найбільші елементи для кожного рядка:", maxOfRows)
    print("Пораховані значення:", result)
    return result.index(max(result))


def bayes_laplace_criterion(matrix, coefficients):
    result = [0 for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i] += coefficients[j] * matrix[i][j];

    print("Коефіцієнти:", coefficients)
    print("Пораховані значення:", result)
    return result.index(max(result))


file = open_file()
lines = []

for line in file:
    if (not (line and not line.isspace())): continue

    row = re.split(',\s?', re.sub('\n', '', line))

    lines.append([int(element) for element in row])

print("Матриця:", lines)

print("\nМаксимальний критерій Вальда:")
indexByWald = walds_maximin_model(lines)
print("Найкраще рішення:", lines[indexByWald])

print("\nКритерій Лапласа:")
indexByLaplace = laplace_criterion(lines)
print("Найкраще рішення:", lines[indexByLaplace])

print("\nКритерій Гурвіца:")
indexByHurwitz = hurwitz_criterion(lines, 0.2)
print("Найкраще рішення:", lines[indexByHurwitz])

print("\nКритерій Байеса-Лапласа:")
indexByBayesLaplace = bayes_laplace_criterion(lines, [0.25, 0.30, 0.45])
print("Найкраще рішення:", lines[indexByBayesLaplace])
