#Goal:
#To reinforce the ability to extract data from a dictionary and construct nested conditional statements.

def user_age_and_status(age:int, active:bool):
    user = {'age': age, 'active' : active}
    if user["age"] >= 18 and user['active'] == True:
        print('Пользователь взрослый, но активный')
    elif user["age"] >= 18 and user['active'] == False:
        print('Пользователь взрослый и неактивный')
    elif user["age"] < 18 and user['active'] == True:
        print('Пользователь несовершеннолетний, но активный')
    elif user["age"] < 18 and user['active'] == False:
        print('Пользователь несовершеннолетний, но неактивный')

user_age_and_status(15, False)


#Goal:
# Learn to use the in / not in operator with dictionaries.
#Understand the difference between checking for a key and checking for a value.
#Practice using a simple if ... else structure without elif.
def checking_name_role_email(input_user):
    users = [{'name': "Ivan", "role": "QA", "email": "123@qa.ru"},
            {"name": "Kate", "role": "Dev", "email": "1234@qa.ru"},
            {"name": "Anna", "role": "PM", "email": "12345@qa.ru"}]

    if "name" not in input_user:
        print("⚠️Вы не ввели имя")
    if "role" not in input_user:
        print("⚠️Вы не ввели роль")
    if "email" not in input_user:
        print("⚠️Вы не ввели email")
    elif input_user["email"] == "" or input_user["email"] is None:
        print("⚠️Email пуст — укажите адрес")
    else:
        print("✅Email указан.")

    for user in users:
        if user["name"] == input_user["name"] and \
           user["role"] == input_user["role"] and \
           user["email"] == input_user["email"]:
            print("Данные корректны. Такой пользователь существует.")
            return

    print("⚠️Данные некорректны. Пользователь не найден.")

checking_name_role_email({"name": "Ivan", "role": "QA", "email": "1234@qa.ru"})
