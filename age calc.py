from datetime import date
import os
from os import system
system("title " + "@c9zd - Age Calculator")

print("""
    
░█████╗░░██████╗░███████╗  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░██╗
██╔══██╗██╔════╝░██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║
███████║██║░░██╗░█████╗░░  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝██║
██╔══██║██║░░╚██╗██╔══╝░░  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗╚═╝
██║░░██║╚██████╔╝███████╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║██╗
╚═╝░░╚═╝░╚═════╝░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝
    """)
print("""
Cᴏᴅᴇᴅ Bʏ Aʜᴍᴇᴅ Iɴsᴛᴀ: @c9zd
""")

def age(birth_date):
    today = date.today()
    y = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        y -= 1

    return y

def main_calculator():
    Name = input("Tell us Your Name: ")
    while True:
        try:
            year = int(input("Enter Your Year of Birth: "))
        except:
            print("Value must be a number!")
            continue
        else: break
    while True:
        try:
            month = int(input("Enter Your Month of Birth: "))
        except:
            print("Value must be a number!")
            continue
        else: break
    while True:
        try:
            day = int(input("Enter Your Day of Birth: "))
        except:
            print("Value must be a number!")
            continue
        else: break

    birth_date = date(int(year),int(month),int(day))

    age_years = age(birth_date)
    
    print("Hello "+ Name)
    print("You are "+ str(age_years) + " years old")

while 1:
    startQ = input("Want me to Calculate Your Age? ").lower()
    if startQ == "yes":
        main_calculator()
    else:
        break

