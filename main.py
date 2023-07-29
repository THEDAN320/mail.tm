import requests
import json
import fake_useragent
import secrets
from random import randint


def create_mail(mail: str, password: str) -> bool:
    session = requests.Session()
    session.headers = {"user-agent": fake_useragent.UserAgent().random}
    session.get("https://mail.tm/ru")
	
    data: dict = {"address": f"{mail}", "password": f"{password}"}
    headers: dict = {
        "accept": "application/ld+json",
        "Content-Type": "application/json",
    }
    response: requests.Response = session.post(
        "https://api.mail.tm/accounts", data=json.dumps(data), headers=headers
    )
	
    if response:
        return True
    else:
        return False


def creare_accounts() -> None:
    count: int = int(input("скок акков нада?>>"))
    mail: str = input("введи почту(без @mail и тд)>>")
   
    for i in range(count):
        new_mail: str = mail + f"_{i}@exelica.com"
        password: str = secrets.token_urlsafe(randint(5, 12))
        status: bool = create_mail(new_mail, password)
  
        with open("accounts.txt", "a") as file:
            if status:
                file.write(f"login - {new_mail}, password - {password}\n")
            else:
                file.write(f"error with login - {new_mail}\n")
    print("готово!")


if __name__ == "__main__":
    creare_accounts()
	