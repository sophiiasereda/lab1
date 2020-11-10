import sys
import re

def open_file():
    try:
        return open("lab1_sereda.txt")
    except FileNotFoundError:
        print("Файл не знайдено...")
        exit()



def maximum_model(matrix):
    minRow = []
    for row in matrix:
        minRow.append(min(row))

    maxValue = max(minRow)
    print("Найменші елементи для кожного рядка:", minRow)
    print("Найбільший з найменших елементів:", maxValue)
    return minRow.index(maxValue)


def laplace(matrix):
    sumRows = []
    for row in matrix:
        sumRows.append(sum(row) / len(row))

    maxValue = max(sumRows)
    print("Сумовування розділених значень для кожного рядка:", sumRows)
    print("Найбільший елемент:", maxValue)
    return sumRows.index(maxValue)


def hurwitz(matrix, coefficient):
    minRows = []
    maxRows = []

    for row in matrix:
        minRows.append(min(row))
        maxRows.append(max(row))

    result = []
    for i in range(len(minRows)):
        result.append(coefficient * minRows[i] + (1 - coefficient) * maxRows[i])

    print("Коефіцієнт:", coefficient)
    print("Найменші елементи для кожного рядка:", minRows)
    print("Найбільші елементи для кожного рядка:", maxRows)
    print("Пораховані значення:", result)
    return result.index(max(result))


def bayes_laplace(matrix, coefficients):
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
indexByWald = maximum_model(lines)
print("Найкраще рішення:", lines[indexByWald])

print("\nКритерій Лапласа:")
indexByLaplace = laplace(lines)
print("Найкраще рішення:", lines[indexByLaplace])

print("\nКритерій Гурвіца:")
indexByHurwitz = hurwitz(lines, 0.2)
print("Найкраще рішення:", lines[indexByHurwitz])

print("\nКритерій Байеса-Лапласа:")
indexByBayesLaplace = bayes_laplace(lines, [0.25, 0.30, 0.45])
print("Найкраще рішення:", lines[indexByBayesLaplace])
