from pip._internal.operations.freeze import freeze
from faker import Faker
import random
import pandas as pd
import requests


def generate_name_email():
    result = []
    fake = Faker()
    domain = random.choice(["com", "ru", "ua"])
    domain_name = random.choice(["gmail", "mail", "i", "rambler"])
    names = [fake.unique.first_name() for _ in range(500)]
    name = random.choice(names)
    rand_email_name = "".join(list(random.choice("qwertyuiopasdfghjklzxcvbmn") for _ in range(random.randint(4, 10))))
    result.append(f"{name} {rand_email_name}@{domain_name}.{domain}")
    return result


def amount_users(amount):
    users = []
    for i in range(amount):
        users += generate_name_email()
    return str(users)


def write_requirements():
    requirements_txt = open("requirements.txt", "w+")
    for requirement_ in freeze(local_only=True):
        requirements_txt.write(requirement_)
    requirements_txt.close()
    return requirements_txt


def open_txt(filename):
    with open(filename, "r") as txt_file:
        read_txt = txt_file.read()
    return read_txt


def read_mean_hw_csv():
    file = pd.read_csv('hw.csv')
    mean_height_cm = file["Height(Inches)"].mean() * 2.54
    mean_weight_kg = file["Weight(Pounds)"].mean() / 2.205
    return f"Mean height cm = {mean_height_cm}, mean weight kg = {mean_weight_kg}"


def amount_astros_now():
    r = requests.get('http://api.open-notify.org/astros.json')
    read = r.json()["people"]
    amount_astros = 0
    for astros in read:
        amount_astros += 1
    return f"Amount Astros now: {amount_astros}"
