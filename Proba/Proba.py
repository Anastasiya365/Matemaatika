import random

def generate_expression(operation, difficulty):
    if difficulty == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 2:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    else:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '**':
        result = num1 ** num2

    return f"{num1} {operation} {num2}", result

def main():
    total_questions = int(input("Введите количество примеров: "))
    difficulty = int(input("Выберите сложность (1, 2 или 3): "))
    operation = input("Выберите операцию (+, -, *, /, **): ")

    correct_answers = 0

    for _ in range(total_questions):
        expression, correct_result = generate_expression(operation, difficulty)

        user_answer = float(input(f"Сколько будет {expression}? "))

        if user_answer == correct_result:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный ответ: {correct_result}")

    score = (correct_answers / total_questions) * 100

    if score < 60:
        print("Оценка: Hinne 2")
    elif 60 <= score < 75:
        print("Оценка: Hinne 3")
    elif 75 <= score < 90:
        print("Оценка: Hinne 4")
    else:
        print("Оценка: Hinne 5")

if __name__ == "__main__":
    main()

