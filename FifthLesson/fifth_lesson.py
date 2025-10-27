#Goal:
#Learn to work with nested dictionaries, the in / not in operators, and the logical expressions and / or / not.
#Practice applying a combination of several checks: role-based access, activity status, and absence from the “blacklist.”


def checking_blacklist(name):
    users = {
        "alice": {"role": "admin", "active": True},
        "bob": {"role": "qa_lead", "active": False},
        "carol": {"role": "tester", "active": True},
        "dave": {"role": "admin", "active": True},
        "caro": {"role": "pm", "active": True},
    }
    allowed_roles = ["admin", "qa_lead"]
    banned_users = ["dave"]

    if name in banned_users:
        print('❌', name, ' — доступ запрещён: пользователь в списке BANNED')
        return
    if name not in users:
        print('⚠️Пользователь не найден.')
        return

    current_user = users[name]
    if current_user['role'] in allowed_roles \
            and current_user['active']:
        print('✅', name, ' — доступ разрешён.')

    elif current_user['role'] not in allowed_roles:
        print('❌', name, '— доступ запрещён: роль', current_user['role'],'не имеет прав.')

    else:
        print('❌', name, '— доступ запрещён: неактивный аккаунт.')


checking_blacklist('bob')
