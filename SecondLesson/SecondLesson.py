import math

#multiplication and sum

first_number = input("Привет, введи первое целое число:")
second_number = input("Dведи второе целое число:")
mul_number = int(first_number) * int(second_number)
sum_numbers = int(first_number) + int(second_number)

if mul_number > 1000:
    print(sum_numbers)
else:
    print(mul_number)


#convert km to miles

kilometres = input("Привет, напиши расстояние в километрах:")
mil = float(kilometres) * 0.62137
print(mil)


#calculate squire of circle
def calculate_squire_circle(p_circle: int):
    square_circle = math.pi * pow(int(p_circle),2)
    return square_circle
result = calculate_squire_circle(7)
print(result)

#testing statistics and report
def pass_rate(total_tests:int, passed_tests, bugs_found:int):
    pass_rate = ((passed_tests/total_tests) * 100)
    round_by_two = round(pass_rate,2)
    report = (
        f"Всего тестов: {total_tests}\n"
        f"Пройдено успешно: {passed_tests} ({round_by_two}%)\n"
        f"Найдено багов: {bugs_found}"
    )
    return report

result = pass_rate(50,47,3)
print(result)