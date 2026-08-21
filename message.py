a = str(input("Ismi: "))
b = int(input("ID: "))


def send_notification(*args, **kwargs):
    result = "Hisobot"

    for user in args:
        result += f"\n\nFoydalanuvchi: {user}"
        result += "\nHolat: Yuborildi\n"

        for key, value in kwargs.items():
            result += f"{key}: {value}\n"

    return result



natija = send_notification(a, b, title="Xabar", prority="high", channel="email")

print(natija)